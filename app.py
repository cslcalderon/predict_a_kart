from Simulation import * 

from data_loader import load_maps, load_power_ups, load_characters
from random import * 
import csv

CHARACTERS = load_characters()
MAP_DATA = load_maps()

#ask for user input 
#run the model 
#give final verdict 

#could call UI in here

my_simulation = Simulation(CHARACTERS['toad'], CHARACTERS['bowser'], MAP_DATA['choco_island'])
my_simulation.return_winner()

# Define the number of simulations
num_simulations = 1000
results = []

# Run simulations
for i in range(num_simulations):
    character1 = choice(list(CHARACTERS.values()))
    character2 = choice(list(CHARACTERS.values()))
    while character1 == character2:  # Ensure different characters
        character2 = choice(list(CHARACTERS.values()))
    race_map_key = choice(list(MAP_DATA.keys()))  # Randomly select a map
    race_map = MAP_DATA[race_map_key]

    # Initialize the simulation
    my_simulation = Simulation(character1, character2, race_map)
    final_results = my_simulation.return_all_scores()
    winner = my_simulation.return_winner()

    # Determine the outcome
    if isinstance(winner, str):  
        final_outcome = "Tie"
    else:
        final_outcome = winner.get_name()

    # Store the result in the list
    results.append({
        'Character 1': character1.get_name(),
        'Character 2': character2.get_name(),
        'Map': race_map_key,  
        'Outcome': final_outcome, 
        'Character 1 Base': final_results[0],
        'Character 2 Base': final_results[1],
        'Character 1 Map': final_results[2],
        'Character 2 Map': final_results[3],
        'Character 1 Final': final_results[4],
        'Character 2 Final': final_results[5]
    })

# Write results to CSV
with open('simulation_results.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Character 1', 'Character 2', 'Map', 'Outcome', \
                                              'Character 1 Base', 'Character 2 Base', \
                                              'Character 1 Map', 'Character 2 Map', \
                                              'Character 1 Final', 'Character 2 Final'])
    writer.writeheader()
    writer.writerows(results)

print("Simulation results saved to simulation_results.csv")