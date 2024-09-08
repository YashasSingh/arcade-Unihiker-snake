
# UniHiker Snake Game
![image](https://github.com/user-attachments/assets/50fed191-93fa-4f16-bb64-d58d9ea7bca8)

This project is a modern take on the classic Snake game, developed for the UniHiker platform. The game includes various features such as increasing difficulty, power-ups, and high score tracking, making it an engaging and challenging experience.

## Features

- **Classic Snake Gameplay**: Control the snake as it moves around the screen, eating apples to grow longer.
- **High Score Tracking**: Track the highest score achieved during the session.
- **Levels and Increasing Difficulty**: The game becomes progressively harder as you advance through levels, with increasing speed and obstacles.
- **Power-Ups**: Special items that provide benefits like shrinking the snake or slowing down the game.
- **Obstacles**: Avoid obstacles that appear as you level up.
- **Pause and Resume**: Pause and resume the game using button controls.

## Controls

- **Left Button (Pin P0)**: Turn the snake left (counterclockwise).
- **Right Button (Pin P1)**: Turn the snake right (clockwise).
- **Restart Button (Pin P2)**: Restart the game after a game over.

## Installation

1. **UniHiker Library**: Install the `unihiker` library to manage the GUI and game rendering:
   ```bash
   pip install unihiker
   ```

2. **PinPong Library**: Install the `pinpong` library for button handling:
   ```bash
   pip install pinpong
   ```

## Setup

1. Connect the buttons to the corresponding pins on the UniHiker:
   - **Left Button**: Pin P0
   - **Right Button**: Pin P1
   - **Restart Button**: Pin P2

2. Upload the `snake_game.py` script to the UniHiker.

3. Run the script to start playing.

## How to Play

- Control the snake using the left and right buttons to avoid collisions and eat apples.
- Each apple consumed increases your score and the length of the snake.
- As you progress, the game speed increases, and obstacles will appear on the screen.
- Power-ups can occasionally appear, offering temporary advantages.
- The game ends if the snake collides with itself, the walls, or an obstacle.

## Game Over and High Score

- When the game ends, your final score is displayed along with the current high score.
- Press the restart button to play again.

## Future Enhancements

- **Persistent High Score**: Save the high score across game sessions.
- **Additional Power-Ups**: Introduce new power-ups for more varied gameplay.
- **Wrap-Around Mode**: Allow the snake to wrap around the edges of the screen.

## License

This project is open-source and available under the MIT License.
```

