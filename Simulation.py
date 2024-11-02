
from data_loader import load_maps, load_power_ups, load_characters
from random import * 

MAP_DATA = load_maps()
POWER_UPS = load_power_ups()
CHARACTERS = load_characters()

class Simulation():
    def __init__(self, character1, character2, map):
        self.character1 = character1
        self.character2 = character2
        self.map = map

    def calc_player_baseline(character_name):
        weight = character_name.get_weight()
        acc = character_name.get_acceleration()
        top_speed = character_name.get_top_speed()
        handling = character_name.get_handling()

        win_statistic = (weight + acc + top_speed + handling) * 0.6
        return win_statistic

    def calc_map_perf(character_name, map):
        map_perf = character_name.get_map_perf(map) * 0.20

    def give_randon_power_ups(character_name):
        for _ in range(3):
            random_key = random.choice(list(POWER_UPS.keys()))
            power_up = POWER_UPS[random_key]
            if power_up.get_speed_related == "yes":
                return 2 * 0.20
            else: 
                return 1 * 0.20

    def calc_win_after_powerup(powerups):
        pass

    def calc_defense_offense(player_one, player_two):
    #passing in characters
    #simulate_interaction(player_one.get_powerups(), player_two.get_powerups())
        pass

    def simulate_interaction(player_one_pu, player_two_pu):
    #decicde if they interact at all
    #how the interaction affects each player
        pass


    def calculate_win_stat (character_one, character_two):
    #run three rounds and output the game state
        pass 




    def calculate_effective_speed(character, track_type):
    # Set weightings based on track type
        if track_type == 'straight':
            speed_weight = 1.2
            acceleration_weight = 0.8
        elif track_type == 'curvy':
            speed_weight = 0.8
            acceleration_weight = 1.2
        elif track_type == 'obstacle_rich':
            speed_weight = 1.0
            acceleration_weight = 1.5
        else:
        # Default weights
            speed_weight = 1.0
            acceleration_weight = 1.0

    # Calculate effective speed
        effective_speed = (character.get_top_speed() * speed_weight +
                       character.get_acceleration() * acceleration_weight)
        return effective_speed


