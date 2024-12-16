import numpy as np
from game import TicTacToe

def generate_data(num_games=1000):
    X, y = [], []
    for _ in range(num_games):
        game = TicTacToe()
        board_states = []
        moves = []
        while game.check_winner() is None:
            board_states.append(game.board.copy())
            
            # AI's turn to play (Player 1 is the human, Player -1 is the AI)
            if game.player == -1:
                # AI checks for a move to block the player from winning
                move = find_blocking_move(game)
                if move is None:  # If no blocking move is found, pick randomly
                    move = np.random.choice(np.where(game.board.flatten() == 0)[0])
            else:
                # Random move for the player
                move = np.random.choice(np.where(game.board.flatten() == 0)[0])
                
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

    return np.array(X, dtype=np.float32), np.array(y, dtype=np.float32)

def find_blocking_move(game):
    """Find a move to block the opponent from winning."""
    for move in np.where(game.board.flatten() == 0)[0]:
        row, col = divmod(move, 3)
        
        # Simulate the opponent's move
        game.board[row, col] = 1  # Assume opponent (Player 1) plays here
        if game.check_winner() == 1:  # If this move lets the opponent win
            game.board[row, col] = 0  # Undo the move
            return move  # Return the blocking move
        game.board[row, col] = 0  # Undo the move
    return None
