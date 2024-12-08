from game import TicTacToe
from model import create_model
from data_generator import generate_data
import numpy as np
import tensorflow as tf
import os

MODEL_PATH = "tic_tac_toe_ai_model.h5"

def ai_move(game, model):
    board_input = game.board.reshape(1, 3, 3)
    predictions = model.predict(board_input)[0]
    
    # Get all valid moves (cells that are 0)
    valid_moves = np.where(game.board.flatten() == 0)[0]
    
    # Filter predictions to only consider valid moves
    valid_predictions = predictions[valid_moves]
    best_move = valid_moves[np.argmax(valid_predictions)]
    
    # Convert the flat index to row and column
    row, col = divmod(best_move, 3)
    game.make_move(row, col)

def main():
    if os.path.exists(MODEL_PATH):
        print("Loading the saved model...")
        model = tf.keras.models.load_model(MODEL_PATH)
    else:
        print("Training the model...")
        X, y = generate_data()
        model = create_model()
        model.fit(X, y, epochs=10, batch_size=32)
        model.save(MODEL_PATH)
        print(f"Model saved to {MODEL_PATH}.")

    # Play the game
    game = TicTacToe()
    while game.check_winner() is None:
        game.display_board()
        if game.player == 1:  # Human player
            try:
                row, col = map(int, input("Enter your move (row and column, 0-indexed): ").split())
                game.make_move(row, col)
            except ValueError as e:
                print(e)
                continue
        else:  # AI player
            ai_move(game, model)

    game.display_board()
    winner = game.check_winner()
    if winner == 1:
        print("You win!")
    elif winner == -1:
        print("AI wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()