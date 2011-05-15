Version Bump checker
====================

.. tags: en-us,gentoo

.. _`Frugalware Linux`: http://frugalware.org/
.. _Fabric: http://fabfile.org/
.. _`GNOME version bump checker`: http://git.overlays.gentoo.org/gitweb/?p=proj/gentoo-bumpchecker.git;a=summary

I think that one of the major pains for the package maintainers is to find
version updates. The problem is even bigger if the packages comes from a lot
of diferent places. The sci-electronics category is a good example of this, and
my main motivation to write a script.

The script can fetch the source code of a page and run it through a sequence of
shell commands. These commands will return the upstream version of the package,
inspired by the mechanism used by `Frugalware Linux`_ to find updates. After
that, the script compares the upstream version with the current Gentoo version
and generates a HTML file. The URLs and commands are stored in a .ini-style
file.

.. read_more

The script, that I called checkbump.py, is available here:

http://git.rafaelmartins.eng.br/?p=checkbump.git

You can clone it using the command::

    $ git clone git://git.rafaelmartins.eng.br/checkbump.git

You will need to have ``dev-python/jinja`` installed to be able to run the
script.

The generated HTML page, for some of the packages from sci-electronics, is
available here:

http://dev.gentoo.org/~rafaelmartins/checkbump/sci-electronics.html

The script is affected by overlays and still needs some improvement. Feel free
to clone the repository and e-mail me a patch. If you want to see the .ini
file, look at the ``config/`` directory of the Git repository.

A Fabric_ fabfile is also available on the repository, and is what I use to
create the files and upload them to the remote web server.

In a perfect world the maintainers would follow the mailing-lists and project
pages closely, but we know that this isn't always possible. On the other hand,
a public page with the information about the updated packages is good for the
members of the herd know the state of the packages they are maintaining, and
for the users as well.

I have plans to integrate this script as a module to another solution, like the
`GNOME version bump checker`_, but this works for now.

That's all.

Thanks.


.. date added automatically by the script blohg_dump.py.
   this file was exported from an old repository, and this comment will
   help me to forcing the old creation date, instead of the date of the
   first commit on the new repository.

.. date: 1290824826

