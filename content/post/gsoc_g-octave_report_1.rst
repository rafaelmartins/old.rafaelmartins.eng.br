GSoC - g-Octave - weekly report #1
==================================

.. tags: gentoo,g-octave,gsoc,summer_of_code,octave

.. _g-Octave: http://g-octave.rafaelmartins.eng.br/
.. _`Google Summer of code 2010`: http://socghop.appspot.com/
.. _`Gentoo Foundation`: http://www.gentoo.org/

Hi folks,

as said in the previous post, I'm finishing the development of g-Octave_ as
part of the `Google Summer of code 2010`_, for the `Gentoo Foundation`_.

This is my first weekly report, written based on my daily reports, that are
sent to my mentor (Denis Dupeyron).

I started working in May 21, then this report is for more than a week.

My roadmap can be seen here:

http://g-octave.rafaelmartins.eng.br/roadmap

.. read_more


GSoC report: g-Octave (Improve Octave/Matlab support)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

May 21
------

* Created the script to run the tests, using the Python module unittest.
  (scripts/run_tests.py)


May 22
------

* Several fixes to the script run_tests.py.
* Added tests to the module g_octave.description. (tests/test_description.py)


May 23
------

* Rewritten the module g_octave.description, that is basically the parser of
  the DESCRIPTION files, to fix some issues. Added a bunch of comments.


May 24
------

* Small fixes on the tests of the module g_octave.description.


May 25
------

* Nothing done. :(


May 26
------

* Added tests to the module g_octave.description_tree.
  (tests/test_description_tree.py)
* Started tests to the modules g_octave.config and g_octave.ebuild.


May 27
------

* Added tests to the module g_octave.config. (tests/test_config.py)
* Amended the module g_octave.config to be able to run the tests.
* Added tests to the module g_octave.overlay. (tests/test_overlay.py)
* Amended the module g_octave.overlay to be able to run the tests.
* Started tests to the module g_octave.ebuild.


May 28
------

* Added tests to the module g_octave.overlay. (tests/test_overlay.py)
* Created an example tree with DESCRIPTION files and all the aditional.
  files needed by g-octave, to help with the tests.
* Amended the previously implemented tests and the g_octave modules to
  use ths example tree in the tests.
* Added tests to the module g_octave.ebuild. (tests/test_ebuild.py)


May 29
------

* Finished tests to the module g_octave.ebuild.
* Several fixes in the tests to all the modules.
* Added a src_test phase to the live ebuild.


-------------------

That's all for now.


.. date added automatically by the script blohg_dump.py.
   this file was exported from an old repository, and this comment will
   help me to forcing the old creation date, instead of the date of the
   first commit on the new repository.

.. date: 1275354559

