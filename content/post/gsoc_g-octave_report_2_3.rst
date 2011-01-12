GSoC - g-Octave - weekly report #2 #3
=====================================

.. tags: gentoo,g-octave,gsoc,summer_of_code,octave

Hi folks,

sorry for the delay and the lack of informations about the project.

As usual, I'm sending daily reports to my mentor, and this "weekly" report is
based on those daily reports.

During this period I wrote some documentation, that's available here:

http://soc.dev.gentoo.org/~rafaelmartins/g-octave/docs

Fixes to the documentation are welcome, as always.

I'll post the weekly report #4 soon.

.. read_more


GSoC report: g-Octave (Improve Octave/Matlab support)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

May 31
------

 * Not much work, only some fixes in the tests.


June 1
------

 * Started planning the implementation of the tinderbox stuff.
 * Studied the flameeyes' tinderbox scripts.


June 2
------

 * Started the tinderbox script. The basic functionality is done. The script
   is already capable to find all the packages in the database and build
   them.


June 3
------

 * Added a module to interact with the Trac instance. Written firstly to use
   urllib2, but urllib2 doesn't supports file uploads, then I needed to port
   the module to use pyCurl.
 * Fixes in the tinderbox script.


June 4
------

 * Finished tinderbox script
 * Written static docs: http://soc.dev.gentoo.org/~rafaelmartins/
 * Released g-octave 0.1.


June 7
------

 * Started the script to extract the non-octave dependencies from the
   DESCRIPTION files and generate the JSON file used by g-octave


June 8
------

 * Finished the script to create and edit the JSON file with the non-octave
   dependencies.


June 9
------

 * More small fixes to the script that generates the JSON file with the
   non-octave dependencies.


June 10
-------

 * Small fixes to the script 'requirements.py'
 * Implemented a filter for duplicated dependencies
 * Documentation fixes for the coming release


June 11
-------

 * Released g-octave 0.2_rc1


June 14
-------

 * Started the next milestone
 * Created a class to handle the SVN stuff, using pysvn


June 15
-------

 * More work in the previously created class.
 * Created a class to handle the SVN revisions number, using a JSON file.

-------------------

That's all for now.


.. date added automatically by the script blohg_dump.py.
   this file was exported from an old repository, and this comment will
   help me to forcing the old creation date, instead of the date of the
   first commit on the new repository.

.. date: 1277274500

