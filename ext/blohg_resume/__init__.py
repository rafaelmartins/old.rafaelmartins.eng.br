import babel
import re
from flask import current_app, render_template
from blohg.ext import BlohgBlueprint, BlohgExtension

ext = BlohgExtension(__name__)
resume = BlohgBlueprint('resume', __name__, url_prefix='/resume',
                        static_folder='static', template_folder='templates')

re_resume_src = re.compile(r'/resume\-([^\.-]+)\.rst$')

FORMATS = [('pdf', 'Portable Document Format (PDF)'),
           ('html', 'HyperText Markup Language (HTML)'),
           ('rst', 'ReStructuredText (RST)')]


def get_source_files():
    rv = []
    resume_dir = current_app.config['RESUME_DIR'].rstrip('/') + '/'
    for filename in current_app.blohg.changectx.files:
        if filename.startswith(resume_dir):
            rv.append(filename)
    return rv


def get_locales():
    def get_locale(locale):
        for _locale in sorted(babel.localedata.list()):
            if _locale.lower() == locale.lower():  # case-insensitive comparision
                return babel.Locale(_locale)

    rv = []
    for filename in get_source_files():
        match = re_resume_src.search(filename)
        if match is None:
            continue
        locale_id = match.group(1)
        rv.append((locale_id, get_locale(locale_id)))
    rv.sort(key=lambda x: x[0])
    return rv


@resume.route('/')
def home():
    return render_template('resume.html', locales=get_locales(), formats=FORMATS)


@resume.route('/resume-<language>.<file_format>')
def render(language, file_format):
    return '%s: %s' % (language, file_format)


@ext.setup_extension
def setup_extension(app):
    from blohg import Flask
    assert isinstance(app, Flask)
    app.config.setdefault('RESUME_DIR', 'resume')
    app.register_blueprint(resume)
