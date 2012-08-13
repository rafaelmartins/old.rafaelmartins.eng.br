Deploying blohg to bitbucket
============================

.. tags: en-us,blohg,bitbucket,mercurial

Bitbucket_ is a repository hosting service widely used by Mercurial_ users.
Its basic plan is free and includes unlimited private repositories.

.. _Bitbucket: http://bitbucket.org/
.. _Mercurial: http://mercurial.selenic.com/

Some people don't know, because it isn't widely advertised, but Bitbucket_
provides free web hosting for static files. Any files stored in a repo called
``username.bitbucket.org`` will be served from http://username.bitbucket.org/.
It just works for user names, as far as I know.

.. read_more

Some documentation is available here:

https://confluence.atlassian.com/display/BITBUCKET/Publishing+a+Website+on+bitbucket

I never cared about creating a way to build a static version of a blohg-based
blog, but blohg is open-source and someone else cared about it. :)

Benoît Allard implemented a ``freeze`` command for blohg, that uses the
Frozen-Flask_ extension to create a static version of the blog, and it was
merged with blohg a long time ago.

.. _Frozen-Flask: http://packages.python.org/Frozen-Flask/

I will list here the basic steps required to get your blohg-based blog
running on Bitbucket_.


Creating the Bitbucket repository
---------------------------------

First of all, create a repository using the Bitbucket web interface.
It should be named ``username.bitbucket.org``. For example, if your username
is ``john``, your repository will be ``john.bitbucket.org``. I'll use ``blohg``
as the username for this example.


Setting up your blohg repository before "freeze" the content
------------------------------------------------------------

Supposing that you already have a blohg repository with the sources of your
blog, created following the `official documentation <http://docs.blohg.org>`_,
you should add the following content to your ``.hgignore`` file, if it wasn't
added yet by the default blohg template::

    ^build/

This will prevent your blohg repository of include the build files by mistake.


Creating a Makefile to automate the deployment
----------------------------------------------

Now create a ``Makefile`` file at the root of your blohg repository, with the
following content (make sure to change ``blohg`` to your username):

.. sourcecode:: make

    .PHONY: push

    USERNAME=blohg
    REPO=$(USERNAME).bitbucket.org

    push:
    	blohg freeze
    	hg clone ssh://hg@bitbucket.org/$(USERNAME)/$(REPO)/ /tmp/$(REPO)
    	cp -vr build/* /tmp/$(REPO)/
    	hg commit -Am "blohg update: $(shell date)" -R /tmp/$(REPO)
    	hg push -R /tmp/$(REPO)
    	rm -rf /tmp/$(REPO)

This ``Makefile`` isn't optimal, as it will clone/delete a local copy of the
repository each time you deploy your blog, but I think that you got the idea
and can improve it by yourself. :)


Commiting the Makefile to your blohg repository
-----------------------------------------------

You can add this ``Makefile`` to your blohg repository, to make the deployments
easier everywhere::

    $ hg commit -Am 'Added Makefile'


Publishing the blog
-------------------

If everything is ok you should be able to publish your blog running the
following command::

    $ make push

If you was already using the repository, you may get some conflicts. You'll
need to fix them by yourself, like you usually do for your software projects
versioned with Mercurial_. :)

You should run this command each time you publish a new post, change some
configuration parameter, etc. Make sure to run it after commit the changes
to the blohg repository.

That's it, have fun!
