import pygame

WHITE = (255, 255, 255)

class Score:
    def __init__(self, x, y, font_size=70):
        self.score = 0
        self.font = pygame.font.Font(None, font_size)
        self.x = x
        self.y = y

    def increment_score(self):
        self.score += 1

    def draw(self, screen):
        score_text = self.font.render(str(self.score), True, WHITE)
        screen.blit(score_text, (self.x, self.y))