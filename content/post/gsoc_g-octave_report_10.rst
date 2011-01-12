GSoC - g-Octave - weekly report #10
===================================

.. tags: gentoo,g-octave,gsoc,octave

Hi folks,

here is my weekly report #10.

.. read_more


GSoC report: g-Octave (Improve Octave/Matlab support)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

July 27
-------

* Tested some Python libraries to work with Git repositories.


July 28
-------

* Nothing done.


July 29
-------

* Did more tests with Python libraries to work with Git repositories


July 30
-------

* Found a RSS feed with the package releases of octave-forge and wrote scripts
  to build the package database using that feed (``contrib/manage_pkgdb.py`` and
  ``contrib/manage_info.py``)
* Moved away from the Python libraries to work with Git repositories and wrote a
  simple class to call the git binary directly. It's fair enough for what I needed.
* Moved the package database to GitHub and rewrote the module g-octave.fetch to
  get the package database from GitHub, using the snapshot tarballs.


July 31
-------

* Did some changes to remove the PySVN dependency.
* Rewrote the command-line option ``--list``.
* Fixed the eclass to remove the forced strip from mkoctfile calls and more small fixes.
* Added the command-line option ``--oneshot``.
* Did a clean up on the sources.


August 1
--------

* Added the command-line option ``--list-raw``.
* Wrote a new script to do automated build tests, using XML-RPC (``contrib/tinderbox.py``).
* Did a first round of automated tests using the new script, using my laptop.
  Report: http://article.gmane.org/gmane.linux.gentoo.science/1360


August 2
--------

* Added metadata.xml to the ebuild directories.
* Improved the license support on the ebuilds. The ``LICENSE`` variable from the ebuilds
  now matches with the license names found on ``${PORTDIR}/licenses``
* Started updating the documentation for the coming release.


-------------------

That's all for now.


.. date added automatically by the script blohg_dump.py.
   this file was exported from an old repository, and this comment will
   help me to forcing the old creation date, instead of the date of the
   first commit on the new repository.

.. date: 1280963513

