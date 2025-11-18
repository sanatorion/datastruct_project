def reset():
        print('\033[H')

def clearLine(moveup):
    
    if moveup:
        print('\033[F', end = '')
    print('\033[2K', end = '')
    pass

def savepos():
    print('\033[s', end = '')
    
def restorepos():
    print('\033[u', end = '')

def moveUp(n):
    pass
def moveDown(n):
    pass
def moveLeft(n):
    pass
def moveRight(n):
    pass

def moveto(row, col):
    pass