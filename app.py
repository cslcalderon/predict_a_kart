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

num_simulations = 1000
results = []

for i in range(num_simulations):
    character1, character2 = sample(list(CHARACTERS.values()), 2) #no repeats
    while character1 == character2: 
        character2 = choice(list(CHARACTERS.values()))
    race_map_key = choice(list(MAP_DATA.keys()))  
    race_map = MAP_DATA[race_map_key]

    my_simulation = Simulation(character1, character2, race_map)
    final_results = my_simulation.return_all_scores()
    winner = my_simulation.return_winner()

    if isinstance(winner, str):  
        final_outcome = "Tie"
    else:
        final_outcome = winner.get_name()

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
        'Character 2 Final': final_results[5], 
        'Character 1 PU': final_results[6],
        'Character 2 PU': final_results[7],

    })

with open('simulation_results.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Character 1', 'Character 2', 'Map', 'Outcome', \
                                              'Character 1 Base', 'Character 2 Base', \
                                              'Character 1 Map', 'Character 2 Map', \
                                              'Character 1 Final', 'Character 2 Final', \
                                              'Character 1 PU', 'Character 2 PU'])
    writer.writeheader()
    writer.writerows(results)

print("Simulation results saved to simulation_results.csv")



#PHYSICS ADDITION
num_simulations = 1000  
results = []

for _ in range(num_simulations):
    character1, character2 = sample(list(CHARACTERS.values()), 2)
    race_map_key = choice(list(MAP_DATA.keys()))
    race_map = MAP_DATA[race_map_key]

    simulation = Simulation(character1, character2, race_map)
    physics_scores = simulation.return_physics_scores()
    physics_scores['Map'] = race_map_key  
    results.append(physics_scores)

with open('physics_simulation_results.csv', mode='w', newline='') as file:
    fieldnames = [
        'Character 1', 'Character 2', 'Map', 'Outcome', 'Effective Acceleration 1', 'Effective Acceleration 2', \
        'Effective Speed 1', 'Effective Speed 2','Power-Ups 1', 'Power-Ups 2'
    ]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print("Simulation results saved to physics_simulation_results.csv")