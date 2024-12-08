import numpy as np

class TicTacToe:
    def __init__(self):
        self.board=np.zeros((3,3),dtype=int)
        self.player=1 
    
    def display_board(self):
        symbols={0:'',1:"X",-1:"O"}
        for row in self.board:
            print("|".join(symbols[cell] for cell in row))
            print("-"*5)
    def make_move(self, row, col):
        if self.board[row, col] != 0:
            print("Attempting to make move at:", row, col)
            print("Board state when the error occurred:")
            print(self.board)
            raise ValueError('Invalid move!')
        self.board[row, col] = self.player
        print(f"Player {self.player} placed at {row}, {col}")
        self.player *= -1
        print("Updated board state:")
        print(self.board)

    
    def check_winner(self):
            for i in range(3):
                if abs(self.board[i].sum()) == 3 or abs(self.board[:, i].sum()) == 3:
                    return self.board[i, 0] or self.board[0, i]
            if abs(self.board.trace()) == 3 or abs(np.fliplr(self.board).trace()) == 3:
                return self.board[1, 1]
            if not np.any(self.board == 0):
                return 0  # Draw
            return None  # Game ongoing
