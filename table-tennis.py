import pygame  # must be installed first
import random

# Initialize Pygame
pygame.init()

# Define colors for easy reference
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)

# Set up the game display dimensions
width = 800
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Table Tennis Game')

# Paddle properties
paddle_width = 15  # Width of the paddles
paddle_height = 100  # Height of the paddles
paddle_speed = 10  # Speed at which paddles move

# Ball properties
ball_size = 15  # Diameter of the ball
ball_speed_x = 5  # Horizontal speed of the ball
ball_speed_y = 5  # Vertical speed of the ball

# Initialize paddle positions (centered vertically)
left_paddle_y = height // 2 - paddle_height // 2
right_paddle_y = height // 2 - paddle_height // 2

# Initialize ball position (centered on the screen)
ball_x = width // 2 - ball_size // 2
ball_y = height // 2 - ball_size // 2

# Main game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the game loop if the window is closed

    # Get the current state of all keys
    keys = pygame.key.get_pressed()

    # Left paddle movement (Player 1)
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed  # Move up
    if keys[pygame.K_s] and left_paddle_y < height - paddle_height:
        left_paddle_y += paddle_speed  # Move down

    # Right paddle movement (Player 2)
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed  # Move up
    if keys[pygame.K_DOWN] and right_paddle_y < height - paddle_height:
        right_paddle_y += paddle_speed  # Move down

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with the top and bottom edges
    if ball_y <= 0 or ball_y >= height - ball_size:
        ball_speed_y *= -1  # Reverse vertical direction

    # Ball collision with the paddles
    if (ball_x <= paddle_width and left_paddle_y < ball_y < left_paddle_y + paddle_height) or \
       (ball_x >= width - paddle_width - ball_size and right_paddle_y < ball_y < right_paddle_y + paddle_height):
        ball_speed_x *= -1  # Reverse horizontal direction

    # Check if the ball goes out of bounds (left or right)
    if ball_x <= 0 or ball_x >= width - ball_size:
        # Reset ball to the center
        ball_x, ball_y = width // 2 - ball_size // 2, height // 2 - ball_size // 2
        # Randomize ball's initial horizontal direction
        ball_speed_x *= random.choice([-1, 1])

    # Fill the screen with black (clear previous frame)
    display.fill(black)

    # Draw the left paddle (Player 1)
    pygame.draw.rect(display, white, [0, left_paddle_y, paddle_width, paddle_height])

    # Draw the right paddle (Player 2)
    pygame.draw.rect(display, white, [width - paddle_width, right_paddle_y, paddle_width, paddle_height])

    # Draw the ball
    pygame.draw.ellipse(display, red, [ball_x, ball_y, ball_size, ball_size])

    # Update the display with the new frame
    pygame.display.update()

    # Control the game's frame rate (60 frames per second)
    clock = pygame.time.Clock()
    clock.tick(60)

# Quit Pygame when the game loop ends
pygame.quit()
