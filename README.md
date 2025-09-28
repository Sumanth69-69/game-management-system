
# Game Management System

## Introduction
This project is a simple **Game Management System** implemented in Python.  
It allows **Recruiters** to create and manage games, and **Players** to register for available games.  
The project is entirely menu-driven and uses only in-memory data (lists and dictionaries).  
No external file/database is required.

---

## Features
### Recruiter:
- Create a new game (with name, slots, time, place)
- Edit existing game details
- Delete a game

### Player:
- View available games
- Register for a game (only if slots are available)
- Cancel registration

---

##  Requirements
- Python 3.x (no external libraries required)

---

##  How to Run
1. Save the code in a file named `game_management.py`  
2. Open terminal/command prompt and run:
   ```bash
   python game_management.py
   ```

---

##  Code Structure
- `create_game()` → Recruiter creates a game
- `edit_game()` → Recruiter edits details of an existing game
- `delete_game()` → Recruiter deletes a game
- `view_games()` → Player views available games
- `register_game()` → Player registers for a game
- `cancel_registration()` → Player cancels registration
- `main()` → Menu-driven system for recruiter/player actions

---

##  Example Usage
```
1. Recruiter
   1. Create Game
   2. Edit Game
   3. Delete Game

2. Player
   1. View Games
   2. Register
   3. Cancel Registration
```

---

##  Challenges
- Managing slot availability for each game
- Preventing duplicate player registrations
- Keeping data updated when multiple actions are performed

---

##  Conclusion
This project demonstrates the use of **Python functions, lists, and dictionaries** to build a simple game management system.  
It is suitable as a mini-project for students to practice programming concepts.

---

## 🔮 Future Scope
- Add database storage (MySQL/SQLite) for permanent data storage
- Implement a GUI (Tkinter/PyQt/Web-based interface)
- Add user authentication (separate login for recruiter and players)
- Introduce notifications/reminders for registered players
