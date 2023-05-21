import pygame
from paddle import Paddle
from ball import Ball
from score import Score

class PongEnvironment:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.paddle1 = Paddle(50, 250)  # No keys needed now
        self.paddle2 = Paddle(735, 250)
        self.ball = Ball(400, 300, 5, 5)
        self.score1 = Score(300, 50)
        self.score2 = Score(500, 50)
        self.PADDLE_SPEED = 10

    def reset(self):
        self.paddle1.reset()
        self.paddle2.reset()
        self.ball.reset()
        self.score1.reset()
        self.score2.reset()
        return self.get_state()

    def step(self, action):
        # Update paddle positions based on action
        self.paddle1.move(action[0]*self.PADDLE_SPEED)
        self.paddle2.move(action[1]*self.PADDLE_SPEED)

        # Update ball position
        score_player = self.ball.move()

        # Check for scoring
        if score_player == 1:
            self.score1.increment_score()
            self.ball.rect.center = (400, 300)  # Reset ball position
        elif score_player == 2:
            self.score2.increment_score()
            self.ball.rect.center = (400, 300)  # Reset ball position

        # Check for collisions
        self.ball.collide_with(self.paddle1)
        self.ball.collide_with(self.paddle2)

        # If a player reached a score of 11, the game is done
        done = self.score1.score == 11 or self.score2.score == 11
        reward = (self.score1.score, self.score2.score)

        return self.get_state(), reward, done

    def get_state(self):
        return (
            self.paddle1.rect.x, self.paddle1.rect.y,
            self.paddle2.rect.x, self.paddle2.rect.y,
            self.ball.rect.x, self.ball.rect.y,
            self.ball.dx, self.ball.dy,
        )