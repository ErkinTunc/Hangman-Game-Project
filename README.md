# Hangman Game — Terminal & Graphical Versions

## Project Overview
This Python project implements a classic **Hangman (Pendu)** game in two modes:

1. **Terminal Version (Stable, Fully Functional)**
2. **Graphical Version using Turtle (Work in Progress, Requires Further Development)**

---

## Features

### Terminal Version (`fonctions.py`)

**Status:** Fully functional, runs without any issues.

**Included Features:**
- Human Player Mode (manual letter guessing)
- AI Player Mode (computer guesses automatically)
- Difficulty Levels:
  - Easy Mode (10 max errors)
  - Hard Mode (5 max errors)
- Topics:
  - Films (`motsCinema.txt`)
  - Music (`motsMusic.txt`)
  - Additional topics (Sports, Animals) can be easily added.
- AI Strategies:
  - Alphabetical order guessing
  - Random guessing
  - Frequency-based guessing (based on word file letter frequency)
- Console-based text interface:
  - Simple and clear menu system
  - Replay and exit options available at each step

**Note:**  
The terminal version is included at the bottom of `fonctions.py` (under the comment `# !======MENU======!`).  
To use it, simply **uncomment the loop** and run:

```bash
python fonctions.py
```

**This version runs without problems.**

---

### Graphical Version (`Final.py`)

**Status:** Functional but still in development; further refinement required.

**Technologies Used:**
- Python's `turtle` module for graphics
- Keyboard-controlled menu navigation

**Implemented Features:**
- Graphical loading screen
- Menu system with four options:
  1. Play manually
  2. Let AI play
  3. Options (difficulty and topic selection)
  4. Quit game
- Visual difficulty and topic indicators
- Graphical drawing of Hangman figure
- Integrated gameplay logic from `fonctions.py`

**Current Limitations / To-Do:**
- Improve graphical transitions and animations
- Better win/lose visual feedback
- Smoother navigation and input feedback
- Code structure optimization

**Run:**
```bash
python Final.py
```

Controls:
- `1`: Play manually
- `2`: AI play
- `3`: Options
- `4`: Quit
- `q`: Return to Menu

---

## File Structure

| File            | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| `fonctions.py`  | Core game logic, AI strategies, terminal menu system (stable version).      |
| `Final.py`      | Turtle-based graphical interface (under development).                       |
| `motsCinema.txt`| Word list for Film topic (required for gameplay).                           |
| `motsMusic.txt` | Word list for Music topic (required for gameplay).                          |

---

## Dependencies
- Python 3.x
- Standard libraries:
  - `random`, `time`, `os`, `sys`, `turtle`
  
Optional:
- `Faker` (currently commented out, can be used for generating random word files)

---

## Usage Summary

### Terminal Version:
1. Open `fonctions.py`.
2. Uncomment the menu loop at the bottom (under `# !======MENU======!`).
3. Run:
   ```bash
   python fonctions.py
   ```

### Graphical Version:
1. Ensure `motsCinema.txt` and `motsMusic.txt` are in the project folder.
2. Run:
   ```bash
   python Final.py
   ```

---

## Future Improvements
- Add additional topics (Sports, Animals, etc.).
- Improve graphical interface and transitions.
- Add multiplayer mode.
- Implement score tracking.
- Extend language support (e.g., French, Spanish).
