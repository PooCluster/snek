import pygame
from Board import Board
from Snek import Snek

# Engine is a static class responsible for running the core infra of the game.
class Engine:
    # constants
    TITLE = "snek"
    WIDTH = 400
    HEIGHT = 224
    SCALE = 3
    UPS = 2.

    # static variables
    board = None
    snek = None
    surface = None
    running = False
    __upsCounter = 0
    __fpsCounter = 0

    def initialize():
        pygame.init()
        Engine.surface = pygame.display.set_mode((Engine.WIDTH, Engine.HEIGHT), \
                                                 pygame.DOUBLEBUF)

        pygame.display.set_caption(Engine.TITLE)

        Engine.snek = Snek(Engine.surface, \
                           int((Engine.WIDTH / 2) / 16) * 16, int((Engine.HEIGHT / 2) / 16) * 16)
        Engine.board = Board(Engine.snek, Engine.surface, Engine.WIDTH, Engine.HEIGHT)

        Engine.running = True
        return Engine.running

    def __update():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Engine.running = False
        Engine.board.update()
        if Engine.board.gameOver():
            Engine.snek = Snek(Engine.surface, \
                               int((Engine.WIDTH / 2) / 16) * 16, int((Engine.HEIGHT / 2) / 16) * 16)
            Engine.board = Board(Engine.snek, Engine.surface, Engine.WIDTH, Engine.HEIGHT)

    def __render():
        Engine.surface.fill((0, 0, 0))

        # TODO: game rendering stuff here
        Engine.board.render()

        # update and swap to other buffer
        pygame.display.flip()

    def gameLoop():
        time = pygame.time.get_ticks()
        previousTime = time
        interval = 1000. / Engine.UPS
        difference = 0.
        while Engine.running:
            currentTime = pygame.time.get_ticks()
            difference += (currentTime - previousTime) / interval
            previousTime = currentTime
            while difference >= 1.:
                Engine.__update()
                Engine.__upsCounter += 1
                difference -= 1.
            Engine.__render()
            Engine.__fpsCounter += 1
            if currentTime - time >= 1000:
                # 1 second has past, update display
                time += 1000
                info = str(Engine.__fpsCounter) + " FPS " + \
                       str(Engine.__upsCounter) + " UPS"
                pygame.display.set_caption(Engine.TITLE + " | " + info)
                Engine.__upsCounter = 0
                Engine.__fpsCounter = 0
        # game over
        pygame.display.quit()
        pygame.quit()

def main():
    if not Engine.initialize():
        print("Game failed to init. :(")
        return
    Engine.gameLoop()

main()