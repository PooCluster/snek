import pygame
from random import randint

class Board:
    def __init__(self, snek, surface, width = -1, height = -1):
        self.snek = snek
        self.surface = surface
        self.width = width
        self.height = height
        self.food = Board.produceFood(self, width, height)

    def produceFood(self, width, height):
        # [0 : width|height)
        width -= 1
        height -= 1
        newPos = (int(randint(0, width) / 16) * 16, int(randint(0, height) / 16) * 16)
        while self.snek.posInChain(newPos):
            newPos = (int(randint(0, width) / 16) * 16, int(randint(0, height) / 16) * 16)
        return newPos

    def gameOver(self):
        return self.snek.isDead()

    def update(self):
        if self.snek.isDead():
            return

        # snek moves
        self.snek.update()

        # out of boundaries?
        snekX = self.snek.getHead()[0]
        snekY = self.snek.getHead()[1]
        if snekX < 0 or snekX >= self.width or snekY < 0 or snekY >= self.height:
            self.snek.kill()

        # eating logic
        if not self.snek.getHead() == self.food:
            return
        self.snek.eat()
        self.food = self.produceFood(self.width, self.height)

    def render(self):
        self.snek.render()
        pygame.draw.rect(self.surface, (255, 0, 0, 255), pygame.Rect(self.food[0], self.food[1], 16, 16))