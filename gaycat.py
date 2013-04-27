#!/usr/bin/env python3

import sys

ansiterm = {
    'red':      '\033[0;31',
    'orange':   '\033[0;33',
    'yellow':   '\033[1;33',
    'green':    '\033[0;32',
    'blue':     '\033[0;34',
    'indigo':   '\033[1;35',
    'violet':   '\033[0;35',
    'normal':   '\0330;'
}

""" Print character 'c' in a given color. """
def gayputc(char, color):
    sys.stdout.write("%sm" % color)
    sys.stdout.write(char)
    sys.stdout.write("%sm" % ansiterm['normal'])

if __name__ == '__main__':
    ordered_clist = (
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'indigo',
        'violet'
    )


quote = "Programming is hard.  Let's go rollerblading!"
