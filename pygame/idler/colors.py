import random

# color tuples
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
purple = (255, 0, 255)
orange = (255, 165, 0)

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))