import numpy as np
import tensorflow as tf
from game import TicTacToe

def generate_data(num_games=10000):
    X, y = [], []
    for _ in range(num_games):
        game = TicTacToe()
        board_states = []
        moves = []
        while game.check_winner() is None:
            board_states.append(game.board.copy())
            move = np.random.choice(np.where(game.board.flatten() == 0)[0])  # Random move
            row, col = divmod(move, 3)
            moves.append((row, col))
            game.make_move(row, col)

        winner = game.check_winner()

        # Assign rewards based on the winner
        for state, move in zip(board_states, moves):
            reward = np.zeros(9)  # 9 cells in the board
            if winner == 1:  # Player wins
                reward[move[0] * 3 + move[1]] = 1
            elif winner == -1:  # AI wins
                reward[move[0] * 3 + move[1]] = -1
            X.append(state)
            y.append(reward)

    return np.array(X), np.array(y)
