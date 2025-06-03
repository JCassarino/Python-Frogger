# Python Frogger 🐸

A Frogger-style game implemented in Python, played in the terminal. Navigate your frog (`0`) across multiple lanes of moving obstacles (`X`) to reach the other side!

## 🌟 Features

* Terminal-based gameplay.
* Loads game levels from custom `.frog` files.
* Player-controlled frog movement (up, down, left, right) and a limited number of special jumps.
* Moving rows of obstacles with varying speeds.
* Win/loss conditions.

## ⚙️ How to Play

### Prerequisites

* Python 3.x installed on your system.

### Running the Game

1.  **Clone or Download:** Get the project files onto your local machine.
    ```bash
    git clone <https://github.com/JCassarino/Python-Frogger>
    cd <Python-Frogger>
    ```
    (Or download the ZIP and extract it).
2.  **Ensure Level Files (`.frog`) are Present:** The game requires at least one `.frog` file in the same directory as the `frogger.py` file to define the game board and parameters. See the "Level File Format" section below for details on how to create these.
3.  **Run the Script:** Execute the main Python script from your terminal:
    ```bash
    frogger.py
    ```
4.  **Select a Game File:** The game will prompt you to choose from the available `.frog` files.
5.  **Gameplay:**
    * Your frog is represented by `0`.
    * Obstacles are represented by `X`.
    * Empty spaces are ` `.
    * The top and bottom rows are safe starting/ending zones.
6.  **Controls:**
    * `w`: Move frog Up
    * `a`: Move frog Left
    * `s`: Move frog Down
    * `d`: Move frog Right
    * `j <row_num> <col_num>`: Jump to a specific column in an adjacent row (e.g., `j 2 5` to jump to row 2, column 5). You have a limited number of jumps. *Note: In the code, `jump_y` is the target row index (0-indexed) and `jump_x` is the target column index (0-indexed after subtracting 1 from user input).*

### Winning/Losing

* **Win:** Reach the bottom-most safe row.
* **Lose:** Land on a space occupied by an obstacle (`X`).

## 📄 Level File Format (`.frog` files)

The game levels are defined in `.frog` text files, structured as:

* **Line 1: Board Configuration**
    * Format: `BOARD <width> <max_jumps>`
    * Example: `BOARD 10 3` (This defines a board width of 10 columns and allows the player 3 jumps).
* **Line 2: Row Speeds**
    * A space-separated list of integers representing the speed of each moving row.
    * The number of speeds should match the number of moving rows you define in the subsequent lines.
    * Positive numbers move objects to the left (as the row "shifts left" on update).
    * Example: `1 -1 2` (Row 1 moves 1 space left, Row 2 moves 1 space right, Row 3 moves 2 spaces left).
* **Line 3 onwards: Board Layout**
    * Each line represents a moving row on the game board.
    * `X` represents an obstacle.
    * ` ` (space) represents an empty path.
    * The length of these lines should match the `<width>` defined in Line 1.
    * The number of these lines will determine the height of the playable area (excluding the top and bottom safe rows).

## Code Overview

The game logic is structured into several functions:

* `select_game_file()`: Prompts user to select a `.frog` level file.
* `board_setup()`: Initializes the game board from the selected file.
* `row_speeds()`: Reads row movement speeds from the file.
* `jump_limit()`: Gets the maximum number of jumps allowed.
* `frog_setup()`: Initializes the frog's starting position.
* `update_board()`: Shifts the rows on the board according to their speeds each turn.
* `display_board()`: Renders the current state of the game board with the frog to the terminal.
* `move_frog()`: Handles player input for movement (WASD).
* `frog_jump()`: Handles the special jump action.
* `win_loss_check()`: Determines if the player has won or lost.
* `play_frogger()`: Main game loop that orchestrates the game flow.

## 📝 Project Status

This is a completed project. No further updates are planned at this time.
