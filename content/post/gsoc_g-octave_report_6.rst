GSoC - g-Octave - weekly report #6
==================================

.. tags: gentoo,g-octave,gsoc,summer_of_code,octave

Hi folks,

here is my weekly report #6.

.. read_more


GSoC report: g-Octave (Improve Octave/Matlab support)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

June 30
-------

* More changes on g-octave to be able to work with SVN stuff.
* Finished the stuff to create new package databases.


July 1
------

* Introduced the support of the installation from SVN to the module g_octave.ebuild.
* Fixed some test cases.
* Changed g-octave to be able to work with a package database installed by portage.
  (octave-forge databases now "live" on the SRC_URI of g-octave's ebuild)
* Changed g-octave to only fetch a package database directly from the mirrors if the
  user is with the live version of g-octave installed.
* Fixed the documentation for the coming release.
* More minor fixes.
* Released g-octave 0.2.


July 2
------

* Fixed the ebuilds to g-octave 0.2 and to add the pysvn dependency.
* Bug fixes: missing source tarballs (optim and ode), and missing $OCT_PKGDIR for the
  fresh octave installations. (reported by Paulo Matias, thanks!)
* Released g-octave 0.2.1.


July 3
------

* Added support to logging actions to a file. not used in the source code yet.


July 4
------

* Only small bug fixes in the eclass g-octave.eclass.


July 5
------

* Started moving the g-octave stuff from a VPS to the Gentoo infrastructure
  (Moved the source control to Git and the octave-forge's source tarballs to
  http://soc.dev.gentoo.org/~rafaelmartins). More details about this in a next
  post.


-------------------

That's all for now.


.. date added automatically by the script blohg_dump.py.
   this file was exported from an old repository, and this comment will
   help me to forcing the old creation date, instead of the date of the
   first commit on the new repository.

.. date: 1278394565

