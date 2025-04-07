import pygame
from constants import TILE_SIZE, GRID_OFFSET_X, GRID_OFFSET_Y, BLACK


class Tile:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(
            GRID_OFFSET_X + x * TILE_SIZE,
            GRID_OFFSET_Y + y * TILE_SIZE,
            TILE_SIZE, TILE_SIZE
        )

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 1)

    def update_rect(self):
        self.rect = pygame.Rect(
            GRID_OFFSET_X + self.x * TILE_SIZE,
            GRID_OFFSET_Y + self.y * TILE_SIZE,
            TILE_SIZE, TILE_SIZE
        )
