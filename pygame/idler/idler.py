import pygame
from colors import * 
import random

class Idler():
    def __init__(self, size, x, y, movement_cooldown_seconds, color):
        self.size = size
        self.x, self.y =  x, y
        self.idler_movement_cooldown = movement_cooldown_seconds
        self.current_movement_cooldown = self.idler_movement_cooldown
        self.visited_cells = set()
        self.adjacent_cells = {(self.x + self.size, self.y), 
                               (self.x - self.size, self.y), 
                               (self.x, self.y + self.size), 
                               (self.x, self.y - self.size)}
        self.valid_moves = set()
        self.color = color        
        self.move_history = []

    def update(self, dt):
        self.current_movement_cooldown -= dt
        if self.current_movement_cooldown <= 0:
            self.move()
            self.current_movement_cooldown = self.idler_movement_cooldown

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.size, self.size])

    def move(self):
        new_x, new_y = random.choice(list(self.valid_moves))
       
        if new_x > self.x:
            self.move_history.append("r")
        elif new_x < self.x:
            self.move_history.append("l")
        elif new_y > self.y:
            self.move_history.append("d")
        elif new_y < self.y:
            self.move_history.append("u")

        self.x, self.y = new_x, new_y

        self.visited_cells.add((self.x, self.y))
        self.adjacent_cells = {(self.x + self.size, self.y), 
                               (self.x - self.size, self.y), 
                               (self.x, self.y + self.size), 
                               (self.x, self.y - self.size)}

