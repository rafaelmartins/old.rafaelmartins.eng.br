GSoC - g-Octave - weekly report #9
==================================

.. tags: gentoo,g-octave,gsoc,octave

Hi folks,

here is my weekly report #9.

.. read_more


GSoC report: g-Octave (Improve Octave/Matlab support)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

July 20
-------

* Did a lot of tests with some matlab packages that are supposed to works with octave.


July 21
-------

* Implemented the search of octave-forge packages (*-s*/*--search* command-line option).


July 22
-------

* Started removing the implicit hardmask of live versions. The users will need to use
  the configuration file to say if they want to create the ebuild for the live versions
  or not (*use_scm* option). Additionally, the users can disable or enable the installation
  of the live version using the command line (*--scm* and *--no-scm* options). As part
  of this change of behavior, the user will still need to unmask the package on the package
  manager configuration files, in order to install the live version of the package.
  

July 23
-------

* g-octave stuff got new home (thanks ferringb) and a new domain name (http://www.g-octave.org).
  Spent the day configuring the trac instance, not done yet, but already works fairly.


July 24
-------

* Fixed some bugs with the automated tests, that broke with the new trac instance. Some
  work on this is still needed.


July 26
-------

* Finished the work to remove the implicit hardmask of live versions and the implementation
  of the new behavior.


-------------------

That's all for now.


.. date added automatically by the script blohg_dump.py.
   this file was exported from an old repository, and this comment will
   help me to forcing the old creation date, instead of the date of the
   first commit on the new repository.

.. date: 1280286841

