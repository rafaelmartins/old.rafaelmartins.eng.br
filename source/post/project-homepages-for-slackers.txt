Project homepages for slackers
==============================

.. tags: en-us,gentoo,mercurial

.. pull-quote::

   **Warning**: This project is deprecated. Look at
   http://rafaelmartins.eng.br/projects/

Create a homepage and documentation for a project is a boring task. I
have a few projects that were not released yet due to lack of time and
motivation to create a simple webpage and write down some Sphinx_-based
documentation.

.. _Sphinx: http://sphinx-doc.org/

To fix this issue I did a quick hack based on my favorite pieces of
software: Flask_, docutils_ and Mercurial_. It is a single file web
application that creates homepages automatically for my projects, using
data gathered from my `Mercurial repositories`_. It uses the tags, the
README file, and a few variables declared on the repository's ``.hgrc``
file to build an interesting homepage for each project. I just need to
improve my READMEs! :)

.. _Flask: http://flask.pocoo.org/
.. _docutils: http://docutils.sourceforge.net/
.. _Mercurial: http://mercurial.selenic.com/
.. _`Mercurial repositories`: http://hg.rafaelmartins.eng.br/

It works similarly to the `PyPI Package Index`_, but accepts any project
hosted on a Mercurial repository, including my non-Python and Gentoo-only
projects.

.. _`PyPI Package Index`: http://pypi.python.org/

My instance of the application lives here (not anymore):

http://projects.rafaelmartins.eng.br/

The application is highly tied to my workflow, e.g. the way I handle tags
and the directory structure of my repositories on my server, but the code
is available in a Mercurial repository:

https://github.com/rafaelmartins/projects/

Most of my projects aren't listed yet, and I'll start enabling them as soon
as I fix their READMEs.
