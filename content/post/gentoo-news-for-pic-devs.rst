Gentoo: News for PIC developers
===============================

.. tags: en-us,gentoo,electronics,pic

Some weeks ago I decided to restart working with PIC microcontrollers, just for fun,
and bought some electronic components, tools, etc. After having everything in hands,
I started looking at the state of the PIC development tools in Gentoo, and found some
outdated packages. I updated the packages I wanted to use (``dev-embedded/gputils``
and ``dev-embedded/gpsim``; ``dev-embedded/sdcc`` still needs some work), and added
some other packages (``dev-embedded/cpik``, a C compiler for PIC 18F, and re-added
``dev-embedded/pikdev``, a simple graphic IDE for the development of PIC-based
applications, that was previously removed due to the usage of kdelibs3, and now is a
Qt4-only application).

I'll be putting some effort on packaging the MPLAB X IDE and the XC8 compiler in the
next weeks, if permitted by their licenses. I'm not sure yet.

That's all for now.

Thanks.
