# -*- coding: utf-8 -*-
"""
    blohg_draft
    ~~~~~~~~~~~

    A blohg extension that adds a rst directive, to mark a post/page as draft.

    :copyright: (c) 2014 by Rafael Goncalves Martins
    :license: GPL-2, see blohg/LICENSE for more details.
"""

from docutils.statemachine import StringList
from docutils.parsers.rst.directives import register_directive
from docutils.parsers.rst.directives.body import BlockQuote

from blohg.ext import BlohgExtension

ext = BlohgExtension(__name__)


class DraftDirective(BlockQuote):

    has_content = False

    def __init__(self, name, arguments, options, content, lineno,
                 content_offset, block_text, state, state_machine):
        # this is the ugliest hack ever!!!
        content_offset += 1
        content = StringList(
            [u'**Warning**: This is a draft! Content is a work in progress!'],
            items=[(state.document.current_source, content_offset),])
        self.has_content = True
        return BlockQuote.__init__(self, name, arguments, options, content,
                                   lineno, content_offset, block_text, state,
                                   state_machine)


@ext.setup_extension
def setup_extension(app):
    register_directive('draft', DraftDirective)
