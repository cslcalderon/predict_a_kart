from data_loader import load_maps, load_power_ups, load_characters

# Load data using the functions from data_loader.py
map_data = load_maps()
power_ups = load_power_ups()
characters = load_characters()

# Print data for verification (optional)
print("Map Data:")
for map_name, data in map_data.items():
    print(f"{map_name.capitalize()}: {data}")

print("\nPower-Ups:")
for name, power_up in power_ups.items():
    print(f"{name}: CI={power_up.get_ci()}, VL={power_up.get_vl()}, DP={power_up.get_dp()}, "
          f"KB={power_up.get_kb()}, RR={power_up.get_rr()}, Speed Related={power_up.get_speed_related()}")

print("\nCharacters:")
for name, character in characters.items():
    print(f"{name}: Weight={character.get_weight()}, Acceleration={character.get_acceleration()}, "
          f"Top Speed={character.get_top_speed()}, Handling={character.get_handling()}, "
          f"CI={character.get_ci()}, VL={character.get_vl()}, DP={character.get_dp()}, "
          f"KB={character.get_kb()}, RR={character.get_rr()}")
