from termcolor import colored
from time import sleep
from os import system


def display(b):
    """Display board"""
    for y in b:
        for x in y:
            print(x, end=' ')
        print()
    
def check_finish(b, floor_ch):
    """Check board fill"""

    for y in b:
        for x in y:
            if x == floor_ch:
                return False
    return True

def pool_table(y_size, x_size, floor_ch, *navigators, effect=False, current_co=None, previous_co=None, delay=0):
    """
    Simulating the impact of one (or more) billiard balls on a billiard table 

    y_size: Width -> width board

    x_size: Length -> lenght board

    floor_ch: Floor character -> ground floor character

    *navigators: Navigators information in tuple format -> included: (charcter_navigator, y_position, x_position, y_direction, x_direction)
        y_position, x_position: Initial location
        y_direction, x_derection: Initial movement direction -> default: 1, 1

    effect: Remaining navigator effect after passing a point -> defalut: False
    
    current_co: Current color -> main navigator color
    
    previous_co: Previous color -> color remains the effect
    
    delay: Board update delay -> default: 0 (s)
    
    """
    

    # Color Init
    system("")
    

    ch_navigator = {}
    po_navigator = {}
    dir_navigator = {}

    # Navigators status analysis
    for ind, navigator in enumerate(navigators):

        if len(navigator) == 3:
            ch_navigator[ind] = navigator[0]
            po_navigator[ind] = (navigator[1], navigator[2])
            dir_navigator[ind] = (1, 1)
        else:
            ch_navigator[ind] = navigator[0]
            po_navigator[ind] = (navigator[1], navigator[2])
            dir_navigator[ind] = (navigator[3], navigator[4])
    

    # Make board
    board = [[floor_ch for _ in range(x_size)] for _ in range(y_size)]

    # Display evolution
    while True:

        system('cls')

        # Placement of navigators
        if effect:
            for i in range(len(navigators)):
                y, x = po_navigator[i]
                board[y][x] = colored(ch_navigator[i], current_co)
        else:
            for i in range(len(navigators)):
                y, x = po_navigator[i]
                board[y][x] = ch_navigator[i]
        
        # Display board
        display(board)

        # Reset page based on effect
        if effect:
            for i in range(len(navigators)):
                y, x = po_navigator[i]
                board[y][x] = colored(ch_navigator[i], previous_co)
        else:
            for i in range(len(navigators)):
                y, x = po_navigator[i]
                board[y][x] = floor_ch
        
        
        # Control collision with walls
        for i in range(len(navigators)):
            y, x = po_navigator[i]
            dy, dx = dir_navigator[i]

            if y == 0:
                dy = 1
            
            if y == y_size - 1:
                dy = - 1
            
            if x == 0:
                dx = 1
            
            if x == x_size - 1:
                dx = -1
            
            dir_navigator[i] = (dy, dx)
        
        # Make the next move
        for i in range(len(navigators)):
            y, x = po_navigator[i]
            dy, dx = dir_navigator[i]
            
            po_navigator[i] = (y+dy, x+dx)
        
        if check_finish(board, floor_ch):
            break

        sleep(delay)


if __name__ == '__main__':

    y_size = 20
    x_size = 30
    floor_ch = ' '

    pool_table(y_size, x_size, floor_ch, ('0', 0, 0), effect=True, current_co='yellow', previous_co='blue', delay=0.01)

    # or
    #pool_table(y_size, x_size, floor_ch, ('0', 0, 0), ('1', 0, 29, -1, -1), delay=0.01)

    # or
    #pool_table(y_size, x_size, floor_ch, ('0', 0, 0), ('1', 0, 29), effect=True, current_co='yellow', previous_co='blue', delay=0.01)