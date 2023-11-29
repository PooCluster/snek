import pygame
from OpenGL.GL import *

# Engine is a static class responsible for running the core infra of the game.
class Engine:
    # constants
    TITLE = "SNEK"
    WIDTH = 400
    HEIGHT = WIDTH / 16 * 9
    SCALE = 3
    FPS = 60.

    # static variables
    running = False
    upsCounter = 0
    fpsCounter = 0

    def initialize():
        pygame.init()
        # set_mode(pos tuple, flags: OpenGL and double buffer rendering
        pygame.display.set_mode((Engine.WIDTH, Engine.HEIGHT),
                                pygame.OPENGL|pygame.DOUBLEBUF)

        Engine.running = True
        return Engine.running

    def update():
        for event in pygame.event.get():
                if event.type == pygame.quit:
                    Engine.running = False
        # TODO

    def render():
        glClearColor(1, 1, 1, 1) # RGBA
        glClear(GL_COLOR_BUFFER_BIT)

        # TODO: game rendering stuff here

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
                Engine.update()
                Engine.upsCounter += 1
                difference -= 1.
            Engine.render()
            Engine.fpsCounter += 1
            if currentTime - time >= 1000:
                # TODO: 1 second has past, update display
                time += 1000
                info = str(Engine.fpsCounter) + " FPS " + str(Engine.upsCounter) + " UPS"
                print(Engine.TITLE + " | " + info)
                Engine.upsCounter = 0
                Engine.fpsCounter = 0

def main():
    if not Engine.initialize():
        print("Game failed to init. :(")
        return
    Engine.gameLoop()

main()