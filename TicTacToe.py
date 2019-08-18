
import sys
import random
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print (' {0:1} | {1:1} | {2:1} '.format(board[7],board[8],board[9]))
    print ('---+---+---')
    print (' {0:1} | {1:1} | {2:1} '.format(board[4],board[5],board[6]))
    print ('---+---+---')
    print (' {0:1} | {1:1} | {2:1} '.format(board[1],board[2],board[3]))
    pass

# lets Player 1 choose O or X and assigns Player 2 the other
def player_welcome():
    players = []
    for num in range(2): # 0,1
        name = input(f'Player {num+1} what is your name?')
        players.append({'name':name})

    if random.randint(0,1):
        players[0]['sym'] = 'X'
        players[1]['sym'] = 'O'
    else:
        players[0]['sym'] = 'O'
        players[1]['sym'] = 'X'

    print('%s you are %s' %(players[0]['name'], players[0]['sym']))
    print('%s you are %s' %(players[1]['name'], players[1]['sym']))

    return players

def place_marker(board, marker, position):
    board[position] = marker
    return board

def win_check(board, mark):
    wins = []
    wins.extend([[1,2,3],[4,5,6],[7,8,9]]) # rows
    wins.extend([[1,4,7],[2,5,8],[3,6,9]]) # cols
    wins.extend([[1,5,9],[3,5,7]]) # diagonals

    for patt in wins:
        if (board[patt[0]] == mark) and (board[patt[1]] == mark) and (board[patt[2]] == mark):
            return True
    else:
        return False


def space_check(board, position):
    return board[position] != 'X' and board[position] != 'O'

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    else:                   # is this syntax going to work?
        return True

# asks player for their move
def player_choice(board):
    while True:
        pos = 0
        while not pos in range (1,10):
            pos = input ('Enter a position from 1 to 9')
            try:
                pos = int(pos)
            except:
                print('Input should be one digit')

        if space_check(board,pos):
            return pos
        else:
            print ('Space not free')
            continue

def replay():
    while True:
        text = input('Play again? (Y/N)')
        if text=='Y':
            return True
        elif text =='N':
            return False
        else:
            print ('Not a recognised answer')

def take_turn(board, plyr):
    display_board(board)
    print ('============')
    print ('%s (%s)' %(plyr['name'], plyr['sym']))
    print ('============')
    position = player_choice(board)
    place_marker(board, plyr['sym'], position)

def game_loop():
    print('Welcome to Tic Tac Toe!')

    while True:
        board = ['','','','','','','','','','',]
        display_board(board)

        players = player_welcome() # both players, in a list
        curr = random.randint(0,1) # one player is a dict
        winner = None

        print('%s you are first'%players[curr]['name'])

        # print(f'{players[curr]['name']} you are first')
        # print(f'{players[curr]['name']} you are {players[curr]['sym']}')


        game_on = True
        while game_on:
            take_turn(board, players[curr])
            if win_check(board, players[curr]['sym']):
                winner = players[curr]
                game_on = False
            elif full_board_check(board):
                print ("Board full")
                game_on = False
            else:
                curr = abs(curr-1) # alternates 0,1,0,1,0,1

        # End of game
        display_board(board)
        if winner:
            print ('Winner was %s' %winner['name'])
        else:
            print ('It was a draw')

        if not replay():
            break

if __name__ == '__main__':
  game_loop()
  sys.exit(0)
