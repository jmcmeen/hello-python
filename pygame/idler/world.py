from grid import Grid
from colors import black, white
from blip import Blip

class World:
    def __init__(self, cell_size, num_rows, num_cols):
        # create the grid
        self.grid = Grid(cell_size, num_rows, num_cols, render_lines=True)
        
        # create the blip
        self.blip = Blip(size=cell_size, 
            x = num_cols // 2 * cell_size,
            y = num_rows // 2 * cell_size,
            action_cooldown_seconds = 1,
            color = white)

    def update(self, dt):
        # make sure the blip only choses to move to valid cells
        self.blip.valid_moves = self.grid.cells.intersection(self.blip.get_adjacent_cells())
        
        # update the grid and blip
        self.blip.update(dt)
        self.grid.update(dt)

    def draw(self, screen):
        # the background
        screen.fill(black)

        # draw grid and blip
        self.grid.draw(screen)
        self.blip.draw(screen)
