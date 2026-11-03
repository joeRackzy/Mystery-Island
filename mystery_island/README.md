# 🏝️ Mystery Island: The Lost Lighthouse

## About the Project

Mystery Island: The Lost Lighthouse is a beginner-friendly Python terminal game.

The player is stranded on a mysterious island and must explore different locations, collect useful objects, manage energy, and restore the lost lighthouse beacon to win.

## Features

- Player name input.
- Five island locations.
- Player energy management.
- Random weather conditions.
- Movement restrictions during rain.
- Object collection (Rope and Lantern).
- Inventory and player status.
- Lighthouse restoration.
- Replay option.
- Input validation.

## Game Rules

1. The player starts at the Beach with 5 energy points.
2. The player must explore the island to find a Rope and a Lantern.
3. The Rope is required to cross the Old Bridge.
4. The Lantern is required to restore the Lighthouse.
5. Every successful movement reduces energy by 1.
6. Invalid or cancelled movements do not reduce energy.
7. The player cannot move while it is raining.
8. The player loses when energy reaches zero.
9. The player wins by restoring the Lighthouse beacon.

## Island Locations

- Beach
- Jungle
- Cave
- Old Bridge
- Lighthouse

## Requirements

- Python 3.10 or later.
- No external Python packages are required.

## How to Run the Game

1. Open your terminal.
2. Navigate to the project folder.
3. Run:

```bash
python3 main.py
```

## How to Run Tests

The project uses Python's built-in `unittest` framework.

Run:

```bash
python3 -m unittest -v
```

## Project Files

```text
mystery_island/
├── main.py
├── test_main.py
├── README.md
├── .gitignore
└── monkey.py
```

- `main.py` — Contains the game logic.
- `test_main.py` — Contains automated tests.
- `README.md` — Provides project documentation.
- `.gitignore` — Specifies files Git should ignore.

## Project Status

The game has been implemented and automated tests have been written to check its main features.

More improvements may be added as development continues 
am Joseph Ameh Ocheme
thank you.