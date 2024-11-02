from data_loader import load_maps, load_power_ups, load_characters

map_data = load_maps()
power_ups = load_power_ups()
characters = load_characters()
print(characters)


# print("Map Data:")
# for map_name, data in map_data.items():
#     print(f"{map_name.capitalize()}: {data}")

# print("\nPower-Ups:")
# for name, power_up in power_ups.items():
#     print(f"{name}: CI={power_up.get_ci()}, VL={power_up.get_vl()}, DP={power_up.get_dp()}, "
#           f"KB={power_up.get_kb()}, RR={power_up.get_rr()}, Speed Related={power_up.get_speed_related()}")

# print("\nCharacters:")
# for name, character in characters.items():
#     print(f"{name}: Weight={character.get_weight()}, Acceleration={character.get_acceleration()}, "
#           f"Top Speed={character.get_top_speed()}, Handling={character.get_handling()}, "
#           f"CI={character.get_ci()}, VL={character.get_vl()}, DP={character.get_dp()}, "
#           f"KB={character.get_kb()}, RR={character.get_rr()}")

def calc_player_baseline(character_name):
    weight = character_name.get_weight()
    acc = character_name.get_acceleration()
    top_speed = character_name.get_top_speed()
    handling = character_name.get_handling()

    win_statistic = weight ()


def calc_map_perf(character_name, map):
    pass

def give_randon_power_ups(character_name):
    pass

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

