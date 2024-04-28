

# Python Chess Game

## Description
This project is a two-player chess game developed in Python for a coursework assignment. It is designed with a focus on readability and maintainability, making it ideal for beginners. The game uses the Pygame library to display the chessboard, captured pieces, and other interactive elements.

## Features
- **Chess Basics**: Supports basic chess moves, including pawn double moves, en passant, castling (Rochade), and pawn promotion.
- **Starting Positions**: Offers various starting positions that can be activated by uncommenting lines in the `main_game_loop`.
- **Graphical Interface**: Utilizes Pygame for a user-friendly graphical interface, allowing players to interact with the game using mouse and keyboard.
- **Turn-Based Play**: Displays the current turn and captured pieces for each player.
- **Resign Button**: A button to allow players to resign from the game.
- **Window Scaling**: The game window size can be adjusted through the "scaling_factor" in the `main_game_loop`.

## Limitations
- **No Check/Checkmate**: The game does not include rules for check, checkmate, or stalemate, meaning players can make illegal or forced moves without restriction.
- **No Forced Moves**: Players are not forced to move out of check, allowing for more flexibility but requiring manual enforcement of certain rules.

## Installation and Setup
1. Ensure you have Python installed. This game was created for Python 3.12.
2. Clone or download the project repository to your local machine.
3. Install the required packages by running `pip install -r requirements.txt`.
4. Start the game by running `main_game_loop`.

## Gameplay Instructions
- The game is played on a graphical chessboard. Players can interact using the mouse and keyboard.
- To move a piece, click on the piece, then click on the destination square.
- The game supports basic chess rules, including pawn double moves, en passant, castling, and pawn promotion.
- To resign, click the "Resign" button.

## Development and Contribution
This project was created for a Python coursework assignment. Contributions are not currently accepted. However, feedback and suggestions are welcome.

## Contact Information
For questions or feedback, please contact ottmich1811@gmail.com.