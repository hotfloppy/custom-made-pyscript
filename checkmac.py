#!/usr/bin/env python

'''
Check Hardware Manufacturer

Usage:
    checkmac.py (MAC_ADDR)
    checkmac.py (-h | --help)
    checkmac.py (-v | --version)

Arguments:
    MAC_ADDR        MAC address that we wanted to check. ie: B0:5A:DA:5A:65:22

Options:
    -h --help       Show this screen
    -v --version    Show version
'''

from docopt import docopt
from colorama import Fore, Style
from pycurl import Curl
from cStringIO import StringIO


if __name__ == '__main__':
    # assign arguments from docopt into $args
    args = docopt(__doc__, version='FIXME')

    # assign MAC_ADDR value into $macaddress
    macaddress = (args['MAC_ADDR'])

    url = "https://api.macvendors.com/{}".format(macaddress)
    vendor = StringIO()

    # c = pycurl.Curl()
    c = Curl()
    c.setopt(c.URL, url)                        # set URL
    c.setopt(c.WRITEFUNCTION, vendor.write)     # store output in $vendor
    c.perform()
    c.close()

    print Style.BRIGHT + "MAC Address" + Fore.GREEN + " : {}".format(macaddress.upper()) + Style.RESET_ALL
    print Style.BRIGHT + "Vendor     " + Fore.GREEN + " : {}".format(vendor.getvalue()) + Style.RESET_ALL
