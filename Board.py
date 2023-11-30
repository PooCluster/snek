import pygame
from random import randint

class Board:
    def __init__(self, snek, surface, width = -1, height = -1):
        self.snek = snek
        self.surface = surface
        self.width = width
        self.height = height
        self.food = Board.produceFood(width, height)

    def produceFood(width, height):
        return (int(randint(0, width) / 16) * 16, int(randint(0, height) / 16) * 16)

    def update(self):
        # snek moves
        self.snek.update()

        # check/change board game state
        if not self.snek.getHead() == self.food:
            return
        self.snek.eat()
        self.food = Board.produceFood(self.width, self.height)

    def render(self):
        self.snek.render()
        pygame.draw.rect(self.surface, (255, 0, 0, 255), pygame.Rect(self.food[0], self.food[1], 16, 16))