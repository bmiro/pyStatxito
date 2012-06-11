#!/usr/bin/env python

import shlex
from subprocess import Popen

__VERSION__="0.1"


""" Open the luks device identified by the cryptname at the device (can be a loop
" one) using the passkey or keyfile depending on which is given
"""
def luks_open(device, cryptname, passkey=None, keyfile=None):
    luksOpen_cmd = "cryptsetup luksOpen %s %s" % (device, cryptname)

    if keyfile:
        # Use passfile
        luksOpen_cmd += "--key-file " + keyfile

    luksOpen_args = shlex.split(luksOpen_cmd)    
    luksOpen = Popen(luksOpen_args) 

    if keyfile:
        luksOpen.communicate(passkey)

    luksOpen.wait()


""" Closes the crypted volume identified by cryptname """
def luks_close(cryptname):
    luksClose_args = shlex.split("cryptsetup luksClose %s" + cryptname)
    luksClose = Popen(luksClose_args)   
    luksClose.wait()
    

