from __future__ import print_function


from IPython.display import clear_output
def display_board(bprint('   |   |'):
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

print "Player 1, would you like to be X's or O'x?"

def player_input():
                  
    marker = ' '
    while not marker == 'O' or marker == 'X'):
        raw_input(Player 1: 'Please choose 'X' or 'O'').upper()

    if marker == 'X':
        return('X', 'O')
    if marker == 'O':
        return('O', 'X')
    
def place_maker(board, marker, position):
    board[position] = marker
        
def win_check(board, player):
    if board[7] == board[8] == board [9] == player or \
       board[4] == board[5] == board [6] == player or \
       board[1] == board[2] == board [3] == player or \
       board[7] == board[4] == board [1] == player or \
       board[8] == board[5] == board [2] == player or \
       board[9] == board[6] == board [3] == player or \
       board[7] == board[5] == board [3] == player or \
       board[9] == board[5] == board [1] == player or \
       return True
    else:
        return False

def full_board(board):
    if " " in board[1:]:
        return False
    else:
        return True

def ask_player(mark):
    






