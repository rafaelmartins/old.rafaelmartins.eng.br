# -*- coding: utf-8 -*-
"""
    blohg_machines
    ~~~~~~~~~~~~~~

    A blohg extension that adds some rst directives to list informations about
    computer hardware.

    :copyright: (c) 2013 by Rafael Goncalves Martins
    :license: GPL-2, see blohg/LICENSE for more details.
"""

from docutils import nodes
from docutils.parsers.rst import directives, Directive

from blohg.ext import BlohgExtension

ext = BlohgExtension(__name__)


def text_field(key, value):
    field_name = nodes.field_name(key, key)
    field_body_p = nodes.paragraph(value, value)
    field_body = nodes.field_body('', field_body_p)
    return nodes.field('', field_name, field_body)


def bullet_list_field(key, value):
    items = []
    for item in value:
        item_p = nodes.paragraph(item, item)
        items.append(nodes.list_item('', item_p))
    bullet_list = nodes.bullet_list('', *items)
    field_name = nodes.field_name(key, key)
    field_body = nodes.field_body('', bullet_list)
    return nodes.field('', field_name, field_body)


def boolean_field(key, value):
    boolean_value = 'No'
    if value:
        boolean_value = 'Yes'
    return text_field(key, boolean_value)


def argument_list(separator=','):
    def inner(argument):
        if argument is None:
            return None
        return [item.strip() for item in unicode(argument).split(separator)]
    return inner


class MachineDirective(Directive):

    required_arguments = 1  # machine name
    option_spec = {
        'model': directives.unchanged,
        'aliases': argument_list(),
        'services': argument_list(),
        'cpu': argument_list(';'),
        'ram': argument_list(';'),
        'storage': argument_list(';'),
        'network': argument_list(';'),
        'os': directives.unchanged,
        'provider': directives.unchanged,
        'location': directives.unchanged,
        'virtual-machine': directives.flag,
        'public': directives.flag,
    }

    def run(self):
        childrens = [text_field('Name', self.arguments[0])]
        if 'model' in self.options:
            childrens.append(text_field('Model', self.options['model']))
        if 'aliases' in self.options:
            childrens.append(bullet_list_field('Aliases',
                                               self.options['aliases']))
        if 'services' in self.options:
            childrens.append(bullet_list_field('Services',
                                               self.options['services']))
        if 'cpu' in self.options:
            childrens.append(bullet_list_field('CPU', self.options['cpu']))
        if 'ram' in self.options:
            childrens.append(bullet_list_field('RAM', self.options['ram']))
        if 'storage' in self.options:
            childrens.append(bullet_list_field('Storage',
                                               self.options['storage']))
        if 'network' in self.options:
            childrens.append(bullet_list_field('Network',
                                               self.options['network']))
        if 'os' in self.options:
            childrens.append(text_field('Operating System',
                                        self.options['os']))
        if 'provider' in self.options:
            childrens.append(text_field('Provider', self.options['provider']))
        if 'location' in self.options:
            childrens.append(text_field('Location', self.options['location']))
        childrens.append(boolean_field('Virtual Machine',
                                       'virtual-machine' in self.options))
        childrens.append(boolean_field('Publicly accessible',
                                       'public' in self.options))
        return [nodes.field_list('', *childrens)]


@ext.setup_extension
def setup_extension(app):
    directives.register_directive('machine', MachineDirective)
