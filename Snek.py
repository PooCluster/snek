import pygame
from enum import Enum

class Snek:
    # constant
    DEFAULT_LENGTH = 3

    class Direction(Enum):
        UP    = 0
        DOWN  = 1
        LEFT  = 2
        RIGHT = 3

    def __init__(self, surface, x = -1, y = -1):
        self.chain = []
        for i in range(Snek.DEFAULT_LENGTH):
            self.chain.append((x + (i * 16), y))
        self.surface = surface
        self.direction = Snek.Direction.LEFT
        self.eating = False
        self.dead = False

    def getHead(self):
        return (self.chain[0][0], self.chain[0][1])

    def eat(self):
        self.eating = True

    def kill(self):
        self.dead = True

    def isDead(self):
        return self.dead

    def posInChain(self, pos):
        return pos in self.chain

    def update(self):
        # we good?
        if self.dead:
            return

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
        newPos = (self.chain[0][0] + xChange, self.chain[0][1] + yChange)
        if self.posInChain(newPos):
            self.kill()
        self.chain.insert(0, newPos)

        # eat or remove tail
        if self.eating:
            self.eating = False
        else:
            self.chain.pop()

    def render(self):
        for snekNode in self.chain:
            pygame.draw.rect(self.surface, (0, 255, 0, 255), pygame.Rect(snekNode[0], snekNode[1], 16, 16))