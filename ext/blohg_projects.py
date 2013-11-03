# -*- coding: utf-8 -*-
"""
    blohg_projects
    ~~~~~~~~~~~~~~

    A blohg extension that adds a reStructuredText directive to show info about
    open-source projects.

    :copyright: (c) 2012-2013 by Rafael Goncalves Martins
    :license: GPL-2, see blohg/LICENSE for more details.
"""

import json
import posixpath

from contextlib import closing
from docutils import nodes
from docutils.parsers.rst import directives, Directive
from urllib2 import urlopen

from blohg.ext import BlohgExtension

ext = BlohgExtension(__name__)


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
    }
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
    }

    def run(self):
        options = get_pypi_data(self.arguments[0])
        options.update(self.options)
        self.options = options
        return Project.run(self)


@ext.setup_extension
def setup_extension(app):
    directives.register_directive('project', Project)
    directives.register_directive('pypi-project', PyPIProject)
