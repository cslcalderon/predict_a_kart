
from data_loader import load_maps, load_power_ups, load_characters
from random import * 

MAP_DATA = load_maps()
POWER_UPS = load_power_ups()
CHARACTERS = load_characters()

POWERUP_OBT_PROB = 0.80
HIT_PROB = 0.30


class Simulation():
    def __init__(self, character1, character2, race_map):
        self.character1 = character1
        self.character2 = character2
        self.race_map = race_map

    def calc_player_baseline(self, character_name):
        weight = character_name.get_weight()
        acc = character_name.get_acceleration()
        top_speed = character_name.get_top_speed()
        handling = character_name.get_handling()
        on_road_traction = character_name.get_on_road_traction()
        mini_turbo = character_name.get_mini_turbo()


        baseline = (weight + acc + top_speed + handling + on_road_traction + mini_turbo) / 55
        print(f"{character_name.get_name()} baseline performance: {baseline}")

        return baseline

    def calc_map_perf(self, character, race_map):
        if race_map['curvy'] == "yes":
            handling_weight = 0.4
            traction_weight = 0.3
        else:
            handling_weight = 0.2
            traction_weight = 0.2

        slipperiness_weight = race_map['slipperiness'] / 5  
        traction_weight += slipperiness_weight * 0.2
        handling_weight += slipperiness_weight * 0.1
        
        remaining_weight = 1 - (handling_weight + traction_weight)
        acceleration_weight = remaining_weight / 2
        speed_weight = remaining_weight / 2

        map_perf = ((character.get_handling() * handling_weight +
                character.get_on_road_traction() * traction_weight +
                character.get_acceleration() * acceleration_weight +
                character.get_top_speed() * speed_weight)) / 40
        
        print(f"{character.get_name()} map performance: {map_perf}")

        return map_perf


    def give_random_power_ups(self, character_name):
        for _ in range(3):
            random_key = random.choice(list(POWER_UPS.keys()))
            power_up = POWER_UPS[random_key]
            character_name.add_powerup(power_up)
            if power_up.get_speed_related == "yes":
                return 2 * 0.20
            else: 
                return 1 * 0.20

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


    def calculate_total_performance(self, character):
        baseline_score = self.calc_player_baseline(character)
        map_score = self.calc_map_perf(character, self.race_map)
        #powerup_score = self.calc_powerup_perf(character)

        final_score = (baseline_score * 0.6) + (map_score * 0.4) 
        return final_score

    def return_all_scores(self):
        baseline_score_1 = self.calc_player_baseline(self.character1)
        baseline_score_2 = self.calc_player_baseline(self.character2)

        map_score_1 = self.calc_map_perf(self.character1, self.race_map)
        map_score_2 = self.calc_map_perf(self.character2, self.race_map)


        score1 = self.calculate_total_performance(self.character1)
        score2 = self.calculate_total_performance(self.character2)

        # print(f"{self.character1.get_name()}: {score1}")
        # print(f"{self.character2.get_name()}: {score2}")

        return [baseline_score_1, baseline_score_2, map_score_1, map_score_2, score1, score2]

    def return_winner(self):
        #baseline, map_score, power_ups, probability
        score1 = self.calculate_total_performance(self.character1)
        score2 = self.calculate_total_performance(self.character2)

        if score1 > score2:
            return self.character1
        elif score2 > score1:
            return self.character2
        else:
            return "It's a tie!"



