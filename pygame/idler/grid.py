import pygame
from blip import Blip
from colors import random_color, green, white, black

class Grid():
    def __init__(self, cell_size, num_rows, num_cols, render_lines=False):
        self.cell_size = cell_size
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.height = num_rows * cell_size
        self.width = num_cols * cell_size
        self.render_lines = render_lines
        self.cells = {(x * cell_size, y * cell_size) for y in range(num_rows) for x in range(num_cols)}


    def update(self, dt):
        pass

    def draw(self, screen):
        if self.render_lines:
            for x in range(0, self.width, self.cell_size):
                pygame.draw.line(screen, green, (x, 0), (x, self.height))
            for y in range(0, self.height, self.cell_size):
                pygame.draw.line(screen, green, (0, y), (self.width, y))

    def toggle_lines(self):
        self.render_lines = not self.render_lines
