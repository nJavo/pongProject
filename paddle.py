import pygame

PADDLE_WIDTH, PADDLE_HEIGHT = 15, 80
WHITE = (255, 255, 255)

class Paddle:
    def __init__(self, x, y, up_key, down_key):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.up_key = up_key
        self.down_key = down_key
        
    def move(self, speed):
        keys = pygame.key.get_pressed()
        if keys[self.up_key]:
            self.rect.move_ip(0, speed)
        elif keys[self.down_key]:
            self.rect.move_ip(0, -speed)
        
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:  # Assuming the height of the screen is 600
            self.rect.bottom = 600
            
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)