import pygame
from paddle import Paddle

# Define the speed of the paddles
PADDLE_SPEED = 2

# Initialize Pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((800, 600))  # Assuming the width of the screen is 800

# Create two paddles with different control keys
paddle1 = Paddle(50, 250, pygame.K_w, pygame.K_s)  # Control with W and S
paddle2 = Paddle(735, 250, pygame.K_UP, pygame.K_DOWN)  # Control with UP and DOWN

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    paddle1.move(PADDLE_SPEED)
    paddle2.move(PADDLE_SPEED)
    
    screen.fill((0, 0, 0))  # Fill the screen with black
    paddle1.draw(screen)
    paddle2.draw(screen)
    pygame.display.flip()
    
pygame.quit()
