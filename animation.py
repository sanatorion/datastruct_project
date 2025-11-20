import time, msvcrt, pygame

pygame.init()
pygame.mixer.init()

delayperchar = 0.03
delayperline = 0.02

def readbuffer():
    while msvcrt.kbhit():
        c = msvcrt.getch()

def printPerLine(enablesfx, delay, *messages):
    delay = delayperline if delay == 0 else delay
    for message in messages:
        if enablesfx: sfx = pygame.mixer.Sound("sounds/perrest.mp3"); sfx.set_volume(0.5); sfx.play()
        print(message)
        time.sleep(delay)
        
def printPerChar(message, pressToContinue, delay, allowSkip, printnewline):
    readbuffer()
    
    for char in message:
        if msvcrt.kbhit():
            c = msvcrt.getch()
            
            if allowSkip:
                print("\r" + message)
                return
        
        print(char, end='', flush=True)
        sfx = pygame.mixer.Sound("sounds/textbeep.mp3")
        sfx.set_volume(0.5)
        sfx.play()
        time.sleep(delayperchar)
    
    time.sleep(delay)
    
    if pressToContinue:
        input()
    elif printnewline:
        print()

def savepos():
    print('\033[s', end = '')
    
def restorepos():
    print('\033[u', end = '')

def clearLine(moveup):
    if moveup:
        print('\033[F', end = '')
    print('\033[2K', end = '')