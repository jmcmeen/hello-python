import pygame
from colors import *
from grid import Grid
from world import World

def start():
    # frame rate
    dt = 0 # delta time
    FPS = 240 # FPS

    # World
    world = World(cell_size = 25, num_rows = 25, num_cols=40)

    # pygame setup
    pygame.init()
    pygame.display.set_caption("idler")
    screen = pygame.display.set_mode((world.grid.width, world.grid.height))

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
                    world.blip.action_cooldown *= .9
                elif event.key == pygame.K_DOWN:
                    world.blip.action_cooldown *= 1.1
                elif event.key == pygame.K_SPACE:
                    world.grid.toggle_lines()

        # update
        world.update(dt)
        world.draw(screen)

        # flip() the display to put your work on display.
        pygame.display.flip()

        # dt is delta time in seconds since last frame
        dt = clock.tick(FPS) / 1000

    # quit the game
    pygame.quit()
