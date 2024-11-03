# data_loader.py
import csv
from Character import Character
from PowerUp import PowerUp
from Map import Map

def load_maps(filename='Super Mario Kart Data - Maps.csv'):
    maps = {}
    
    with open(filename, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            map_name = row['map']
            obstacles = row['obstacles']
            slipperiness = int(row['slipperiness'])
            curvy = row['curvy']
            
            map_obj = Map(name=map_name, obstacles=obstacles, slipperiness=slipperiness, curvy=curvy)
            maps[map_name] = map_obj

    return maps
    

def load_power_ups(filename='Super Mario Kart Data - PowerUps.csv'):
    power_ups = {}
    
    with open(filename, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name'].strip()
            ci = int(row['choco_island'])
            vl = int(row['vanilla_lake'])
            dp = int(row['donut_plains'])
            kb = int(row['koopa_beach'])
            rr = int(row['rainbow_road'])
            speed_related = row['speed_related'].strip().lower() == 'yes'
            
            power_up = PowerUp(name, ci, vl, dp, kb, rr, speed_related)
            power_ups[name] = power_up
    
    return power_ups

def load_characters(filename='Super Mario Kart Data - Players.csv'):
    characters = {}
    
    with open(filename, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name'].strip()
            weight = int(row['weight'])
            acceleration = int(row['acceleration'])
            top_speed = int(row['top_speed'])
            handling = int(row['handling'])
            ci = int(row['choco_island'])
            vl = int(row['vanilla_lake_perf'])
            dp = int(row['donut_plains_perf'])
            kb = int(row['koopa_beach_perf'])
            rr = int(row['rainbow_road_perf'])
            on_road_traction = int(row['on_road_traction'])
            mini_turbo = int(row['mini_turbo'])
            
            character = Character(name, weight, acceleration, top_speed, handling, ci, vl, dp, kb, rr, on_road_traction, mini_turbo)
            characters[name] = character
    
    return characters
