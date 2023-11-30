import pygame
import Snek
from OpenGL.GL import *

# Engine is a static class responsible for running the core infra of the game.
class Engine:
    # constants
    TITLE = "snek"
    WIDTH = 400
    HEIGHT = WIDTH / 16 * 9
    SCALE = 3
    FPS = 60.

    # static variables
    running = False
    __upsCounter = 0
    __fpsCounter = 0

    def initialize():
        pygame.init()
        # set_mode(pos tuple, flags: OpenGL and double buffer rendering
        pygame.display.set_mode((Engine.WIDTH, Engine.HEIGHT), \
                                pygame.OPENGL|pygame.DOUBLEBUF)
        pygame.display.set_caption(Engine.TITLE)

        Engine.snek = Snek.Snek(Engine.WIDTH / 2, Engine.HEIGHT / 2)

        Engine.running = True
        return Engine.running

    def __update():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Engine.running = False
        # TODO

    def __render():
        glClearColor(1, 1, 1, 1) # RGBA
        glClear(GL_COLOR_BUFFER_BIT)

        # TODO: game rendering stuff here
        Engine.snek.render()

        # swap to other buffer
        pygame.display.flip()

    def gameLoop():
        time = pygame.time.get_ticks()
        previousTime = time
        interval = 1000. / Engine.FPS
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
                # TODO: 1 second has past, update display
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