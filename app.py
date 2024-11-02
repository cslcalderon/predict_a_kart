from mario_model import *

#ask for user input 
#run the model 
#give final verdict 

#could call UI in here

def simulate_race(character1, character2, track_conditions, power_up_effects):
    # Calculate initial stats based on character and track
    char1_speed = calc_player_baseline(character1)+ calc_win_after_powerup(character1)
    char2_speed = character2.top_speed + power_up_effects.get(character2.name, 0)
    
    # Adjust for track slipperiness and handling
    char1_adjusted_speed = char1_speed - (track_conditions['slipperiness'] / character1.handling)
    char2_adjusted_speed = char2_speed - (track_conditions['slipperiness'] / character2.handling)
    
    # Simulate the outcome based on adjusted speeds (higher speed = likely winner)
    winner = character1.name if char1_adjusted_speed > char2_adjusted_speed else character2.name
    win_margin = abs(char1_adjusted_speed - char2_adjusted_speed)  # Record how close the race was
    
    return winner, win_margin