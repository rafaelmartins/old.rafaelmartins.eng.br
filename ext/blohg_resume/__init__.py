import babel
import logging
import re

from contextlib import closing
from cStringIO import StringIO
from docutils.core import publish_string
from flask import abort, current_app, render_template, make_response, url_for
from flask.helpers import locked_cached_property

from blohg.ext import BlohgBlueprint, BlohgExtension
from blohg.signals import reloaded

ext = BlohgExtension(__name__)
resume = BlohgBlueprint('resume', __name__, url_prefix='/resume',
                        static_folder='static', template_folder='templates')


class ResumeLocale(object):

    re_resume_src = re.compile(r'/resume\-([^\.-]+)\.rst$')
    file_formats = [('pdf', 'Portable Document Format (PDF)'),
                    ('html', 'HyperText Markup Language (HTML)'),
                    ('rst', 'ReStructuredText (RST)')]

    def __init__(self, blohg, filepath):  # filepath relative to repository root
        self.blohg = blohg
        self.filepath = filepath
        self.locale_id = None
        self.locale = None
        match = self.re_resume_src.search(self.filepath)
        if match is None:
            return
        self.locale_id = match.group(1)
        self.locale = babel.Locale.parse(self.locale_id)
        self.filectx = blohg.changectx.get_filectx(self.filepath)
        self.content = self.filectx.content

    @locked_cached_property
    def rst(self):
        if self.filectx is None:
            abort(404)
        rv = make_response(self.content)
        rv.headers['Content-Type'] = 'text/plain; charset="utf-8"'
        return rv

    @locked_cached_property
    def html(self):
        if self.filectx is None:
            abort(404)
        settings = {'stylesheet': [
                        url_for('.static', filename='html4css1.css'),
                        url_for('.static', filename='resume.css')],
                    'stylesheet_path': None,
                    'embed_stylesheet': False,
                    'input_encoding': 'utf-8',
                    'output_encoding': 'utf-8',
                    'initial_header_level': 2}
        rv = make_response(publish_string(source=self.content,
                                          writer_name='html4css1',
                                          settings_overrides=settings))
        rv.headers['Content-Type'] = 'text/html; charset="utf-8"'
        return rv

    @locked_cached_property
    def pdf(self):
        from rst2pdf.createpdf import RstToPdf
        from rst2pdf.styles import CallableStyleSheet
        if self.filectx is None:
            abort(404)
        stylesheet_filename = resume.repo_static_folder + '/resume.style'
        stylesheet = CallableStyleSheet(stylesheet_filename,
                                        self.blohg.changectx.get_filectx(stylesheet_filename).content)
        parser = RstToPdf(breaklevel=0, stylesheets=[stylesheet])
        with closing(StringIO()) as fp:
            parser.createPdf(text=self.content, output=fp)
            rv = make_response(fp.getvalue())
        rv.headers['Content-Type'] = 'application/pdf'
        return rv


def reload_context(sender):
    ext.g.locales = []
    resume_dir = sender.app.config['RESUME_DIR'].rstrip('/') + '/'
    for filepath in sender.changectx.files:
        if not filepath.startswith(resume_dir):
            continue
        locale = ResumeLocale(sender, filepath)
        if locale.locale_id is None:
            continue
        ext.g.locales.append(locale)
    ext.g.locales.sort(key=lambda x: x.locale_id)


@resume.route('/')
def home():
    return render_template('resume.html', locales=ext.g.locales)


@resume.route('/resume-<language>.<file_format>')
def render(language, file_format):
    if file_format not in [i[0] for i in ResumeLocale.file_formats]:
        abort(404)
    locale = None
    for l in ext.g.locales:
        if l.locale_id == language:
            locale = l
    if locale is None:
        abort(404)
    #if not hasattr(locale, file_format):
    #    abort(404)
    return getattr(locale, file_format)


@ext.setup_extension
def setup_extension(app):
    from blohg import Flask
    assert isinstance(app, Flask)
    app.config.setdefault('RESUME_DIR', 'resume')
    app.register_blueprint(resume)
    reloaded.connect(reload_context)
