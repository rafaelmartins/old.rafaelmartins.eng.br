# -*- coding: utf-8 -*-
"""
    blohg_projects
    ~~~~~~~~~~~~~~

    A blohg extension that renders a page with information about projects
    hosted at github.com

    :copyright: (c) 2013 by Rafael Goncalves Martins
    :license: GPL-2, see blohg/LICENSE for more details.
"""

from datetime import timedelta
from dogpile.cache import make_region
from flask import current_app, render_template
from github import Github

from blohg.ext import BlohgBlueprint, BlohgExtension

ext = BlohgExtension(__name__)
projects = BlohgBlueprint('projects', __name__, url_prefix='/projects',
                          template_folder='templates')
cache = make_region().configure('dogpile.cache.memory',
                                expiration_time=timedelta(hours=1))


@cache.cache_on_arguments()
def get_projects_from_github(username, project_list):
    required_keys = ['description', 'homepage', 'html_url', 'name']
    gh = Github()
    user = gh.get_user(username)
    repos = user.get_repos()
    rv = []
    projects = dict([(project.name, project)
                     for project in repos])
    for project_name in project_list:
        if project_name not in projects:
            continue
        proj = {}
        for key in required_keys:
            proj[key] = getattr(projects[project_name], key)
        proj['username'] = username
        rv.append(proj)
    return rv


@projects.route('/')
def main():
    projects = []
    usernames = []
    for project_dict in current_app.config['GITHUB_PROJECTS']:
        for username, project_list in project_dict.iteritems():
            usernames.append(username)
            projects.extend(get_projects_from_github(username, project_list))
    return render_template('projects.html', usernames=usernames,
                           projects=projects)


@ext.setup_extension
def setup_extension(app):
    app.config.setdefault('GITHUB_PROJECTS', [])
    app.register_blueprint(projects)
