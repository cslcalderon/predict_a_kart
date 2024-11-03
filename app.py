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

# for i in range(num_simulations):
#     character1, character2 = sample(list(CHARACTERS.values()), 2) #no repeats
#     while character1 == character2: 
#         character2 = choice(list(CHARACTERS.values()))
#     race_map_key = choice(list(MAP_DATA.keys()))  
#     race_map = MAP_DATA[race_map_key]

#     my_simulation = Simulation(character1, character2, race_map)
#     final_results = my_simulation.return_all_scores()
#     winner = my_simulation.return_winner()

#     if isinstance(winner, str):  
#         final_outcome = "Tie"
#     else:
#         final_outcome = winner.get_name()

#     results.append({
#         'Character 1': character1.get_name(),
#         'Character 2': character2.get_name(),
#         'Map': race_map_key,  
#         'Outcome': final_outcome, 
#         'Character 1 Base': final_results[0],
#         'Character 2 Base': final_results[1],
#         'Character 1 Map': final_results[2],
#         'Character 2 Map': final_results[3],
#         'Character 1 Final': final_results[4],
#         'Character 2 Final': final_results[5], 
#         'Character 1 PU': final_results[6],
#         'Character 2 PU': final_results[7],

#     })

# with open('simulation_results.csv', mode='w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=['Character 1', 'Character 2', 'Map', 'Outcome', \
#                                               'Character 1 Base', 'Character 2 Base', \
#                                               'Character 1 Map', 'Character 2 Map', \
#                                               'Character 1 Final', 'Character 2 Final', \
#                                               'Character 1 PU', 'Character 2 PU'])
#     writer.writeheader()
#     writer.writerows(results)

# print("Simulation results saved to simulation_results.csv")


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


num_simulations = 1000
results = []

for i in range(num_simulations):
    character1, character2 = sample(list(CHARACTERS.values()), 2)  # Select two different characters
    race_map_key = choice(list(MAP_DATA.keys()))  
    race_map = MAP_DATA[race_map_key]

    simulation = Simulation(character1, character2, race_map)
    all_data = simulation.return_all_data()  # Use return_all_data to get all stats including character details
    
    # Add map key for easier identification
    all_data['Map'] = race_map_key  
    
    # Append results for this simulation run
    results.append(all_data)

# Define the fieldnames for the CSV output, including character stats
fieldnames = [
    'Character 1', 'Weight 1', 'Acceleration 1', 'Top Speed 1', 'Handling 1', 'On Road Traction 1', 'Mini Turbo 1',
    'Character 2', 'Weight 2', 'Acceleration 2', 'Top Speed 2', 'Handling 2', 'On Road Traction 2', 'Mini Turbo 2',
    'Map', 'Outcome', 'Effective Acceleration 1', 'Effective Acceleration 2', 
    'Effective Speed 1', 'Effective Speed 2', 'Power-Ups 1', 'Power-Ups 2'
]

with open('detailed_physics_simulation_results.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    
    for result in results:
        csv_row = {
            'Character 1': result['Character 1 Stats']['Name'],
            'Weight 1': result['Character 1 Stats']['Weight'],
            'Acceleration 1': result['Character 1 Stats']['Acceleration'],
            'Top Speed 1': result['Character 1 Stats']['Top Speed'],
            'Handling 1': result['Character 1 Stats']['Handling'],
            'On Road Traction 1': result['Character 1 Stats']['On Road Traction'],
            'Mini Turbo 1': result['Character 1 Stats']['Mini Turbo'],
            
            'Character 2': result['Character 2 Stats']['Name'],
            'Weight 2': result['Character 2 Stats']['Weight'],
            'Acceleration 2': result['Character 2 Stats']['Acceleration'],
            'Top Speed 2': result['Character 2 Stats']['Top Speed'],
            'Handling 2': result['Character 2 Stats']['Handling'],
            'On Road Traction 2': result['Character 2 Stats']['On Road Traction'],
            'Mini Turbo 2': result['Character 2 Stats']['Mini Turbo'],

            'Map': result['Map'],
            'Outcome': result['Outcome'],
            'Effective Acceleration 1': result['Effective Acceleration 1'],
            'Effective Acceleration 2': result['Effective Acceleration 2'],
            'Effective Speed 1': result['Effective Speed 1'],
            'Effective Speed 2': result['Effective Speed 2'],
            'Power-Ups 1': ', '.join(result['Power-Ups 1']),
            'Power-Ups 2': ', '.join(result['Power-Ups 2']),
        }
        writer.writerow(csv_row)

print("Detailed simulation results saved to detailed_physics_simulation_results.csv")
