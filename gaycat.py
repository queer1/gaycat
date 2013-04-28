#!/usr/bin/env python3
# (c) 2013 D**kSoft

import sys, time

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

ordered_clist = (
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'indigo',
    'violet'
)

""" Print character 'c' in a given color. """
def gayputc(char, color):
    sys.stdout.write("%sm" % color)
    sys.stdout.write(char)
    sys.stdout.write("%sm" % ansiterm['normal'])
    sys.stdout.flush()

def gaytest():
    gayputs('Programming is hard.  Let\'s go rollerblading!')

def gayputs(s):
    for c in range(len(s)):
        gayputc(s[c], ansiterm[ordered_clist[c % len(ordered_clist)]])
        sys.stdout.write('%sm' % ansiterm['normal'])
        sys.stdout.flush()

def gayversion():
    pass

def gayhelp():
    pass

def infinigay():
    pad = 0
    inc = 1
    while(True):
        sys.stdout.write(' '*pad)
        gayputs('###'*len(ordered_clist))
        print()
        time.sleep(0.2)
        if pad >= 10:
            inc = -1
        elif pad < 0:
            inc = 1
        pad += inc
    

def manhandle():
    gayputs('I don\'t know what to do with that.')

if __name__ == '__main__':

    if len(sys.argv) > 1 and sys.argv[1][0] == '-':
        {
            '-t': gaytest,
            '-v': gayversion,
            '-h': gayhelp,
            '-i': infinigay
        }.get(sys.argv[1], manhandle)()

    elif len(sys.argv) > 1 and sys.argv[1][0] != '-':
        pass
    else:
        for line in sys.stdin:
            gayputs(line)
