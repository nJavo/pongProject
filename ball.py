
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
            # Colisión en el lado derecho del paddle cuando la bola se mueve hacia la derecha
            if self.x_speed > 0 and self.rect.right >= paddle.rect.left and self.rect.left < paddle.rect.left:
                self.rect.right = paddle.rect.left - 1  # Ajusta la posición de la bola justo a la izquierda del paddle
                self.x_speed = -self.x_speed

            # Colisión en el lado izquierdo del paddle cuando la bola se mueve hacia la izquierda
            elif self.x_speed < 0 and self.rect.left <= paddle.rect.right and self.rect.right > paddle.rect.right:
                self.rect.left = paddle.rect.right + 1  # Ajusta la posición de la bola justo a la derecha del paddle
                self.x_speed = -self.x_speed  

            # Colisión en la parte inferior del paddle cuando la bola se mueve hacia abajo
            if self.y_speed > 0 and self.rect.bottom >= paddle.rect.top and self.rect.top < paddle.rect.top:
                self.rect.bottom = paddle.rect.top - 1  # Ajusta la posición de la bola justo encima del paddle
                self.y_speed = -self.y_speed 
                self.x_speed = -self.x_speed

            # Colisión en la parte superior del paddle cuando la bola se mueve hacia arriba
            elif self.y_speed < 0 and self.rect.top <= paddle.rect.bottom and self.rect.bottom > paddle.rect.bottom:
                self.rect.top = paddle.rect.bottom + 1  # Ajusta la posición de la bola justo debajo del paddle
                self.y_speed = -self.y_speed  
                self.x_speed = -self.x_speed
            
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)