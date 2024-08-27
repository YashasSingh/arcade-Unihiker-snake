from unihiker import GUI
import time

# Initialize GUI
gui = GUI()

# Set up the grid size
GRID_SIZE = 20
WIDTH = gui.width() // GRID_SIZE
HEIGHT = gui.height() // GRID_SIZE

# Initial snake setup
snake = [(5, 5), (4, 5), (3, 5)]
direction = (1, 0)  # Moving right initially

def draw_snake():
    gui.clear()  # Clear the screen
    for segment in snake:
        x, y = segment
        gui.draw_rectangle(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE, fill="green")
    gui.show()

# Main loop
while True:
    draw_snake()
    # Move the snake by updating the position
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake = [new_head] + snake[:-1]
    time.sleep(0.5)
