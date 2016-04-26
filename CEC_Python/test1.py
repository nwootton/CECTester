import termios, fcntl, sys, os

def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
    new[6][termios.VMIN] = 1
    new[6][termios.VTIME] = 0
    termios.tcsetattr(fd, termios.TCSANOW, new)
    key = None
    try:
        key = os.read(fd, 4)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, old)
    return key

# Use this list to find the key that we want.  This is hard coded for xterm.
def chkkey(key):
    keylist = { '\x1b':'escape', '\x7f':'backspace', '\x1bOH':'HOME',
                 '\x1bOP':'F1',  '\x1bOQ':'F2',   '\x1bOR':'F3',  '\x1bOS':'F4',
                 '\x1b[15':'F5', '\x1b[17':'F6',  '\x1b[18':'F7', '\x1b[19':'F8',
                 '\x1b[20':'F9', '\x1b[21':'F10', '\x1b[23':'F11',
                 '\x1b[24':'F12',
                 '\x1b[A':'ARROW_UP', '\x1b[B':'ARROW_DN',
                 '\x1b[C':'ARROW_RT', '\x1b[D':'ARROW_LT',
                 '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7',
                 '8':'8', '9':'9', '0':'0' }
 
    if key in keylist:
        return keylist[key]
    else:
        return "Unknown"

try:
    while 1:
        try:
            c = chkkey(getkey())
            print "Got character", repr(c)
                       
        except IOError: pass
finally:
    print "Finished"
