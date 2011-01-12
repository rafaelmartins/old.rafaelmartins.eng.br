fwinstall
=========

fwinstall is a Python script to install Frugalware Linux without an
installation media. The script will download and/or generate all the
needed files.

source: http://hg.rafaelmartins.eng.br/scripts/file/tip/python/fwinstall.py

Preparating file systems
------------------------

You need to format the partitions to receive the system manually.

The examples assume */mnt/frugalware* as the directory where you
have mounted */* partition.


Example: */* + swap
~~~~~~~~~~~~~~~~~~~

::

    /       ext3    /dev/sda1
    swap    swap    /dev/sda2

* Formatting partitions: ::

    # mkfs.ext3     /dev/sda1
    # mkswap        /dev/sda2

* Mounting file systems: ::

    # mount /dev/sda1 /mnt/frugalware
    # swapon /dev/sda2


Example: */* + */boot* + */home* + swap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    /boot   ext2    /dev/sda1
    /       ext3    /dev/sda2
    /home   ext3    /dev/sda3
    swap    swap    /dev/sda4

* Formatting partitions: ::

    # mkfs.ext2     /dev/sda1
    # mkfs.ext3     /dev/sda2
    # mkfs.ext3     /dev/sda3
    # mkswap        /dev/sda4

* Mounting file systems: ::

    # mount /dev/sda2 /mnt/frugalware
    # mkdir /mnt/frugalware/{boot,home}
    # mount /dev/sda1 /mnt/frugalware/boot
    # mount /dev/sda3 /mnt/frugalware/home
    # swapon /dev/sda4


Downloading the script
----------------------

::

    # wget http://hg.rafaelmartins.eng.br/scripts/raw-file/tip/python/fwinstall.py
    # chmod +x fwinstall.py


Running the script
------------------

You have to pass the */* mount point to the script as an argument
(e.g. */mnt/frugalware*). ::

    # ./fwinstall.py /mnt/frugalware

This command will install the packages from the -stable repository.
If you want the packages from the -current repository you should
use: ::

    # ./fwinstall.py --current /mnt/frugalware

The script depends on Python 2.6 (maybe works with Python >= 3).

At this point you already have the system installed on your hard disk. :)


Entering chroot
---------------

::

    # mount -t proc none /mnt/frugalware/proc
    # mount -t sysfs none /mnt/frugalware/sys
    # mount -o bind /dev /mnt/frugalware/dev

    # cp /etc/resolv.conf /mnt/frugalware/etc/
    # grep -v rootfs /proc/mounts > /mnt/frugalware/etc/mtab
    # chroot /mnt/frugalware /bin/bash

At this point you are inside your new system, without any configuration.


Configuring */etc/fstab*
------------------------

The file */etc/fstab* is responsible for telling the kernel which
directories to mount the partitions of the hard disk.

Unlike the traditional process of installation, configuration must be
done manually.

Nano and VIM are available.

For the previous examples */etc/fstab* would be: ::

    none            /proc           proc    defaults                0   0
    none            /sys            sysfs   defaults                0   0
    devpts          /dev/pts        devpts  gid=5,mode=628          0   0
    usbfs           /proc/bus/usb   usbfs   devgid=23,devmode=664   0   0
    tmpfs           /dev/shm        tmpfs   defaults                0   0
    
    # Your partitions
    /dev/sda1       /               ext3    noatime                 0   1
    /dev/sda2       none            swap    sw                      0   0

and ::

    none            /proc           proc    defaults                0   0
    none            /sys            sysfs   defaults                0   0
    devpts          /dev/pts        devpts  gid=5,mode=628          0   0
    usbfs           /proc/bus/usb   usbfs   devgid=23,devmode=664   0   0
    tmpfs           /dev/shm        tmpfs   defaults                0   0
    
    # Your partitions
    /dev/sda1       /boot           ext2    noauto,noatime          1   2
    /dev/sda2       /               ext3    noatime                 0   1
    /dev/sda3       /home           ext3    noatime                 0   1
    /dev/sda4       none            swap    sw                      0   0

respectively.

Configure this file according to your partition scheme.


Configuring */etc/sysconfig/keymap*
-----------------------------------

This file configures your keymap.

To know his keymap, look in */usr/share/keymaps*


Example
~~~~~~~

For Brazilian Portuguese keymap (ABNT2), the keymap file is: ::

    /usr/share/keymaps/i386/qwerty/br-abnt2.map.gz

then the contents of the file would be: ::

    keymap=br-abnt2


Configuring */etc/profile.d/lang.sh*
------------------------------------

This file configures your system locales and charset.
	
For a list of locales supported, type: ::

    # locale -a

Select your locale and edit the file.


Configuring your timezone
-------------------------

Use the *timeconfig* tool to configure your timezone.


Grub
----

Configuring Grub
~~~~~~~~~~~~~~~~

Grub is our bootloader. You need edit */boot/grub/menu.lst* to Grub
found your kernel.

If you already have grub installed, configure it as you like.

If you do not have, you need configure it and install it.

For the previous examples */boot/grub/menu.lst* would be something
like: ::

    default=0
    timeout=5
    gfxmenu (hd0,0)/boot/grub/message

    title <release>
        kernel (hd0,0)/boot/vmlinuz root=/dev/sda1 ro quiet vga=<FRAMEBUFFER>

and ::

    default=0
    timeout=5
    gfxmenu (hd0,0)/boot/grub/message
    
    title <release>
        kernel (hd0,0)/boot/vmlinuz root=/dev/sda2 ro quiet vga=<FRAMEBUFFER>

respectively.

<release> will be the current Frugalware release.

<FRAMEBUFFER> will be your framebuffer resolution setting.

*Important:* The configuration of Grub can be highly complex. We highly
recommend the reading of its documentation to configure it.


Installing Grub
~~~~~~~~~~~~~~~

To install grub, assuming that your disk is represented by */dev/sda*,
type: ::

    # grub-install /dev/sda


grubconfig
~~~~~~~~~~

Instead of configuring and installing Grub manually you can try run
grubconfig, from *frugalwareutils* package.

We found some issues with this program when running in a chroot environment,
so the method is not indicated.

We will work on that.


Finishing installation
----------------------

Your Frugalware Linux is installed.

You can take the additional settings using the software in the package
*frugalwareutils*.

To see what packages are installed, type: ::

    # pacman-g2 -Q

To exit the chroot environment type: ::

    # exit
    # umount /mnt/frugalware/proc
    # umount /mnt/frugalware/sys
    # umount /mnt/frugalware/dev

Additionally you should umount your partitions.

*IMPORTANT:* This documentation is heavily based on examples, have that
in mind, and above all, know your hardware :)


.. date added automatically by the script blohg_dump.py.
   this file was exported from an old repository, and this comment will
   help me to forcing the old creation date, instead of the date of the
   first commit on the new repository.

.. date: 1273363567

