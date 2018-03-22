#!/usr/bin/env python

import os
import socket
from colorama import Style


def check_access():
    if os.geteuid() != 0:
        print "Administrator access privileges required."
        exit(99)


def list2string(list):
    string = "%s" % ' '.join(map(str, list))
    return string


def above_line(length=30):
    line = length * "=" + "\n"
    return line


def below_line(length=30):
    line = "\n" + length * "="
    return line


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("9.9.9.9", 80))
    return s.getsockname()[0]


if __name__ == '__main__':
    print Style.BRIGHT + "Compilation of function created by Naim" + Style.RESET_ALL
