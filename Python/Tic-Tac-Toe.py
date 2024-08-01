'''
### Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:
    Players take turns placing characters into empty squares ' '.
    The first player A always places 'X' characters, while the second player B always places 'O' characters.
    'X' and 'O' characters are always placed into empty squares, never on filled ones.
    The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
    The game also ends if all squares are non-empty.
    No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".
'''

import numpy as np

def tictactoe(moves):
    board = np.zeros([3,3])
    i = 0
         
    for move in moves:
        if i == 0:
            board[move[0], move[1]] = 1
            i = 1
                
        else:
            board[move[0], move[1]] = -1
            i = 0

    S1 = np.sum(board, axis=0)
    S2 = np.sum(board, axis=1)
    S3 = np.sum(np.diagonal(board))
    S4 = np.array(board[0, 2] + board[1, 1] + board[2, 0])


    if np.any(S1 == 3) or np.any(S2 == 3) or S3 == 3 or S4 == 3:
        return 'A'
    if np.any(S1 == -3) or np.any(S2 == -3) or S3 == -3 or S4 == -3:
        return 'B'
    elif len(moves) < 9:
        return 'Pending'
    else:
        return 'Draw'




###### Test case

M = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
result = tictactoe(M)
print ( 'The result of game is :')
print(result)











        
