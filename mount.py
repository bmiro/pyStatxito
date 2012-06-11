#!/usr/bin/env python

import shlex
from md5 import md5
from subprocess import check_output, Popen, PIPE


from losetup import get_free_loop_device
from cryptsetup import luksOpen, luksClose


__VERSION__="0.1"


""" Generates a name to identify the volume that will be mounted  """
def generate_cryptname(filepath):
    return filepath.split("/")[-1].replace(" ","_")


""" Mounts the given device to the mount point """
def mount(dev, mountpath):
    mount_args = shlex.split("mount %s %s" % (dev, mountpath))
    mount = Popen(mount_args)
    mount.wait()


""" Umounts the volume, specifying the device or the mountpoint """
def unmount(dev=None, mountpoint=None):
    if dev:
        umount_args = shlex.split("umount " + dev)
    else:
        umount_args = shlex.split("umount " + mountpoint)

    umount = Popen(umount_args)
    umount.wait()
    

""" Mounts the given file to the given mount point using the passkey
" or the keyfile, depending on which is given.
" @return a tupla with the name at the cryptab and the used loop device.
" i.e. (secret_crypted.file, /dev/loop2)
"""
def mount_crypted_file(crypted_file, mountpoint, passkey=None, keyfile=None):
   
    loopdev = get_free_loop_device()

    if not loopdev:
        print "There is no loop devices avaliable" 

    cryptname = generate_cryptname(crypted_file)

    luks_open(loopdev, cryptname, passkey, keyfile)

    return (cryptname, loopdev)
    

""" Umounts the crypted volume identified by cryptname """
def umount_crypted_file(cryptname):
    umount_device 


""" Mounts a crypted "thing" a device of volume to the given
" mount point using the passkey or keyfile, depending on which
" is given
" @return a tupla with the name at the cryptab and the used loop device.
" i.e. (secret_crypted.file, /dev/loop2)
"""
def mount_crypted(crypted_vol, mountpoint, passkey=None, keyfile=None):
    pass
    

""" Umounts the crypted "thing" a device of volume to the given
" mount point using the passkey or keyfile, depending on which
"""
def umount_crypted():
    pass


if __name__=='__main__':
    print "hola"
    print "asdsad"



