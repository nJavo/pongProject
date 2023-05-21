
import pygame

BALL_WIDTH, BALL_HEIGHT = 10, 10
WHITE = (255, 255, 255)

class Ball:
    def __init__(self, x, y, x_speed, y_speed):
        self.rect = pygame.Rect(x, y, BALL_WIDTH, BALL_HEIGHT)
        self.x_speed = x_speed
        self.y_speed = y_speed

    def move(self):
        self.rect.move_ip(self.x_speed, self.y_speed)
        
        # If the ball hits the top or the bottom of the screen, change the y direction
        if self.rect.top < 0 or self.rect.bottom > 600:
            self.y_speed = -self.y_speed
        # If the ball goes past the left or right side of the screen, a player scores
        elif self.rect.left < 0:
            return 2  # Player 2 scores
        elif self.rect.right > 800:
            return 1  # Player 1 scores
            
    def collide_with(self, paddle):
        if self.rect.colliderect(paddle.rect):
            self.x_speed = -self.x_speed
            self.y_speed = -self.y_speed
            
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)