# -*- coding: utf-8 -*-
"""
    blohg_redirect
    ~~~~~~~~~~~~~~

    A blohg extension that redirects internal urls to any url registered in
    the configuration file.

    :copyright: (c) 2014 by Rafael Goncalves Martins
    :license: GPL-2, see blohg/LICENSE for more details.
"""

from blohg.ext import BlohgBlueprint, BlohgExtension
from flask import abort, current_app, redirect

ext = BlohgExtension(__name__)
go = BlohgBlueprint('redirect', __name__, url_prefix='/go')


@go.route('/<path:slug>/')
def redirect_view(slug):
    if 'REDIRECT' not in current_app.config:
        abort(404)
    destination = current_app.config['REDIRECT'].get(slug)
    if destination is None:
        abort(404)
    return redirect(destination)


@ext.setup_extension
def setup_extension(app):
    app.register_blueprint(go)
