
from data_loader import load_maps, load_power_ups, load_characters
import random
MAP_DATA = load_maps()
POWER_UPS = load_power_ups()
CHARACTERS = load_characters()

POWERUP_OBT_PROB = 0.80
HIT_PROB = 0.30


class Simulation():
    def __init__(self, character1, character2, race_map):
        character1.powerups = []
        character2.powerups = []

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
    
    def calc_effective_acceleration(self, character, race_map):
        mass = character.get_weight()
        base_acc = character.get_acceleration()
        slipperiness = race_map.get_slipperiness()

        friction_coefficient = max(0.1, 1 - (slipperiness / 10))  
        frictional_force = friction_coefficient * mass

        effective_acc = base_acc - (frictional_force / mass)
        effective_acc = max(effective_acc, 0) 

        # print(f"{character.get_name()} effective acceleration on {race_map['name']}: {effective_acc}")
        return effective_acc
    
    def calc_effective_speed(self, character, race_map):
        mass = character.get_weight()
        base_speed = character.get_top_speed()
        curvy = race_map.get_curvy() == "yes"

        speed_penalty = 0.8 if curvy else 1.0  
        effective_speed = base_speed * speed_penalty

        if not curvy:
            momentum_bonus = 0.05 * mass  
            effective_speed += momentum_bonus

        # print(f"{character.get_name()} effective speed on {race_map['name']}: {effective_speed}")
        return effective_speed
    
    def calc_total_physics_performance(self, character, race_map):
        effective_acc = self.calc_effective_acceleration(character, race_map)
        effective_speed = self.calc_effective_speed(character, race_map)
    
        if race_map.get_curvy() == "yes":
            total_performance = (effective_acc * 0.6) + (effective_speed * 0.4)
        else:
            total_performance = (effective_acc * 0.4) + (effective_speed * 0.6)
    
        # print(f"{character.get_name()} total physics performance on {race_map['name']}: {total_performance}")
        return total_performance

    def calc_map_perf(self, character, race_map):
        if race_map.get_curvy() == "yes":
            handling_weight = 0.4
            traction_weight = 0.3
        else:
            handling_weight = 0.2
            traction_weight = 0.2

        slipperiness_weight = race_map.get_slipperiness() / 5  
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


    # def calc_powerup_perf(self, character):
    #     powerup_effect = 0  

    #     for _ in range(3): 
    #         if random.random() < POWERUP_OBT_PROB:  
    #             random_key = random.choice(list(POWER_UPS.keys()))
    #             power_up = POWER_UPS[random_key]
    #             character.add_powerup(power_up) 

    #             if power_up.get_speed_related():
    #                 powerup_effect += 0.20  
    #             else:
    #                 powerup_effect += 0.10  

    #     return powerup_effect
    
    def calc_powerup_perf(self, character):
        powerup_effect = 0  

        for _ in range(3):  
            if random.random() < POWERUP_OBT_PROB:  
                power_up = random.choice(list(POWER_UPS.values()))
            
                map_name = self.race_map.get_name() 
                power_up_probability = power_up.get_probability_for_map(map_name)
            
                if random.random() < power_up_probability:
                    character.add_powerup(power_up) 

                    if power_up.get_speed_related():
                        powerup_effect += 0.20
                    else:
                        powerup_effect += 0.10

        return powerup_effect



    def calculate_total_performance(self, character):
        baseline_score = self.calc_player_baseline(character)
        map_score = self.calc_map_perf(character, self.race_map)
        powerup_score = self.calc_powerup_perf(character)

        final_score = (baseline_score * 0.5) + (map_score * 0.3) + (powerup_score * 0.2)
        return final_score
    
    def calculate_total_performance_physics(self, character):
        physics_score = self.calc_total_physics_performance(character, self.race_map)
        powerup_score = self.calc_powerup_perf(character)

        final_score = (physics_score * 0.8) + (powerup_score * 0.2)
        return final_score

    

    def return_all_scores(self):
        baseline_score_1 = self.calc_player_baseline(self.character1)
        baseline_score_2 = self.calc_player_baseline(self.character2)

        map_score_1 = self.calc_map_perf(self.character1, self.race_map)
        map_score_2 = self.calc_map_perf(self.character2, self.race_map)


        score1 = self.calculate_total_performance(self.character1)
        score2 = self.calculate_total_performance(self.character2)

        pu1 = self.character1.get_powerups()
        pu2 = self.character2.get_powerups()

        # print(f"{self.character1.get_name()}: {score1}")
        # print(f"{self.character2.get_name()}: {score2}")

        return [baseline_score_1, baseline_score_2, map_score_1, map_score_2, score1, score2, pu1, pu2]

    def return_winner(self):
        #baseline, map_score, power_ups, probability
        score1 = self.calculate_total_performance_physics(self.character1)
        score2 = self.calculate_total_performance_physics(self.character2)

        if score1 > score2:
            return self.character1
        elif score2 > score1:
            return self.character2
        else:
            return "It's a tie!"
        
    def return_physics_scores(self):
        # Calculate effective acceleration and speed for each character
        effective_acc_1 = self.calc_effective_acceleration(self.character1, self.race_map)
        effective_speed_1 = self.calc_effective_speed(self.character1, self.race_map)
        effective_acc_2 = self.calc_effective_acceleration(self.character2, self.race_map)
        effective_speed_2 = self.calc_effective_speed(self.character2, self.race_map)
        
        # Final outcome
        winner = self.return_winner()
        if isinstance(winner, str):  
            final_outcome = "Tie"
        else:
            final_outcome = winner.get_name()
        
        # Power-ups
        powerups_1 = [self.character1.get_powerups()]
        powerups_2 = [self.character2.get_powerups()]

        # Collect results
        return {
            'Character 1': self.character1.get_name(),
            'Character 2': self.character2.get_name(),
             'Outcome': final_outcome,
            'Effective Acceleration 1': effective_acc_1,
            'Effective Acceleration 2': effective_acc_2,
            'Effective Speed 1': effective_speed_1,
            'Effective Speed 2': effective_speed_2,
            'Power-Ups 1': powerups_1,
            'Power-Ups 2': powerups_2
        }



