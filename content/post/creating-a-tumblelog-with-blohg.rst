Creating a tumblelog with blohg
===============================

.. tags: en-us,gentoo

.. pull-quote::

   **Warning**: This post relies on unreleased blohg features. You will need
   to install blohg from the
   `Mercurial repository <http://hg.rafaelmartins.eng.br/blohg>`_ or use the
   live ebuild (=www-apps/blohg-9999), if you are a Gentoo user. Please ignore
   this warning after blohg-1.0 release.

Tumblelogs are `old stuff <http://www.kottke.org/05/10/tumblelogs>`_, but
services like `Tumblr <http://tumblr.com/>`_ popularized them a lot recently.
Thumblelogs are a quick and simple way to share random content with readers.
They can be used to share a link, a photo, a video, a quote, a chat log, etc.

blohg is a good blogging engine, we know, but what about tumblelogs?!

You can already share videos from Youtube and Vimeo, and can share most of the
other stuff manually, but it is boring, and diverges from the main objective of
the tumblelogs: simplicity.

.. read_more

To solve this issue, I developed a `blohg extension
<http://hg.rafaelmartins.eng.br/blogs/rafael.martins.im/file/default/ext/blohg_tumblelog.py>`_
(Yeah, blohg-1.0 supports extensions! ``\o/`` ) that adds some cool
reStructuredText directives:


link
----

This directive is used to share links. It will embed the content of the link to
the post automatically, if the provided link is from a service that supports
the `oEmbed <http://oembed.com/>`_ protocol. If it isn't, and the link is from
a HTML page, it will include the link with the title of the page to the post.
Otherwise it will just include the raw link to the post.

Usage example:

.. sourcecode:: rst

   .. link:: http://www.youtube.com/watch?v=gp30v6XMxBg


quote
-----

This directive is used to share quotes. It will create a ``blockquote`` element
with the quote and add a signature with the author name, if provided.

Usage example:

.. sourcecode:: rst

   .. quote::
      :author: Myself

      This is a random quote!


chat
----

This directive is used to share chat logs. It will add a div with the chat log,
highlighted with `Pygments <http://pygments.org/>`_.

Usage example:

.. sourcecode:: rst

   .. chat::

      [00:56:38] <rafaelmartins> I'm crazy.
      [00:56:48] <rafaelmartins> I chat alone.


----

You can see the directives in action on my shiny new tumblelog:

http://rafael.martins.im/

The source code of the tumblelog, including the blohg extension and the
mobile-friendly templates, is available here:

http://hg.rafaelmartins.eng.br/blogs/rafael.martins.im/

I have no plans to release this extension as part of blohg, but feel free to
use it if you find it useful!

That's all!
