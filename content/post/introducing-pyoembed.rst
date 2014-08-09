Introducing pyoembed
====================

.. tags: en-us, pyoembed, oembed, python, gentoo

.. _oEmbed: http://oembed.com/
.. _Python: http://code.google.com/p/python-oembed/
.. _libraries: http://pyembed.github.io/

.. pull-quote::

   **Warning**: This is a (very) delayed announcement! ;-)

oEmbed_ is an open standard for embedded content. It allows users to embed some
resource, like a picture or a video, in a web page using only the resource URL,
without knowing the details of how to embed the resource in a web page.

oEmbed_ isn't new stuff. It was created around 2008, and despite not being
widely supported by content providers, it is supported by some big players,
like YouTube, Vimeo, Flickr and Instagram, making its usage highly viable.

To support the oEmbed_ standard, the content provider just needs to provide a
simple API endpoint, that receives an URL and a few other parameters, like the
maximum allowed height/width, and returns a JSON or XML object, with ready-to-use
embeddable code.

The content provider API endpoint can be previously known by the oEmbed client,
or auto-discovered using some meta tags added to the resource's HTML page. This is
the point where the standard isn't precise enough: not all of the providers support
auto-discovering of the API endpoint, neither all of the providers are properly
listed on the oEmbed_ specification. Proper oEmbed_ clients should try both
approaches, looking for known providers first, falling back to auto-discovered
endpoints, if possible.

Each of the Python_ libraries_ for oEmbed_ decided to follow one of the mentioned
approaches, without caring about the other one, failing to support relevant
providers. And this is the reason why I decided to start writing pyoembed!

.. read_more

pyoembed is a simple and easy to use implementation of the oEmbed_ standard for
Python, that supports both auto-discovered and explicitly defined providers,
supporting most (if not all) the relevant providers.

pyoembed's architecture makes it easy to add new providers and supports most of
the existing providers out of the box.

To install it, just type::

    $ pip install pyoembed

Gentoo users can install it from ``gentoo-x86``::

    # emerge -av pyoembed

pyoembed is developed and managed using Github, the repository is publicly
available:

https://github.com/rafaelmartins/pyoembed

A Jenkins instance runs the unit tests and the integration tests automatically,
you can check the results here:

https://ci.rgm.io/view/pyoembed/

The integration tests are supposed to fail from time to time, because they rely
on external urls, that may be unavailable while the tests are running.

pyoembed is released under a 3 clause BSD license.

Enjoy!
