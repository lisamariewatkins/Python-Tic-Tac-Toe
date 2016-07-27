#Python tic-tac-toe game, for project 1 of Udemy's complete python bootcamp
import random

def displayBoard(board):
    print board[1], ' | ',board[2], ' | ',board[3]
    print '-------------'
    print board[4], ' | ',board[5],' | ',board[6]
    print '-------------'
    print board[7],' | ',board[8],' | ',board[9]

def inputLetter(): #lets player type in what letter they'd like to be
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = raw_input("Player 1, do you want to be X or O?").upper()
    if letter == "X":
        return ("X", "O")
    else:
        return ("O", "X")

def first():
    if random.randint(0,1) == 0:
        return "Player 1"
    else:
        return "Player 2"

def playAgain():
    return raw_input("Do you want to play again?").lower().startswith("y")

def move(board, letter, position):
    board[position] = letter

def whoWon(board, letter):
    return (board[0] == board[1] == board [2] == letter or 
       board[3] == board[4] == board [5] == letter or 
       board[6] == board[7] == board [8] == letter or 
       board[0] == board[3] == board [6] == letter or 
       board[1] == board[4] == board [7] == letter or 
       board[2] == board[5] == board [8] == letter or 
       board[0] == board[4] == board [8] == letter or 
       board[2] == board[4] == board [6] == letter) 

def spaceCheck(board, position):
    return board[position] == " "

def fullBoard(board):
    for i in range(1,10):
        if spaceCheck(board,i):
            return False
    return True

def chooseSpace(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not spaceCheck(board,int(position)):
        position = raw_input("Choose your next position: (1-9)")
    return int(position)

def replay():
	return raw_input("Do you want to play again? Enter Yes or No: ").lower().startswith('y')

print("Welcome to Tic-Tac-Toe")

while True:
    board = [' '] * 10
    player1Marker, player2Marker = inputLetter()
    turn = first()
    print(turn + " goes first")
    gameOn = True

    while gameOn:
        if turn == "Player 1":
            displayBoard(board)
            position = chooseSpace(board)
            move(board, player1Marker, position)

            if whoWon(board, player1Marker):
                displayBoard(board)
                print("Congratulations player 1")
                gameOn = False
            else:
                if fullBoard(board):
                    displayBoard(board)
                    print("the game is a draw")
                    break
                else:
                    turn = "Player 2"
        else:
            displayBoard(board)
            position = chooseSpace(board)
            move(board, player2Marker, position)

            if whoWon(board, player2Marker):
                displayBoard(board)
                print("Congratulations player 2")
                gameOn = False
            else:
                if fullBoard(board):
                    displayBoard(board)
                    print("the game is a draw")
                    break
                else:
                    turn = "Player 1"
    if not playAgain():
        break

