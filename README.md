# **Red-Blue Nim Game**

## **Overview**
The Red-Blue Nim game is a variant of the classic Nim game. This version features two piles of marbles: red and blue. On each player's turn, they choose a pile and remove 1 or 2 marbles. The game supports two modes:
- **Standard**: The player loses if either pile is empty on their turn.
- **Misère**: The player wins if either pile is empty on their turn.

The score is calculated based on the remaining marbles:
- 2 points per red marble.
- 3 points per blue marble.

The program uses **MinMax with Alpha-Beta Pruning** for the computer's decisions, ensuring optimal moves. It supports depth-limited search for extra credit.

---
## **How to Play**
The program alternates turns between a computer and a human player. On the computer's turn, the best move is determined using MinMax with Alpha-Beta Pruning. On the human player's turn, the program prompts for input to perform a move.

The game ends when one pile is empty, and the final score determines the winner.
This project is written in Python version: 3.10.11

My code structure:
1) start_game: Initializes and runs the main game loop, alternating turns between the computer and human players until a terminal condition (an empty pile) is reached.
2) calc_val: An evaluation function that computes the score based on the number of red and blue marbles remaining.
3) end_condition: Checks if the game has reached a terminal state (one of the piles is empty).
4) max_min_algo: Implements the MinMax algorithm with Alpha-Beta pruning, allowing the computer to determine the best move.
5) comp_play: Executes the computer's turn by selecting the optimal move.
6) player_move: Prompts the human player to make a move, ensuring valid input.

Game Variants:
The code supports two versions of the Red-Blue Nim game:

1) Standard: The player who encounters an empty pile loses.
2) Misère: The player who encounters an empty pile wins

To get the code running:

- You need to have Python 3.8 or newer versions
- The program is run using command-line arguments in the following format:

python red_blue_nim.py <num-red> <num-blue> <version> <first-player> <depth>

What it means: 
<num-red>: Initial number of red marbles (integer).
<num-blue>: Initial number of blue marbles (integer).
<version>: Game mode (standard or misère).
<first-player>: Who starts the game (computer or human).
<depth>: Depth of search for MinMax with Alpha-Beta Pruning 


Example: 

python red_blue_nim.py 4 3 misère human 4

the parameters mean:
the parameters mean:
4 red marbles
3 blue marbles
Misère version
Human player starting first
Depth of 4 for search 
