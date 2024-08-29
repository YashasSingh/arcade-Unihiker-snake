from unihiker import GUI
from pinpong.board import Board, Pin
import time
import random

# Initialize GUI and pinpong
gui = GUI()
Board("unihiker").begin()

# Set up the grid size
GRID_SIZE = 20
WIDTH = gui.width() // GRID_SIZE
HEIGHT = gui.height() // GRID_SIZE

# Setup buttons
button_left = Pin(Pin.P0, Pin.IN)  # Left button connected to Pin P0
button_right = Pin(Pin.P1, Pin.IN)  # Right button connected to Pin P1
button_restart = Pin(Pin.P2, Pin.IN)  # Restart button connected to Pin P2

# Function to initialize the game state
def initialize_game():
    global snake, direction, apple
    snake = [(5, 5), (4, 5), (3, 5)]
    direction = (1, 0)  # Moving right initially
    apple = generate_apple()

# Generate random apple position
def generate_apple():
    while True:
        apple = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
        if apple not in snake:
            return apple

def draw_snake():
    gui.clear()  # Clear the screen
    # Draw the snake
    for segment in snake:
        x, y = segment
        gui.draw_rectangle(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE, fill="green")
    
    # Draw the apple
    gui.draw_rectangle(apple[0] * GRID_SIZE, apple[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE, fill="red")
    
    gui.show()

# Function to turn the snake left (counterclockwise)
def turn_left():
    global direction
    direction = (-direction[1], direction[0])

# Function to turn the snake right (clockwise)
def turn_right():
    global direction
    direction = (direction[1], -direction[0])

# Function to check for collisions
def check_collision(new_head):
    # Wall collision
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        return True
    # Self-collision (excluding the last segment since it will move)
    if new_head in snake[:-1]:
        return True
    return False

# Function to display game over and wait for restart
def game_over():
    gui.clear()
    gui.draw_text(gui.width() // 2 - 50, gui.height() // 2 - 10, "Game Over", fill="red", size=24)
    gui.draw_text(gui.width() // 2 - 80, gui.height() // 2 + 20, "Press Restart to Play Again", fill="blue", size=16)
    gui.show()
    
    # Wait for the restart button to be pressed
    while button_restart.read() != 0:
        time.sleep(0.1)

    # Restart the game
    initialize_game()

# Initialize game state
initialize_game()

# Main loop
while True:
    draw_snake()

    # Check button inputs with debouncing
    if button_left.read() == 0:  # Left button pressed
        turn_left()
        time.sleep(0.2)  # Debounce delay

    elif button_right.read() == 0:  # Right button pressed
        turn_right()
        time.sleep(0.2)  # Debounce delay

    # Move the snake by updating the position
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Check for collisions
    if check_collision(new_head):
        game_over()  # Handle game over and wait for restart
        continue  # Skip the rest of the loop to restart the game

    # Check if the snake eats the apple
    if new_head == apple:
        snake.insert(0, new_head)  # Grow the snake
        apple = generate_apple()  # Spawn a new apple
    else:
        snake = [new_head] + snake[:-1]  # Normal movement

    time.sleep(0.5)
