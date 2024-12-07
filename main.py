from game import TicTacToe
from model import create_model
from data_generator import generate_data
import numpy as np 
def ai_move(game, model):
    board_input = game.board.reshape(1, 3, 3)
    predictions = model.predict(board_input)
    best_move = np.argmax(predictions)
    row, col = divmod(best_move, 3)
    game.make_move(row, col)

def main():
    # Train or load the model
    X, y = generate_data()
    model = create_model()
    model.fit(X, y, epochs=10, batch_size=32)

    # Play the game
    game = TicTacToe()
    while game.check_winner() is None:
        game.display_board()
        if game.current_player == 1:  # Human player
            row, col = map(int, input("Enter your move (row and column): ").split())
            game.make_move(row, col)
        else:  # AI player
            ai_move(game, model)

    winner = game.check_winner()
    if winner == 1:
        print("You win!")
    elif winner == -1:
        print("AI wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
