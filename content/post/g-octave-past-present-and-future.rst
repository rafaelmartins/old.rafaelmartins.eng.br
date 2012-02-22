g-octave: past, present and future
==================================

.. tags: en-us,gentoo,g-octave

Hi people,

I started g-octave_ in the end of 2009, as a pet project. I was needing
something better to deal with octave-forge_ software than the old
``sci-mathematics/octave-forge-*`` packages distributed by the gentoo-science
overlay. In a few weeks it was already able to do the basic stuff:
install/uninstall packages, manage the package database, etc. I had a lot of
fun working on this project.

.. _g-octave: http://g-octave.org/
.. _octave-forge: http://octave.sf.net/

.. read_more

Some time after I start the project, the Gentoo Foundation announced the
call for proposals for the Google Summer of Code 2010. I sent a proposal and
it was accepted. This was an awesome job: improve the software I created and
be paid for it. :o)

g-octave_ improved heavily during the 3 months of Google Summer of Code and
I considered it ready to replace the old packages from the overlay, reducing
the amount of maintenance needed.

But my amount of time available to work on this project reduced on the last
months. I was busy with an internship at the start of the year, my bachelor
thesis, and I also participated of the Google Summer of Code again, with
another project. Now I'm starting a job and I don't know when I will have free
time again.

Some people started complaining about the "lack of maintenance" of
the project. The complains actually started almost a year ago,
`on the forums`_, but I don't read Gentoo forums at all. I just noticed
this today, when someone moved the topic to the gentoo-science mailing list.

.. _`on the forums`: http://forums.gentoo.org/viewtopic-t-854170-highlight-goctave.html

What this people can't see is that the project **was created to reduce the
maintenance efforts**. I mean, it provides tools to allow people to install
fresh software, even if the default package database is outdated.

Things like the ``--scm`` option and the script ``contrib/manage_pkgdb.py``
allow anyone to install new versions of packages and/or update the `package
database on GitHub`_, sending me a pull request to update the *official*
database.

.. _`package database on GitHub`: https://github.com/rafaelmartins/g-octave-db

Everything is documented on the `project website`_, but looks like this
people don't read the docs nor the elog messages at the end of the installation
of g-octave. This behavior results on users that don't know the features of the
tool and that can't use it because *forgot* to run ``emerge --config g-octave``.

.. _`project website`: http://g-octave.org/

This kind of behavior really annoys me.

I updated the package database, added a g-octave-0.4.1-r2 ebuild to the
tree and closed a few bugs. Feel free to do future updates by yourself on
GitHub and send me a pull request.

I don't know what will happen with the project in the future. The maintainer of
the old-style packages retired from Gentoo and was bored of maintain these
packages, IIRC. I stopped using octave a few months ago, and looks like I'll
not use it for the coming months or years.

I'll still do whatever I can to keep g-octave_ working, but please be kind and
contribute, instead of complain.

Thanks!
