# CS50 Programming with Python - Harvard Final Project

## Description

This project, **Alien Invasion**, is a Python-based interactive arcade-style game inspired by classic space shooter games, created after studying *Python Crash Course* by Eric Matthes. Developed as the final submission for the Harvard course, the game challenges players to defend their spaceship from waves of alien invaders while achieving the highest score possible. The game emphasizes fast-paced action, strategic shooting, and careful navigation to avoid collisions.

The player navigates a spaceship along the bottom of the screen, firing bullets at advancing alien fleets. The challenge increases with each level, as aliens move faster and attack in more complex patterns. By combining engaging gameplay with visually appealing graphics and responsive controls, the project demonstrates both programming skill and creative design.

### Key Features

- **Engaging Gameplay:** Players must shoot down incoming aliens while avoiding collisions and preventing aliens from reaching the bottom of the screen.  
- **Dynamic Difficulty:** As the game progresses, alien speed and fleet size increase, ensuring a continuously challenging experience.  
- **Score Tracking:** The game maintains the current score, level, and high score, motivating players to improve their performance.  
- **Customizable Settings:** Players can adjust screen resolution, ship speed, bullet limits, and alien fleet behavior for personalized gameplay.  
- **Polished Visuals:** Custom graphics for the spaceship and aliens create an immersive arcade experience.  
- **Responsive Controls:** Smooth keyboard input allows intuitive movement and firing mechanics.

### Technical Highlights

- **Object-Oriented Design:** Each component of the game (ship, bullets, aliens, scoreboard) is implemented as a class, improving modularity and maintainability.  
- **Collision Detection:** Efficient collision handling ensures accurate bullet-alien and ship-alien interactions.  
- **Game State Management:** Dedicated classes track active/inactive game states, player lives, levels, and scores.  
- **Pygame Library:** Handles graphics rendering, user input, and main game loops for a seamless experience.  
- **Modular Codebase:** The project is divided into multiple files for readability and easier debugging.

### Project Files

- `project.py`: Launches the game and initializes the main game loop.  
- `settings.py`: Contains all configurable settings, such as screen dimensions, ship speed, bullet properties, and alien behavior.  
- `ship.py`: Defines the `Ship` class, including movement, rendering, and boundary handling.  
- `bullet.py`: Implements the `Bullet` class, handling bullet creation, movement, and collision detection.  
- `alien.py`: Defines the `Alien` class and manages alien fleet creation, movement, and collision behavior.  
- `game_stats.py`: Tracks game statistics including score, level, and number of ships remaining.  
- `scoreboard.py`: Displays the player's score, high score, and current level on the screen.  
- `button.py`: Implements start and restart buttons for easy game control.  
- `main.py` (optional if used): Coordinates game setup, events, and updates across modules.
- `test_project.py`: A few functions to ensure that everything is working smoothly

### How to Play

1. **Start the Game:** Run the `project.py` file to launch the game.  
2. **Controls:**  
   - Arrow keys: Move the spaceship left or right.  
   - Spacebar: Fire bullets at aliens.  
3. **Objective:** Destroy all aliens in each fleet while avoiding collisions and preventing them from reaching the bottom of the screen.  
4. **Progression:** Clear all aliens to advance levels; each level increases difficulty with faster, more numerous aliens.  
5. **Game Over:** The game ends when all player ships are lost. High scores are saved for replayability.

### Design Decisions

An object-oriented approach was chosen to maintain a modular and scalable codebase. Each game entity was encapsulated in its own class, simplifying updates, debugging, and potential future enhancements. Difficulty progression was carefully designed by increasing alien speed and quantity per level, balancing challenge and engagement. Pygame was used for efficient graphics rendering and event handling, allowing focus on gameplay mechanics rather than low-level programming. Custom graphics were implemented to create a visually appealing experience while maintaining performance.

This project demonstrates a practical application of Python programming concepts, including object-oriented design, event-driven programming, collision detection, and game development principles.
