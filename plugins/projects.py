# -*- coding: utf-8 -*-
"""
    projects
    ~~~~~~~~

    A blohg plugin that adds a reStructuredText directive to show info about
    open-source projects.

    :copyright: (c) 2012 by Rafael Goncalves Martins
    :license: GPL-2, see blohg/LICENSE for more details.
"""

from blohg.rst import parser
from contextlib import closing
from docutils import nodes
from docutils.parsers.rst import directives, Directive
from flask import current_app as app
from urllib2 import urlopen
from werkzeug.contrib.cache import FileSystemCache, NullCache
import json
import posixpath

if app.debug:
    cache = NullCache()
else:
    cache = FileSystemCache(app.config.get('CACHE_DIR', '/tmp'),
                            default_timeout=int(
                                app.config.get('CACHE_TIMEOUT', 300)))


def text_field(key, value):
    field_name = nodes.field_name(key, key)
    field_body_p = nodes.paragraph(value, value)
    field_body = nodes.field_body('', field_body_p)
    return nodes.field('', field_name, field_body)


def reference_field(key, value, value_text=None):
    field_name = nodes.field_name(key, key)
    field_body_ref = nodes.reference(value, value_text or value, refuri=value)
    field_body_p = nodes.paragraph('', '', field_body_ref)
    field_body = nodes.field_body('', field_body_p)
    return nodes.field('', field_name, field_body)


def get_pypi_data(project_id):
    key = 'projects_' + project_id
    value = cache.get(key)
    if value is not None:
        return value
    project_url = 'http://pypi.python.org/pypi/%s/json' % project_id
    try:
        with closing(urlopen(project_url)) as fp:
            value = json.load(fp)
    except:
        return None
    # I always provide sdist :)
    for f in value['urls']:
        if f['packagetype'] == 'sdist':
            donwload_url = f['url']
            break
    info = {
        'description': value['info']['summary'],
        'latest-version': value['info']['version'],
        'homepage': value['info']['home_page'],
        'download-url': donwload_url or '',
        'license': value['info']['license'],
        'long_description': parser(value['info']['description'])['fragment'],
    }
    cache.set(key, info)
    return info


class Project(Directive):

    option_spec = {
        'description': directives.unchanged,
        'latest-version': directives.unchanged,
        'homepage': directives.uri,
        'download-url': directives.uri,
        'repository-type': directives.unchanged,
        'repository-url': directives.uri,
        'license': directives.unchanged,
    }

    def run(self):
        childrens = []
        if 'description' in self.options:
            childrens.append(text_field('Description',
                                        self.options['description']))
        if 'latest-version' in self.options:
            childrens.append(text_field('Latest version',
                                        self.options['latest-version']))
        if 'homepage' in self.options:
            childrens.append(reference_field('Homepage',
                                        self.options['homepage']))
        if 'download-url' in self.options:
            url = self.options['download-url']
            childrens.append(reference_field('Download URL', url,
                                        posixpath.basename(url)))
        if 'repository-url' in self.options:
            key = 'Repository URL'
            if 'repository-type' in self.options:
                key += ' (%s)' % self.options['repository-type']
            childrens.append(reference_field(key,
                                             self.options['repository-url']))
        if 'license' in self.options:
            childrens.append(text_field('License',
                                        self.options['license']))
        return [nodes.field_list('', *childrens)]


class PyPIProject(Project):
    """It is like Project, but fetches project info from PyPI."""

    required_arguments = 1  # project id
    option_spec = {
        'description': directives.unchanged,
        'latest-version': directives.unchanged,
        'homepage': directives.uri,
        'download-url': directives.uri,
        'repository-type': directives.unchanged,
        'repository-url': directives.uri,
        'license': directives.unchanged,
        'hide-long-description': directives.flag,
    }

    def run(self):
        options = get_pypi_data(self.arguments[0])
        options.update(self.options)
        tmp = []
        if len(options):
            warning = 'At least part of the data above was grabbed ' \
                'automatically from PyPI.'
            if 'hide-long-description' not in self.options:
                tmp.append(nodes.raw('', options['long_description'],
                                     format='html'))
            tmp.append(nodes.warning('', nodes.paragraph(warning, warning)))
        self.options = options
        del self.options['long_description']
        return Project.run(self) + tmp


directives.register_directive('project', Project)
directives.register_directive('pypi-project', PyPIProject)
