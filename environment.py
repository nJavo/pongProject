import numpy as np
import pygame

from paddle import Paddle
from ball import Ball

class PongEnvironment:
    def __init__(self, screen):
        self.screen = screen
        self.paddle1 = Paddle(50, 250, pygame.K_w, pygame.K_s)  # Control with W and S
        self.paddle2 = Paddle(735, 250, pygame.K_UP, pygame.K_DOWN)  # Control with UP and DOWN
        self.PADDLE_SPEED = 10
        self.ball = Ball(400, 300, 5, 5)  # Assuming the initial position and speed
        self.score1 = 0
        self.score2 = 0

    def get_state(self):
        # Current simplified state space: positions of two paddles and the ball
        return np.array([self.paddle1.rect.y, self.paddle2.rect.y, self.ball.rect.x, self.ball.rect.y])

    def reset(self):
        # Reset the game state to the initial state
        self.paddle1.rect.y = 250
        self.paddle2.rect.y = 250
        self.ball.rect.x = 400
        self.ball.rect.y = 300
        self.score1 = 0
        self.score2 = 0
        return self.get_state()

    def step(self, action1, action2):
        # 1 is move up, 2 is move down, 0 is do nothing
        if action1 == 1:
            self.paddle1.move(-self.PADDLE_SPEED)
        elif action1 == 2:
            self.paddle1.move(self.PADDLE_SPEED)

        if action2 == 1:
            self.paddle2.move(-self.PADDLE_SPEED)
        elif action2 == 2:
            self.paddle2.move(self.PADDLE_SPEED)
        
        score_player = self.ball.move()
        if score_player == 1:
            self.score1 += 1
            self.ball.rect.center = (400, 300)  # Reset ball position
        elif score_player == 2:
            self.score2 += 1
            self.ball.rect.center = (400, 300)  # Reset ball position

        self.ball.collide_with(self.paddle1)
        self.ball.collide_with(self.paddle2)

        # The reward is the difference in scores
        reward = self.score1 - self.score2
        # The game is done if a player has 11 points
        done = self.score1 >= 11 or self.score2 >= 11
        return self.get_state(), reward, done

    def render(self):
        self.screen.fill((0, 0, 0))  # Fill the screen with black
        # Draw a middle line
        pygame.draw.line(self.screen, (255, 255, 255), (400, 0), (400, 600), 1)
        self.paddle1.draw(self.screen)
        self.paddle2.draw(self.screen)
        self.ball.draw(self.screen)
        pygame.display.flip()