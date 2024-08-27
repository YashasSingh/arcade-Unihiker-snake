from unihiker import GUI
import time
import random

# Initialize GUI
gui = GUI()

# Set up the grid size
GRID_SIZE = 20
WIDTH = gui.width() // GRID_SIZE
HEIGHT = gui.height() // GRID_SIZE

# Initial snake setup
snake = [(5, 5), (4, 5), (3, 5)]
direction = (1, 0)  # Moving right initially

# Generate random apple position
def generate_apple():
    while True:
        apple = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
        if apple not in snake:
            return apple

apple = generate_apple()

def draw_snake():
    gui.clear()  # Clear the screen
    # Draw the snake
    for segment in snake:
        x, y = segment
        gui.draw_rectangle(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE, fill="green")
    
    # Draw the apple
    gui.draw_rectangle(apple[0] * GRID_SIZE, apple[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE, fill="red")
    
    gui.show()

# Main loop
while True:
    draw_snake()

    # Move the snake by updating the position
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Check if the snake eats the apple
    if new_head == apple:
        snake.insert(0, new_head)  # Grow the snake
        apple = generate_apple()  # Spawn a new apple
    else:
        snake = [new_head] + snake[:-1]  # Normal movement

    time.sleep(0.5)
