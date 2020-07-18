"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0

    for row in board:
        for value in row:
            if value:
                count += 1
    
    if count % 2 == 0:
        return 'X'
    else:
        return 'O'



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                possible_actions.add((i, j))
    
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    temp = copy.deepcopy(board)

    if temp[action[0]][action[1]]:
        raise Exception
    
    temp[action[0]][action[1]] = player(temp)
    return temp


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # check rows
        if(board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0]):
            return board[i][0]
        # check columns
        if(board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i]):
            return board[0][i]

    # check diagonals
    if(board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0]):
        return board[0][0]
    if(board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2]):
        return board[0][2]
    

    return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    tie = True
    for row in board:
        for cell in row:
            if not cell:
                tie = False

    if winner(board) or tie:
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    player = winner(board)
    if player == 'X':
        return 1
    if player == 'O':
        return -1
    return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if player(board) == "X":
        v = float("-inf")
        for action in actions(board):
            value = min_value(result(board,action), float("-inf"), float("inf"))
            if value > v:
                v = value
                move = action
    else:
        v = float("inf")
        for action in actions(board):
            value = max_value(result(board,action), float("-inf"), float("inf"))
            if value < v:
                v = value
                move = action
        
    return move

def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = float("-inf")

    for action in actions(board):
        v = max(v, min_value(result(board,action), alpha, beta))
        alpha = max(alpha, v)
        if alpha >= beta:
            break
    return v

def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = float("inf")

    for action in actions(board):
        v = min(v, max_value(result(board,action), alpha, beta))
        beta = min(beta, v)
        if alpha >= beta:
            break
    return v
    