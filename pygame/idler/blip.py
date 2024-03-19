import pygame
from colors import * 
import random

class Blip():
    def __init__(self, size, x, y, action_cooldown_seconds, color):
        self.size = size
        self.x, self.y =  x, y
        self.action_cooldown = action_cooldown_seconds
        self.current_action_cooldown = self.action_cooldown
        self.valid_moves = set()
        self.color = color        

    def update(self, dt):
        self.current_action_cooldown -= dt
        if self.current_action_cooldown <= 0:
            self.move()
            self.current_action_cooldown = self.action_cooldown

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.size, self.size])

    def move(self):
        self.x, self.y = random.choice(list(self.valid_moves))

    def get_adjacent_cells(self):
        return {(self.x + self.size, self.y), 
                (self.x - self.size, self.y), 
                (self.x, self.y + self.size), 
                (self.x, self.y - self.size)}