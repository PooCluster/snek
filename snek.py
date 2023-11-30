import pygame

class Snek:
    class SnekNode:
        def __init__(self, x, y):
            self.pos = (x, y)

    def __init__(self, x = -1, y = -1):
        self.chain = [                  \
            Snek.SnekNode(x, y),        \
            Snek.SnekNode(x + 1, y),    \
            Snek.SnekNode(x + 1, y + 1) \
        ]

    def update(self):
        # TODO
        print("TODO")

    def render(self):
        # TODO
        for snekNode in self.chain:
            surface = pygame.Surface([16, 16])
            pygame.Surface.fill(surface, (0, 255, 0))