# simple little aim trainer for pygame

import pygame
import random

# Initialize pygame
pygame.init()

# Circle properties
circle_radius = 50
x_velocity = 750
y_velocity = 750
dt = 0

# Colors
RED = (255, 0, 0)

#set up colors
colors = [(x,y,z) for x in range(50, 256) for y in range(50, 256) for z in range(50, 256)]

# Set up the screen and clock
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Aim Trainer")
clock = pygame.time.Clock()

info = pygame.display.Info() # You have to call this before pygame.display.set_mode()
screen_width,screen_height = info.current_w,info.current_h

# Initialize circle properties
circle_x = random.randint(circle_radius, screen_width - circle_radius)
circle_y = random.randint(circle_radius, screen_height - circle_radius)
circle_dx = random.randint(-x_velocity, x_velocity)
circle_dy = random.randint(-y_velocity, y_velocity)
circle_color = random.choice(colors)
running = True

while running:
    # file the screen with black
    screen.fill((0, 0, 0))

    # Draw the circle
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

    # Move the circle
    circle_x += circle_dx * dt
    circle_y += circle_dy * dt

    # Check for X axis wall collision
    if circle_x - circle_radius <= 0 or circle_x + circle_radius >= screen_width:
        circle_dx = -circle_dx

    # Check for y axis wall collision
    if circle_y - circle_radius <= 0 or circle_y + circle_radius >= screen_height:
        circle_dy = -circle_dy

    # Check for events
    for event in pygame.event.get():
        # Check for closing the window
        if event.type == pygame.QUIT:
            running = False
        # Check for key presses
        elif event.type == pygame.KEYDOWN:
            # Check for escape key
            if event.key == pygame.K_ESCAPE:
                running = False
            # Check for left button, decrease circle radius
            elif event.key == pygame.K_LEFT:
                if circle_radius > 10:
                    circle_radius -= 5
            # Check for right button, increase circle radius
            elif event.key == pygame.K_RIGHT:
                if circle_radius < 100:
                    circle_radius += 5
        # check for mouse button presses
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance = ((mouse_x - circle_x) ** 2 + (mouse_y - circle_y) ** 2) ** 0.5
            if distance <= circle_radius:
                circle_x = random.randint(circle_radius, screen_width - circle_radius)
                circle_y = random.randint(circle_radius, screen_height - circle_radius)
                circle_dx = random.randint(-x_velocity, x_velocity)
                circle_dy = random.randint(-y_velocity, y_velocity)
                circle_color = random.choice(colors)

    pygame.display.flip()
    dt = clock.tick(240) / 1000

pygame.quit()
