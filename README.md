# Knight Tour

A console application for constructing a chess knight's route across a chessboard.

The program allows you to choose the route construction algorithm, board size, knight's starting position, and result display method.

## Features

- choosing the chessboard size;
- choosing the knight's starting position;
- constructing a random route;
- constructing a route using Warnsdorff's algorithm;
- validating the constructed route;
- displaying the route in the console;
- visualizing the route on a chessboard;
- displaying the route both in the console and on the board;
- handling invalid user input.

## Algorithms

### Random Route

At each step, the program randomly selects one of the available squares the knight can move to.

Because the choice is random, the route may not cover the entire board and may end early if there are no available moves from the current position.

### Warnsdorff's Algorithm

For each possible next move, the program determines the number of further available moves.

At each step, the square with the minimum number of onward moves is selected. This allows the program to construct long knight's routes much more efficiently.

## Route Validation

After the route is constructed, it is automatically validated.

The following are checked:

- the sequence of move numbers;
- the validity of each knight's move;
- whether all coordinates are within the board;
- the number of visited squares.

As a result, the program reports whether the route is valid and whether the knight has covered the entire board.

## Project Structure

```text
knightTour/
├── main.py             # Main menu and program control
├── knight.py           # Route construction logic
├── board.py            # Route output and board visualization
├── validator.py        # Route validation
├── input_handler.py    # User input handling
├── README.md           # Project documentation
└── .gitignore
```

## Installation

Python and the `matplotlib` library are required for visualization.

Install the dependency with:

```bash
pip install matplotlib
```

## Running

Navigate to the project directory and run:

```bash
python main.py
```

After launching, the main menu will be displayed:

```text
==================================================
                  KNIGHT'S TOUR
==================================================

Current settings:
  Board size    : 8x8
  Output method : board

--------------------------------------------------
1 — Random Route
2 — Warnsdorff's Algorithm
3 — Change Board Size
4 — Change Output Method
0 — Exit

Choose an action:
```

## Output Methods

The program supports three output modes:

**1 — Console**

The route is displayed as a table containing move numbers.

**2 — Board**

The route is displayed graphically on a chessboard using `matplotlib`.

**3 — Console and Board**

Both output methods are used simultaneously.

## Example

For an `8×8` board and a selected algorithm, the program may construct a route such as:

```text
11  . 13  .  9  .  7 34
14  1 10  3  . 35  .  .
 . 12 15  .  .  8 33  6
 .  .  2 17  4  . 36 31
41 16 19  .  . 32  5  .
20  . 40 27 18 25 30 37
 . 42  . 22 39 28  . 24
 . 21  . 43 26 23 38 29
```

After constructing the route, the program reports the number of visited squares and the route status.

## Technologies Used

- Python
- `matplotlib`
- Warnsdorff's algorithm
- `dict` and `list` data structures
- exception handling
- modular program organization

## Project Goal

The project was created to practice Python development and implement knight's tour algorithms with subsequent visualization of the result.