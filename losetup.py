#!/usr/bin/env python

import shlex
from subprocess import check_output

__VERSION__="0.1"


""" Gets a free loop device at dev to mount the file and pass it to the luks.
" @return the path of the loop device or none if there is no loop devices
" valiable.
"""
def get_free_loop_device():
    losetupf_args = shlex.split("losetup -f")
    losetupf_output = check_output(losetupf_args)
   
    return losetupf_output


