# main.py
import pygame
import sys
import time
import random
import threading

import debug
import player
import particles


class framework:
    def __init__(self):
        pygame.init()
        windowSize, fullscreen = self._loadSettings()
        self.windowSize = windowSize
        if fullscreen:
            self.screen = pygame.display.set_mode(windowSize, pygame.FULLSCREEN | pygame.DOUBLEBUF)
            self.windowSize = self.screen.get_size()
        else:
            self.screen = pygame.display.set_mode(windowSize, pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        self.hw = windowSize[0] / 2
        self.hh = windowSize[1] / 2
        self.visibleOnScreen = pygame.sprite.Group()
        self.allSprites = pygame.sprite.Group()
        self.chunks = pygame.sprite.Group()
        self.particles = []
        self.display = pygame.Surface((960, 540))
        self.debugging = ""

    def _loadSettings(self):
        windowSize = (1920, 1080)
        fullscreen = 0
        with open("bin/settings.ini", mode="r", encoding="utf-8") as file:
            for i in file.readlines():
                tmp = i.replace("\n", "")
                if tmp.startswith("FULLSCREEN="):
                    if tmp.replace("FULLSCREEN=", "") == "1":
                        fullscreen = 1
                elif tmp.startswith("RESOLUTION="):
                    tmp = tmp.replace("RESOLUTION=", "")
                    tmpArr = tmp.split(",")
                    windowSize = (int(tmpArr[0]), int(tmpArr[1]))
        return windowSize, fullscreen

    def mainMenu(self):
        pass

    def run(self):
        running = 1
        clock = self.clock
        delta = 0
        lastTick = 0
        self.p = player.player()
        self.p.rect.center = (480, 270)
        while running:
            delta = time.time() - lastTick        # calculating deltaTime
            lastTick = time.time()

            self.debugging = int(clock.get_fps())

            self.handleInput(delta)      # Handle user-inputs
            self.p.ontick(delta)
            self.handleCollision()      # Handle collisions
            self.render()       # render everything to screen

            pygame.display.update()     # updating screen
            clock.tick(60)      # setting framerate

    def handleInput(self, delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_SPACE]:
                    for i in range(5000):
                        testParticle = particles.particles(1, random.randint(30, 300), (random.randint(-10, 10), random.randint(-10, 10)), (float(random.randint(-100, 100) / 10), float(random.randint(-100, 100) / 10)), random.randint(10, 100) / 10, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), random.randint(0, 1))
                        self.particles.append(testParticle)

    def handleCollision(self):
        pass

    def render(self):
        self.display.fill("grey")
        self.visibleOnScreen.draw(self.display)
        self.p.draw(self.display)
        for particle in self.particles:
            particle.position = particle.basePos - self.p.position
            particle.draw(self.display)
            if not particle.isAlive:
                self.particles.remove(particle)
        surf = pygame.transform.scale(self.display, self.windowSize)
        self.screen.blit(surf, (0, 0))
        debug.debug(self.screen, self.debugging)


def main():
    game = framework()
    game.run()


if __name__ == "__main__":
    main()
