#NAME: Shruti Gunasekaran
#ID: 1002162170


import sys

#x - is red
#y- is blue
#The below code :
# Define an evaluation function that calculates the score based on remaining marbles
# Multiplies red and blue marbles by their respective point values (2 and 3) for score computation
# Checks if the game has reached a terminal state (that isone pile is empty)
# If either pile is empty, the game ends based on standard or misère rules

def start_game(x, y, mode='standard', p_turn='computer', lvl=None):
    print("----------------------!!Welcome to the game!!------------------\n")
    def calc_val(a, b):
        
        return a * 2 + b * 3
    
    def end_condition(x, y):
        
        return x == 0 or y == 0
    

# The below code:
 # Checks if a terminal state is reached or depth limit is met
 # If yes, calculate and return the outcome score based on the game mode
 # Define possible moves based on game type, prioritizing higher reductions
 # Check that enough marbles are available for each move option
 # Prune branches that will not be selected
 # Define possible moves based on game type, prioritizing lower reductions
 # Check that enough marbles are available for each move option
 # Prune branches that will not be selected





    def max_min_algo(x, y, lvl, max_turn, alpha_val, beta_val, game_type):
        
        if end_condition(x, y) or (lvl is not None and lvl == 0):
            outcome = calc_val(x, y)
            if game_type == 'standard':
                return -outcome if max_turn else outcome
            else:  # misère version
                return outcome if max_turn else -outcome


        if max_turn:
            max_result = float('-inf')
            
            move_choices = [(2, 0), (0, 2), (1, 0), (0, 1)] if game_type == 'standard' else [(0, 1), (1, 0), (0, 2), (2, 0)]
            for r_move, b_move in move_choices:
                if (x >= r_move) and (y >= b_move):
                    eval_result = max_min_algo(x - r_move, y - b_move, lvl - 1 if lvl is not None else None, False, alpha_val, beta_val, game_type)
                    max_result = max(max_result, eval_result)
                    alpha_val = max(alpha_val, eval_result)
                    if beta_val <= alpha_val:
                        break
            return max_result
        else:
            min_result = float('inf')
            
            move_choices = [(2, 0), (0, 2), (1, 0), (0, 1)] if game_type == 'standard' else [(0, 1), (1, 0), (0, 2), (2, 0)]
            for r_move, b_move in move_choices:
                if (x >= r_move) and (y >= b_move):
                    eval_result = max_min_algo(x - r_move, y - b_move, lvl - 1 if lvl is not None else None, True, alpha_val, beta_val, game_type)
                    min_result = min(min_result, eval_result)
                    beta_val = min(beta_val, eval_result)
                    if beta_val <= alpha_val:
                        break
            return min_result
        


#The below code:
# Initializes optimal move variables for the computer's best choice
# Choose moves based on game type, with different priorities for each mode
# Ensures there are enough marbles to make the move
# Update optimal move if current move has a higher score
# Prompt the player for input until a valid move is chosen
# Validate if there are enough marbles in the selected pile

        
    def comp_play(x, y, game_type, lvl):
       
        optimal_score = float('-inf')
        optimal_move = None
        action_set = [(2, 0), (0, 2), (1, 0), (0, 1)] if game_type == 'standard' else [(0, 1), (1, 0), (0, 2), (2, 0)]
        for r_take, b_take in action_set:
            if (x >= r_take) and (y >= b_take):
                move_score = max_min_algo(x - r_take, y - b_take, lvl - 1 if lvl is not None else None, False, float('-inf'), float('inf'), game_type)
                if move_score > optimal_score:
                    optimal_score = move_score
                    optimal_move = (r_take, b_take)
        return optimal_move
    
    def player_move(x, y):
       
        while True:
            try:
                print(f"Current state - Red marbles: {x}, Blue marbles: {y}")
                chosen_pile = input("--> Choose a pile to pick from (red/blue): ").strip().lower()
                if chosen_pile not in ('red', 'blue'):
                    print("----Invalid choice. Please choose 'red' or 'blue'.-------")
                    continue
                amount = int(input("--> Choose number of marbles to remove (1 or 2): ").strip())
                if amount not in (1, 2):
                    print("--------Invalid count! Please choose 1 or 2.----------")
                    continue
                if chosen_pile == 'red' and x >= amount:
                    return (amount, 0)
                elif chosen_pile == 'blue' and y >= amount:
                    return (0, amount)
                else:
                    print(f"-------Invalid move! Not enough {chosen_pile} marbles left.---------")
            except ValueError:
                print("------Invalid input! Please try again.----------")


# Main game loop
# Loop continues until a terminal condition is reached (one pile is empty)
# Computer decides its optimal move using the max_min_algo function
# Human player is prompted to make a move
# Determine and display the game outcome
# Determine winner based on game type and current turn
# Parse command-line arguments for initial game setup


    current_turn = p_turn
    while not end_condition(x, y):
        if current_turn == 'computer':
            action = comp_play(x, y, game_type, lvl)
            if action is None:
                break
            x -= action[0]
            y -= action[1]
            print(f"** Computer has removed {action[0]} red and {action[1]} blue marbles.")
            current_turn = 'human'
        else:
            action = player_move(x, y)
            x -= action[0]
            y -= action[1]
            print(f"** Human has removed {action[0]} red and {action[1]} blue marbles.")
            current_turn = 'computer'

    # outcome
    final_score = calc_val(x, y)
    if end_condition(x, y):
        if game_type == 'standard':
            winner = 'Human' if current_turn == 'computer' else 'Computer'
        else:
            winner = 'Computer' if current_turn == 'computer' else 'Human'
        print(f"-------------------!!Game Over!! {winner} wins with a score of {final_score} .-----------------------")
    else:
        print("--------------!!Game Over!! It's a draw.------------------")

if __name__ == '__main__':
   
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    game_type = sys.argv[3] if len(sys.argv) > 3 else 'standard'
    p_turn = sys.argv[4] if len(sys.argv) > 4 else 'computer'
    lvl = int(sys.argv[5]) if len(sys.argv) > 5 else None


    start_game(x, y, game_type, p_turn, lvl)


