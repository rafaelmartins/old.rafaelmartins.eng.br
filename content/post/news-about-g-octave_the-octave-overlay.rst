g-octave news: the octave overlay
=================================

.. tags: en-us,gentoo

After having lots of problems with people that can't use g-octave properly,
sometimes because they don't seems to be able to read documentation, elog
messages and/or just ask, and after a suggestion of Sebastien Fabbro
(bicatali), I write down some simple scripts to update the
`g-octave package database <https://github.com/rafaelmartins/g-octave-db>`_
and an `overlay <https://github.com/rafaelmartins/octave-overlay>`_ using
g-octave and a cronjob.

I built a virtual machine on my own server and set up a weekly cronjob, that
will hopefully keep the packages up-to-date.

The overlay is available on Github:

https://github.com/rafaelmartins/octave-overlay

To install it, follow the instrunctions available on the README file. The
overlay is available on ``layman``, named ``octave``.

Packages with unresolvable dependencies, e.g. packages with dependencies
unavailable on gentoo-x86, aren't available in the overlay. If you find
some package that is supposed to work and isn't available on the overlay
please open an issue on Github, and I'll take a look ASAP.

As a bonus, g-octave code itself was moved to Github:

https://github.com/rafaelmartins/g-octave

Feel free to submit pull requests if you think that something is broken and
you know how to fix it.

And as another bonus, the g-octave website (http://g-octave.org/) is now
running on the `Read the Docs <http://readthedocs.org/>`_ service, that is
way more reliable than my own server. This should avoid the recent
documentation downtimes.
