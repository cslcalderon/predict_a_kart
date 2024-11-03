import streamlit as st
from Simulation import Simulation
from data_loader import load_characters, load_maps

CHARACTERS = load_characters()
MAPS = load_maps()

st.title("Predict-a-Kart 🏎️")

character1_name = st.selectbox("Select Character 1", options=list(CHARACTERS.keys()))
character2_options = [name for name in CHARACTERS.keys() if name != character1_name]
character2_name = st.selectbox("Select Character 2", options=character2_options)

map_name = st.selectbox("Select Map", options=list(MAPS.keys()))

num_simulations = st.number_input("Number of Simulations", min_value=1, max_value=10000, value=1000)

if st.button("Run Simulation"):
    character1 = CHARACTERS[character1_name]
    character2 = CHARACTERS[character2_name]
    selected_map = MAPS[map_name]
    
    character1_wins = 0
    character2_wins = 0
    ties = 0

    for _ in range(num_simulations):
        simulation = Simulation(character1, character2, selected_map)
        winner = simulation.return_winner()
        
        if isinstance(winner, str):  # Tie condition
            ties += 1
        elif winner.get_name() == character1.get_name():
            character1_wins += 1
        else:
            character2_wins += 1

    character1_win_rate = (character1_wins / num_simulations) * 100
    character2_win_rate = (character2_wins / num_simulations) * 100
    tie_rate = (ties / num_simulations) * 100

    st.write(f"**Results over {num_simulations} simulations on {map_name}**")
    st.write(f"{character1_name} Win Rate: {character1_win_rate:.2f}%")
    st.write(f"{character2_name} Win Rate: {character2_win_rate:.2f}%")
    st.write(f"Tie Rate: {tie_rate:.2f}%")
