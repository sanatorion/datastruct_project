import time, cursor, msvcrt

delayperchar = 0.03
delayperline = 0.02
def readbuffer():
    while msvcrt.kbhit():
        c = msvcrt.getch()

def printPerLine(*messages):
    for message in messages:
        print(message)
        time.sleep(delayperline)
        
def printPerChar(message, pressToContinue, delay, allowSkip, printnewline):
    readbuffer()
    for char in message:
        if msvcrt.kbhit():
            c = msvcrt.getch()
            
            if allowSkip:
                print("\r" + message)
                return

        print(char, end='')
        time.sleep(delayperchar)
    
    time.sleep(delay)
    
    if pressToContinue:
        input()
    elif printnewline:
        print()