# -*- coding: utf-8 -*-
"""
    blohg_projects
    ~~~~~~~~~~~~~~

    A blohg extension that renders a page with information about projects
    hosted at github.com

    :copyright: (c) 2013 by Rafael Goncalves Martins
    :license: GPL-2, see blohg/LICENSE for more details.
"""

from docutils import nodes
from docutils.parsers.rst import directives, Directive

from flask import render_template_string
from blohg.ext import BlohgExtension

ext = BlohgExtension(__name__)

TEMPLATE = '''\
<table class="project-table field-list">
    <tr class="field">
        <th class="field-name" colspan="2">
            {% if homepage or github_url %}<a href="{{
                homepage or github_url }}">{% endif %}
                {{ repository }}
            {% if homepage or github_url %}</a>{% endif %}
        </th>
    </tr>
    {%- if description %}
    <tr class="field">
        <th class="field-name">Description:</th>
        <td class="field-body">{{ description }}</td>
    </tr>
    {%- endif %}
    {%- if homepage %}
    <tr>
        <th class="field-name">Home page:</th>
        <td class="field-body">
            <a href="{{ homepage }}">{{ homepage }}</a>
        </td>
    </tr>
    {%- endif %}
    <tr>
        <th class="field-name">GitHub repository:</th>
        <td class="field-body">
            <a href="{{ github_url }}">{{ github_url }}</a>
        </td>
    </tr>
</table>'''


class ProjectDirective(Directive):

    required_arguments = 1  # repo-owner/repo-name
    option_spec = {'description': directives.unchanged_required,
                   'homepage': directives.unchanged}

    def run(self):
        # FIXME: Use proper docutils nodes instead of raw HTML.
        repository = self.arguments[0]
        github_url = 'https://github.com/%s' % repository
        homepage = self.options.get('homepage')
        description = self.options['description']
        html = render_template_string(TEMPLATE, repository=repository,
                                      github_url=github_url,
                                      homepage=homepage,
                                      description=description)
        return [nodes.raw('', html, format='html')]


@ext.setup_extension
def setup_extension(app):
    directives.register_directive('project', ProjectDirective)
