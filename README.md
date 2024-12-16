# Tic-Tac-Toe AI Game
This project is an AI-powered Tic-Tac-Toe game where a human player competes against an AI opponent. The AI is trained using a custom dataset of Tic-Tac-Toe games and leverages a neural network to predict optimal moves.

## Project Structure

- **`game.py`**: Implements the Tic-Tac-Toe game logic, including the game board, player moves, and winner determination.
- **`data_generator.py`**: Generates data for training the AI model by simulating Tic-Tac-Toe games, with rewards based on the game outcome.
- **`model.py`**: Defines the TensorFlow model architecture used to train the AI.
- **`main.py`**: The entry point for running the game. Handles training/loading the model and orchestrating the game between the human player and AI.
- **`tic_tac_toe_ai_model.h5`**: Saved AI model after training (created after running the project).

---

## Requirements
    - Python 3.7+
    - TensorFlow
    - NumPy
## Installation:
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
2.  Install the required Python packages using one of the following methods:
    ```bash
    pip install -r requirements.txt
- Or, by manually installing the necessary packages:
    ```bash
    pip install tensorflow numpy
## How It Works
### Game Logic (game.py):
A 3x3 board is represented as a NumPy array.
Players take turns to make moves:
Player uses 1 ("X").
AI uses -1 ("O").
The winner is determined based on rows, columns, or diagonals summing to 3 or -3. A tie occurs if the board is full without a winner.
### Data Generation (data_generator.py):
Simulates games where:
The human plays randomly.
The AI attempts to block the human or plays randomly.
Assigns rewards based on the outcome, used to train the neural network.
### AI Model (model.py):
A neural network with the following layers:
Input Layer: Flattens the 3x3 board into a 1D array.
Dense Layers: Two hidden layers with 128 and 64 neurons, using ReLU activation.
Output Layer: A softmax layer predicting probabilities for each cell (9 outputs).
### Game Execution (main.py):

Loads the AI model if it exists. If not, it trains the model on generated data.
Starts a Tic-Tac-Toe game:
Human makes moves by entering row and column indices.
AI chooses the best move based on model predictions.

## How to Run the main program:
open your terminal and run the following command:

    python main.py  

## Game Instructions:
The board will display as a 3x3 grid. Empty cells are blank, X is Player 1, and O is AI.
Enter your move as two space-separated integers (e.g., 1 2 for row 1, column 2).
The AI will respond immediately after your move.
### Winning Conditions:
Line up three symbols (X or O) vertically, horizontally, or diagonally to win.
#### Key Features
- AI Model: Predicts moves based on probabilities using softmax.
- Dynamic Data Generation: Automatically generates training data using simulated games.
- Winner Determination: Handles human wins, AI wins, or ties.
- Replayable Game: Play as many rounds as you'd like, with the model improving over time.
## Example Game Session

    X|O|
    -----
    |X|O
    -----
    | |X

    Player wins!
---
     |O|
    -----
    X|O|X
    -----
     |O|

    AI wins!
