Reworking patches with Mercurial Queues
=======================================

.. tags: en-us,mercurial,git,gsoc,gentoo,diffball

The first task of my `GSoC project`_ was to add XZ support to diffball,
that is a tool that generates binary deltas for tarballs and binaries
in general.

.. _`GSoC project`: http://www.gentoo.org/proj/en/infrastructure/distpatch/

diffball is versioned using Git_, that isn't something I like, personally.
I usually do Git_ in the same way as I do CVS and other centralized version
control systems, resulting in a bad patch series.

As I don't know how to rework patches properly with Git_, I did it using
`Mercurial Queues`_ that are something I know better.

I'll show here how I reworked this patch series, as a mini-howto.

Enjoy :)

.. _Git: http://git-scm.com/
.. _`Mercurial Queues`: http://mercurial.selenic.com/wiki/MqExtension

.. read_more

Enable required extensions
--------------------------

I needed 2 extensions, hg-git_ and mq_. The first one for work in Git_
repositories with Mercurial_, and the last one to work with `Mercurial Queues`_.
hg-git_ needs to be installed manually. mq_ is shipped with Mercurial_.

.. _hg-git: http://hg-git.github.com/
.. _mq: http://mercurial.selenic.com/wiki/MqExtension
.. _Mercurial: http://mercurial.selenic.com/

This is what I added to my ~/.hgrc file::

    [extensions]
    hggit =
    mq = 


Cloning the repository and creating the queue
---------------------------------------------

I need to clone the repository and analyze the Mercurial_ log::
    
    $ hg clone git://pkgcore.org/diffball
    $ cd diffball
    $ hg log
    changeset:   451:481ff769b7fb
    bookmark:    personal/rafaelmartins/xz-support
    tag:         default/personal/rafaelmartins/xz-support
    tag:         tip
    user:        Rafael G. Martins <rafael@rafaelmartins.eng.br>
    date:        Sun May 22 22:48:50 2011 -0300
    summary:     actually added XZ functionality to libcfile.
    
    changeset:   450:421a260e9f28
    user:        Rafael G. Martins <rafael@rafaelmartins.eng.br>
    date:        Sun May 22 17:22:08 2011 -0300
    summary:     fixed typo when enabling dcbuffer debug
    
    changeset:   449:69a5b5d62cc1
    user:        Rafael G. Martins <rafael@rafaelmartins.eng.br>
    date:        Sun May 22 13:22:28 2011 -0300
    summary:     it's XZ, not LZMA.
    
    changeset:   448:566bd0ffd47c
    user:        Rafael G. Martins <rafael@rafaelmartins.eng.br>
    date:        Sun May 22 12:44:49 2011 -0300
    summary:     added liblzma build system checks, using pkgconfig
    
    changeset:   447:bf8e84c492de
    user:        Rafael G. Martins <rafael@rafaelmartins.eng.br>
    date:        Sun May 22 12:33:32 2011 -0300
    summary:     added LZMA auto-detection support.
    
    changeset:   446:5797215cb97f
    bookmark:    master
    tag:         default/master
    user:        Brian Harring <brian.harring@intel.com>
    date:        Thu Apr 07 13:52:26 2011 -0700
    summary:     update copyright/license specifics
    
    ...

My commits are 447:451. I need to convert them to mq patches, after
initialize the mq repository::
    
    $ hg init --mq
    $ hg qimport --git -r 447:451
    $ hg qseries 
    447.diff
    448.diff
    449.diff
    450.diff
    451.diff

Now I have 5 patches, with the local revision number as name. They are applied to
the original repository by default. I need to remove them before start re-adding
each one in the correct order::

    $ hg qpop -a


Reworking the patches
---------------------

I fixed a typo in the code that enable the dcbuffer debug. It's the 4th patch
in the original queue. As this patch isn't related to the XZ support I'm
implementing itself, I'll move it to the begin of the queue and rename it to
something better than the local revision number::
    
    $ hg qpush --move 450.diff
    applying 450.diff
    now at: 450.diff
    $ hg qmv 450.diff fixed-typo-when-enabling-dcbuffer-debug.diff

The patches ``447.diff`` and ``449.diff`` are related. I decided that I should
use the XZ name instead of LZMA, and changed the code of the first patch.
These 2 patches should be unified, creating a new patch::
    
    $ patch -p1 < .hg/patches/447.diff 
    patching file include/cfile.h
    patching file libcfile/cfile.c
    $ patch -p1 < .hg/patches/449.diff 
    patching file include/cfile.h
    patching file libcfile/cfile.c
    $ hg qnew --git --currentuser --currentdate -m "added XZ auto-detection support." added-xz-autodetection-support.diff
    $ hg qdelete 447.diff 449.diff

``.hg/patches`` is the Mercurial_ repository that the extension uses to store
the patches. It was created by the ``hg init --mq`` command.

The patch ``448.diff`` is ok, I'll just re-add it and rename:: 
    
    $ hg qpush 448.diff 
    applying 448.diff
    now at: 448.diff
    $ hg qmv 448.diff added-liblzma-build-system-checks-using-pkgconfig.diff

The last unnaplied patch I have is ``451.diff``, that is good, but the commit
message isn't ok. I'll re-add it, change the commit message and rename it::
    
    $ hg qpush 451.diff
    applying 451.diff
    now at: 451.diff
    $ hg qrefresh -m "added XZ functionality to libcfile."
    $ hg qmv 451.diff added-xz-functionality-to-libcfile.diff

At this point I have a Mercurial_ queue with the 4 reworked patches inside
``.hg/patches``::
    
    $ hg qseries
    fixed-typo-when-enabling-dcbuffer-debug.diff
    added-xz-autodetection-support.diff
    added-liblzma-build-system-checks-using-pkgconfig.diff
    added-xz-functionality-to-libcfile.diff

Commit the queue changes::
    
    $ hg commit --mq -m "added queue"

I can publish it somewhere using the command::
    
    $ hg push --mq $REMOTE_REPO_URL

My repository is here:

http://hg.rafaelmartins.eng.br/mq/diffball

This howto is far from perfect. I just wanted to give a quick introdution
for people that want to get started with this cool feature of Mercurial_. :)

That's all!

Thanks!
