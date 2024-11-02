import Character
import numpy as np
import csv

CHOCO_ISLAND = {}
VANILLA_LAKE = {}
DONUT_PLAINS = {}
KOOPA_BEACH = {}
RAINBOW_ROAD = {}

map_dicts = {
    'choco_island': CHOCO_ISLAND,
    'vanilla_lake': VANILLA_LAKE,
    'donut_plains': DONUT_PLAINS,
    'koopa_beach': KOOPA_BEACH,
    'rainbow_road': RAINBOW_ROAD
}

with open('Super Mario Kart Data - Maps.csv', mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        map_name = row['map']
        obstacles = row['obstacles']
        slipperiness = int(row['slipperiness'])
        terrain = row['terrain']
        
        if map_name in map_dicts:
            map_dicts[map_name]['obstacles'] = obstacles
            map_dicts[map_name]['slipperiness'] = slipperiness
            map_dicts[map_name]['terrain'] = terrain

print("Choco Island:", CHOCO_ISLAND)
print("Vanilla Lake:", VANILLA_LAKE)
print("Donut Plains:", DONUT_PLAINS)
print("Koopa Beach:", KOOPA_BEACH)
print("Rainbow Road:", RAINBOW_ROAD)

print(CHOCO_ISLAND)



