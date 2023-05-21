import pygame
from paddle import Paddle
from ball import Ball
from score import Score

# Initialize Pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((800, 600))  # Assuming the width of the screen is 800

# Create two paddles, a ball, and the scores
paddle1 = Paddle(50, 250, pygame.K_w, pygame.K_s)  # Control with W and S
paddle2 = Paddle(735, 250, pygame.K_UP, pygame.K_DOWN)  # Control with UP and DOWN
PADDLE_SPEED = 10
ball = Ball(400, 300, 5, 5)  # Assuming the initial position and speed
score1 = Score(300, 50)  # Assuming the position of the score display
score2 = Score(500, 50)  # Assuming the position of the score display

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # This will ensure the game runs at 60 frames per second
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    paddle1.move(PADDLE_SPEED)
    paddle2.move(PADDLE_SPEED)
    score_player = ball.move()
    if score_player == 1:
        score1.increment_score()
        ball.rect.center = (400, 300)  # Reset ball position
    elif score_player == 2:
        score2.increment_score()
        ball.rect.center = (400, 300)  # Reset ball position

    ball.collide_with(paddle1)
    ball.collide_with(paddle2)
    
    screen.fill((0, 0, 0))  # Fill the screen with black

    # Draw a middle line
    pygame.draw.line(screen, (255, 255, 255), (400, 0), (400, 600), 1)

    paddle1.draw(screen)
    paddle2.draw(screen)
    ball.draw(screen)
    score1.draw(screen)
    score2.draw(screen)
    pygame.display.flip()

pygame.quit()
