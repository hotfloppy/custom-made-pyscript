#!/usr/bin/env python

'''
Verify repository using public key (pubkey) from keyserver.ubuntu.com

Usage:
    addkey.py (PUBKEY)...
    addkey.py (-h | --help)
    addkey.py (-v | --version)

Arguments:
    PUBKEY    Public key to be use for verification. (IE: F60F4B3D7AF2AF82)

Options:
    -h --help       Show this screen
    -v --version    Show version
'''

from docopt import docopt
from colorama import Fore, Style
import hf_function as hf
import subprocess


def addkey(keys):
    url = "/usr/bin/apt-key adv --keyserver keyserver.ubuntu.com --recv-keys"
    cmd = url.split()       # split string 'url' into list and put into 'cmd'

    print Style.BRIGHT + Fore.GREEN + "\n" + \
        hf.above_line() + \
        "Adding key(s): {}".format(hf.list2string(keys)) + \
        hf.below_line() + "\n"

    cmd.extend(keys)        # combine list 'cmd' with list 'keys'
    subprocess.call(cmd)    # execute the command

    print Style.RESET_ALL


if __name__ == '__main__':
    args = docopt(__doc__, version="FIXME")
    hf.check_access()

    addkey(args['PUBKEY'])
