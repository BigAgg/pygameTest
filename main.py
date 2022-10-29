# main.py
import pygame
from pygame.locals import *
import sys
import time
import random

import debug
import player
import particles
import tiles


class framework:
    def __init__(self):
        pygame.init()       # initializing pygame
        windowSize, fullscreen = self._loadSettings()       # getting saved settings
        self.windowSize = windowSize

        # setting up window
        if fullscreen:
            self.screen = pygame.display.set_mode(
                windowSize, FULLSCREEN | DOUBLEBUF)
            self.windowSize = self.screen.get_size()
        else:
            self.screen = pygame.display.set_mode(windowSize, DOUBLEBUF)
        pygame.display.set_caption("TestGame")

        # settings used for rendering and stuff
        self.hw = windowSize[0] / 2
        self.hh = windowSize[1] / 2
        self.visibleOnScreen = pygame.sprite.Group()
        self.allSprites = pygame.sprite.Group()
        self.chunks = pygame.sprite.Group()
        self.particles = []
        # visible display everything is rendered on
        self.display = pygame.Surface((960, 540))
        self.clippingRect = pygame.Rect(0, 0, windowSize[0], windowSize[1])
        self.debugging = ""
        tiles.initialize()

    def _loadSettings(self):
        # setting default settings
        windowSize = (1920, 1080)
        fullscreen = 0

        # loading settings from file
        with open("bin/settings.ini", mode="r", encoding="utf-8") as file:
            for i in file.readlines():
                tmp = i.replace("\n", "")
                if tmp.startswith("FULLSCREEN="):       # getting fullscreen setting
                    if tmp.replace("FULLSCREEN=", "") == "1":
                        fullscreen = 1
                elif tmp.startswith("RESOLUTION="):     # getting saved resolution
                    tmp = tmp.replace("RESOLUTION=", "")
                    tmpArr = tmp.split(",")
                    windowSize = (int(tmpArr[0]), int(tmpArr[1]))
        return windowSize, fullscreen       # returning all settings

    def mainMenu(self):
        pass

    def run(self):
        # setting base variables
        running = 1
        clock = pygame.time.Clock()
        delta = 0
        lastTick = 0
        mouseScale = (960 / self.windowSize[0], 540 / self.windowSize[1])
        self.p = player.player()
        self.p.rect.center = (480, 270)
        self.p.position = pygame.Vector2(self.hw, self.hh)

        # main loop ---------------------------------------------------- #
        while running:
            delta = time.time() - lastTick        # calculating deltaTime
            lastTick = time.time()

            mousePos = pygame.mouse.get_pos()       # mouse pos on screen surface
            # actual mouse position on display surface not screen surface
            mousePos = (mousePos[0] * mouseScale[0],
                        mousePos[1] * mouseScale[1])

            # sending player the actual mouse position according to its position
            self.p.actualMousePos.x = (mousePos[0] - 480.0) * 10
            self.p.actualMousePos.y = (mousePos[1] - 270.0) * 10

            self.debugging = int(clock.get_fps())
            events = pygame.event.get()
            self.handleInput(delta, events)      # Handle user-inputs
            self.p.ontick(delta, events)
            self.handleCollision()      # Handle collisions
            self.render(delta)       # render everything to screen

            pygame.display.update(self.clippingRect)     # updating screen
            clock.tick(60)      # setting framerate
        # main loop end ------------------------------------------------ #
        pygame.quit()
        sys.exit()

    def handleInput(self, delta, events):
        # check window events for input
        for event in events:
            # inputs for closing the game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def handleCollision(self):
        pass

    def render(self, delta):
        self.display.fill((100, 100, 100))      # resetting window
        self.visibleOnScreen.draw(self.display)
        idx = 0
        for tile in tiles.allTextures:
            t = tiles.allTextures.get(tile)
            if t and t.tileset == "element":
                t.position = (idx * 16 + 20 + t.srcR.size[0] / 2, 150)
                idx += t.srcR.size[0] / 16
                t.update(self.p.velocity)
                t.draw(self.display)

        self.p.draw(self.display)

        # drawing all the particles
        for particle in self.particles:
            particle.position = particle.basePos - self.p.position
            particle.draw(self.display, delta)
            if not particle.isAlive:
                self.particles.remove(particle)
                del particle

        # scaling the display surface to window size
        surf = pygame.transform.scale(self.display, self.windowSize)
        self.screen.blit(surf, (0, 0))      # bliting everything to screen
        debug.debug(self.screen, self.debugging)


def main():
    game = framework()
    game.run()


if __name__ == "__main__":
    main()
