import pygame
from enum import Enum

class Snek:
    class Direction(Enum):
        UP    = 0
        DOWN  = 1
        LEFT  = 2
        RIGHT = 3

    class SnekNode:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    def __init__(self, surface, x = -1, y = -1):
        self.chain = [                \
            Snek.SnekNode(x, y),      \
            Snek.SnekNode(x + 16, y), \
            Snek.SnekNode(x + 32, y)  \
        ]
        self.surface = surface
        self.direction = Snek.Direction.LEFT

    def update(self):
        # read direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and not self.direction == Snek.Direction.DOWN:
            self.direction = Snek.Direction.UP
        if keys[pygame.K_DOWN] and not self.direction == Snek.Direction.UP:
            self.direction = Snek.Direction.DOWN
        if keys[pygame.K_LEFT] and not self.direction == Snek.Direction.RIGHT:
            self.direction = Snek.Direction.LEFT
        if keys[pygame.K_RIGHT] and not self.direction == Snek.Direction.LEFT:
            self.direction = Snek.Direction.RIGHT

        # calculate translations (origin is based on top-left)
        xChange = 0
        yChange = 0
        if self.direction == Snek.Direction.UP:
            yChange -= 16
        if self.direction == Snek.Direction.DOWN:
            yChange += 16
        if self.direction == Snek.Direction.LEFT:
            xChange -= 16
        if self.direction == Snek.Direction.RIGHT:
            xChange += 16

        # move head to new location
        self.chain.insert(0, Snek.SnekNode(self.chain[0].x + xChange, self.chain[0].y + yChange))
        # remove tail
        self.chain.pop()

    def render(self):
        for snekNode in self.chain:
            pygame.draw.rect(self.surface, (0, 255, 0, 255), pygame.Rect(snekNode.x, snekNode.y, 16, 16))