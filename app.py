from Simulation import * 

from data_loader import load_maps, load_power_ups, load_characters
from random import * 

CHARACTERS = load_characters()
MAP_DATA = load_maps()

#ask for user input 
#run the model 
#give final verdict 

#could call UI in here

my_simulation = Simulation(CHARACTERS['toad'], CHARACTERS['bowser'], MAP_DATA['choco_island'])
my_simulation.return_winner()