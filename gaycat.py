#!/usr/bin/env python3
# (c) 2013 Dicksoft

import sys

ansiterm = {
    'red':      '\033[0;31',
    'orange':   '\033[0;33',
    'yellow':   '\033[1;33',
    'green':    '\033[0;32',
    'blue':     '\033[0;34',
    'indigo':   '\033[1;35',
    'violet':   '\033[0;35',
    'normal':   '\033[0;'
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

    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        quote = "Programming is hard.  Let's go rollerblading!"
        
        for c in range(len(quote)):
            gayputc(quote[c], ansiterm[ordered_clist[c % len(ordered_clist)]])
        print()
    else:
        for line in sys.stdin:
            c = 0
            for ch in line:
                gayputc(line[c], ansiterm[ordered_clist[c % len(ordered_clist)]])
                c += 1
