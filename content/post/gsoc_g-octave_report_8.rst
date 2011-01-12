GSoC - g-Octave - weekly report #8
==================================

.. tags: gentoo,g-octave,gsoc,octave

Hi folks,

here is my weekly report #8.

.. read_more


GSoC report: g-Octave (Improve Octave/Matlab support)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

July 13
-------

* Fixed some tests.
* Updated the documentation.
* Disabled the logging feature for run the tests.
* Fixed some general stuff to the release.
* Released g-octave 0.3


July 14
-------

* Added some stuff to the package manager classes to help with the listing
  of users with permissions to run each package manager.
* Added a Python module (g_octave/compat.py) to help with the compatibility
  of g-octave with py3k.
* Ported all the modules to py3k.
* Ported the helper packages to py3k.
* Ported the scripts to py3k.
* Ported the test suite to py3k.
* Added a cleanup of environment variables to the script that runs the test
  suite, because these variables can broke some tests.
* Finished the py3k porting.


July 15
-------

* Finished the work to restrict the use of g-octave to the users allowed to
  run the current selected package manager.
* Added some stuff to check if the current selected package manager is really
  installed.


July 16
-------

* Not a lot of work, only some discussions about the next milestones.


July 19
-------

* Testing some stuff to the next milestone.

-------------------

That's all for now.


.. date added automatically by the script blohg_dump.py.
   this file was exported from an old repository, and this comment will
   help me to forcing the old creation date, instead of the date of the
   first commit on the new repository.

.. date: 1279572090

