import pygame
from idler import Idler
from colors import random_color, green, white, black

class Grid():
    def __init__(self, cell_size, num_rows, num_cols, render_lines=False):
        self.cell_size = cell_size
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.height = num_rows * cell_size
        self.width = num_cols * cell_size
        self.cells = {(x * cell_size, y * cell_size) for y in range(num_rows) for x in range(num_cols)}
        self.render = render_lines
        
        # Idler
        self.idler = Idler(size=cell_size, 
                x = self.num_cols // 2 * cell_size,
                y = self.num_rows // 2 * cell_size,
                movement_cooldown_seconds=1,
                color = white)

    def update(self, dt):
        self.idler.valid_moves = self.cells.intersection(self.idler.adjacent_cells)
        self.idler.update(dt)

    def draw(self, screen):
        screen.fill(black)

        if self.render:
            for x in range(0, self.width, self.cell_size):
                pygame.draw.line(screen, green, (x, 0), (x, self.height))
            for y in range(0, self.height, self.cell_size):
                pygame.draw.line(screen, green, (0, y), (self.width, y))

        self.idler.draw(screen)
