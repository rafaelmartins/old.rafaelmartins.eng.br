# -*- coding: utf-8 -*-
"""
    blohg_projects
    ~~~~~~~~~~~~~~

    A blohg extension that renders a page with information about projects
    hosted at github.com

    :copyright: (c) 2013 by Rafael Goncalves Martins
    :license: GPL-2, see blohg/LICENSE for more details.
"""

import requests
from datetime import timedelta
from dogpile.cache import make_region
from flask import current_app, render_template

from blohg.ext import BlohgBlueprint, BlohgExtension

ext = BlohgExtension(__name__)
projects = BlohgBlueprint('projects', __name__, url_prefix='/projects',
                          template_folder='templates')
cache = make_region().configure('dogpile.cache.memory',
                                expiration_time=timedelta(hours=1))


@cache.cache_on_arguments()
def get_projects_from_github(username, projects):
    required_keys = ['description', 'homepage', 'html_url', 'name']
    headers = {'Accept': 'application/vnd.github.v3'}
    response = requests.get('https://api.github.com/users/%s/repos' % username,
                            headers=headers)
    if not response.ok:
        raise RuntimeError('Failed to get projects: %s' % username)
    rv = []
    for project in response.json():
        if project['name'] not in projects:
            continue
        proj = {}
        for key in required_keys:
            proj[key] = project[key]
        rv.append(proj)
    return rv


@projects.route('/')
def main():
    username = current_app.config['GITHUB_USERNAME']
    project_list = current_app.config['GITHUB_PROJECTS']
    projects = get_projects_from_github(username, project_list)
    return render_template('projects.html', username=username,
                           projects=projects)


@ext.setup_extension
def setup_extension(app):
    app.config.setdefault('GITHUB_PROJECTS', [])
    app.register_blueprint(projects)
