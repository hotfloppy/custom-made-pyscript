#!/usr/bin/env python

'''
APT

Usage:
    apt.py (-u | --update)
    apt.py install PKG...
    apt.py (-h | --help | -v | --version)

Arguments:
    PKG         Package to install

Options:
    -u --update     Update apt repo
    -h --help       Show this screen
    -v --version    Show version
'''

from docopt import docopt
import errno
import subprocess
import hf_function as hf


def get_install(package):
    cmd = '/usr/bin/apt-get install'.split()
    cmd.append(package)

    output_kw = {'stdout': subprocess.PIPE, 'stderr': subprocess.PIPE}
    p = subprocess.Popen(cmd, **output_kw)

    status = p.wait()
    error = p.stderr.read().lower()

    if status and 'permission denied' in error:
        print 'Permission denied running apt-get'
        raise OSError(errno.EACCES, 'Permission denied running apt-get')
    # other conditions here as you require


def update_db():
    '''
    cmd = '/usr/bin/apt-get update'.split()
    output_kw = {'stdout': subprocess.PIPE, 'stderr': subprocess.PIPE}
    proc = subprocess.Popen(cmd, **output_kw)
    status = proc.wait()
    error = proc.stderr.read().lower()

    if 'permission denied' in error:
        raise OSError(errno.EACCES, 'Are you sure you have ther pight priviliges?')
    '''
    print "Access granted."


if __name__ == '__main__':
    args = docopt(__doc__, version='FIXME')
    # get_install(args['<PKG>'])
    print args
    if args['--update']:
        hf.check_access()
        update_db()
    elif args['install']:
        print "Installing {}".format(args['PKG'])
