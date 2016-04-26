import termios, sys, os

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
    
#My version for CEC command sending... based on version in test1.py
def buildCmd(key):
    
    #Define nav commands
    keylist = { '\x1b[A':'04:44:01',  #up
                '\x1b[B':'04:44:02', #down
                '\x1b[C':'04:44:04', #right
                '\x1b[D':'04:44:03', #left
                '\n':'04:44:00', #Select/Enter/OK
                'q':'04:44:4c', #Skip back
                'w':'04:44:48', #RWD
                'e':'04:41:24', #Play
                'r':'04:41:25', #Pause
                't':'04:42:03', #Stop
                'y':'04:44:49', #FFWD
                'u':'04:44:4b' #Skip forward
                }
 
    if key in keylist:
        cmd = 'echo "tx ' + keylist[key] + '" | cec-client -s -d 1'
        return cmd
    else:
        return "Unknown command" + key + '\n'


try:
    while 1:
        try:
            os.system(buildCmd(getkey()))
                        
        except IOError: pass
finally:
    print "Finished"
