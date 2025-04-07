import pygame
from constants import SCREEN_WIDTH, CASTLE_WIDTH, CASTLE_HEIGHT, GRAY, BLACK, GREEN, MONSTER_PATH_Y


class Castle:
    def __init__(self, hp=100):  # Теперь принимает HP как параметр
        self.hp = hp
        self.max_hp = hp
        self.width = CASTLE_WIDTH
        self.height = CASTLE_HEIGHT
        self.x = SCREEN_WIDTH - 50
        self.y = MONSTER_PATH_Y - 10

    def draw(self, surface):
        pygame.draw.rect(
            surface, GRAY, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, BLACK, (self.x, self.y - 20, self.width, 10))
        pygame.draw.rect(surface, GREEN,
                         (self.x, self.y - 20, self.width * (self.hp / self.max_hp), 10))
