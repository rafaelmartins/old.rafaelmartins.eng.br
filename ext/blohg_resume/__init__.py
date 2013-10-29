import babel
import logging
import re

from contextlib import closing
from docutils.core import publish_string
from flask import abort, render_template, make_response, url_for
from flask.helpers import locked_cached_property

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

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

    def __init__(self, blohg, filepath):
        # filepath is relative to repository root
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
        ss_filename = resume.repo_static_folder + '/resume.style'
        ss_filectx = self.blohg.changectx.get_filectx(ss_filename)
        ss = CallableStyleSheet(ss_filename, ss_filectx.content)
        parser = RstToPdf(breaklevel=0, stylesheets=[ss])
        with closing(StringIO()) as fp:
            parser.createPdf(text=self.content, output=fp)
            rv = make_response(fp.getvalue())
        rv.headers['Content-Type'] = 'application/pdf'
        return rv


@reloaded.connect
def embed_pdf_fonts(sender):
    from reportlab.lib.fonts import addMapping
    from reportlab.pdfbase.pdfmetrics import registerFont
    from reportlab.pdfbase.ttfonts import TTFont

    # FIXME: the fonts shouldn't be hardcoded here :(
    fonts = ['DroidSans', 'DroidSans-Bold', 'DroidSans', 'DroidSans']
    registered_fonts = []

    for font in fonts:
        if font in registered_fonts:
            continue
        font_filename = '%s/fonts/%s.ttf' % (resume.repo_static_folder, font)
        font_filectx = sender.changectx.get_filectx(font_filename)
        with closing(StringIO(font_filectx.data)) as fp:
            registerFont(TTFont(font, fp))
        registered_fonts.append(font)

    addMapping(fonts[0], 0, 0, fonts[0])
    addMapping(fonts[0], 0, 1, fonts[2])
    addMapping(fonts[0], 1, 0, fonts[1])
    addMapping(fonts[0], 1, 1, fonts[3])


@reloaded.connect
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
            break
    if locale is None or not hasattr(locale, file_format):
        abort(404)
    return getattr(locale, file_format)


@ext.setup_extension
def setup_extension(app):
    ext.g.locales = []
    app.config.setdefault('RESUME_DIR', 'resume')
    app.register_blueprint(resume)
    reload_context(app.blohg)
