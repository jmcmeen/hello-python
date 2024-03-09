import pygame
from colors import *
from grid import Grid

def start():
    # frame rate
    dt = 0 # delta time
    FPS = 240 # FPS

    # Grid
    grid = Grid(cell_size = 20, num_rows = 20, num_cols=20)

    # pygame setup
    pygame.init()
    pygame.display.set_caption("idler")
    screen = pygame.display.set_mode((grid.width, grid.height))

    # clock
    clock = pygame.time.Clock()
    running = True

    # game loop
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:
                    grid.idler.idler_movement_cooldown *= .9
                elif event.key == pygame.K_DOWN:
                    grid.idler.idler_movement_cooldown *= 1.1

        # update
        grid.update(dt)
        grid.draw(screen)

        # flip() the display to put your work on display.
        pygame.display.flip()

        # dt is delta time in seconds since last frame
        dt = clock.tick(FPS) / 1000

    # quit the game
    pygame.quit()
