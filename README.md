# 🏎️ Predict-a-Kart 🏆

Welcome to **Predict-a-Kart** – a Mario Kart-inspired simulation where characters face off on legendary maps! This project uses Python to simulate races, leveraging stats from **Super Mario Kart** data to bring the thrill of the race to your terminal! 🎮

---

## 📋 Project Overview & Figma 

Predict-a-Kart simulates epic battles between iconic Mario Kart characters across different maps! This simulation uses character stats, map-specific physics, and power-ups to determine who will cross the finish line first. You can run thousands of simulations, dive into physics-based results, and explore exciting CSV outputs! 

📊Figma: https://www.figma.com/proto/2L4W4Rlapyn1NUwc8bFSS2/Hack24?node-id=1-3&node-type=canvas&t=vcyBvKrgJhVfZuRy-1&scaling=scale-down&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=1%3A3&share=1

### Features
- 🏁 **Race Simulations**: Pit characters like Toad 🐸 and Bowser 🐢 against each other on maps like Choco Island 🍫 and Rainbow Road 🌈!
- ⚙️ **Character & Map Data**: Each character has unique stats – from speed to handling, while each map has challenges like slipperiness and curves.
- 💥 **Power-Ups**: Randomly applied power-ups add a thrilling twist to each race.
- 📈 **Results Output**: Get detailed results with character scores, map influences, and final winners saved to CSV files.

---

## 🚀 Getting Started

1. **Clone this repo**: Get all the code files for the project.
2. **Install Requirements**: Make sure you have Python 3.10 or later installed. You may also need packages like `csv` if they aren’t already available in your setup.
3. **Run the Simulation**: Use `app.py` to start the fun – set up matchups, select maps, and let the races begin!

### Example Command
```bash
python app.py
```

---

## 📂 Project Structure

- **`app.py`**: The main file to run the simulation! It sets up characters, selects maps, and runs simulations.
- **`data_loader.py`**: Loads character, map, and power-up data from CSV files. 📊
- **`Simulation.py`**: The core of the project – runs each race simulation using character stats and map physics.
- **`Map.py`, `Character.py`, `PowerUp.py`**: Classes defining the properties and methods for maps, characters, and power-ups.

---

## 🧪 Running Simulations

Set up the number of races, choose characters, and specify maps to see who takes the gold 🥇! The code runs simulations based on physics and randomness, generating scores for each matchup.

Results are saved in:
- `simulation_results.csv` for overall race outcomes 🏆
- `physics_simulation_results.csv` for physics-based scores and effects ⚙️

---

## 📊 Sample Data

In `simulation_results.csv`, you’ll see:
- **Character Matchups**: E.g., Mario vs. Luigi
- **Map Details**: Like Choco Island 🍫 or Koopa Beach 🐢
- **Race Outcomes**: The final winner or tie

---

## 📈 Future Enhancements

We’re just getting started! Consider adding:
- More characters 🎉
- Additional maps 🌍
- Advanced power-up effects 🚀
- Visualized race results 🖼️

---

## 🤝 Contributing & Running

Feel free to fork this repo and submit pull requests for improvements! Let’s make Mario Kart simulations even more exciting! 🥳
You can also run our preliminary UI when you download our project and run the command `streamlit run app_ui.py`

---

## 🏆 Credits

This project is inspired by Mario Kart and developed with ❤️ for simulation and data enthusiasts.

Happy racing! 🏎️💨
