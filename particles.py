# particles.py
import pygame


def circleSurf(size, color):
    # setting up surface to draw circle on
    surf = pygame.Surface((size * 2, size * 2))
    # draw circle on surface
    pygame.draw.circle(surf, color, (size, size), size)
    # set the colorkey so the background is invisible
    surf.set_colorkey((0, 0, 0))
    return surf.convert_alpha()


class particles():
    def __init__(self, size, lifespan, position, direction, speed, color, colorfade=False, light=False):
        # setting all used variables
        self.lifespan = lifespan
        self.basePos = pygame.Vector2(position)
        self.direction = pygame.Vector2(direction)
        if self.direction:
            self.direction = self.direction.normalize()
        if colorfade:
            self.draw = self.colorfading
        self.speed = speed
        self.timeGone = 0
        self.isAlive = True
        self.surf = circleSurf(size, color)
        self.alpha = 100
        self.flags = 0

        # setting up light surface if wanted
        if light:
            r = color[0] - 220
            g = color[1] - 220
            b = color[2] - 220
            if r < 0:
                r = 0
                if color[0] > 30:
                    r = 20
            if g < 0:
                g = 0
                if color[1] > 30:
                    g = 20
            if b < 0:
                b = 0
                if color[2] > 30:
                    b = 20
            lightCircle = circleSurf(size * 2, (r, g, b))
            newSurf = pygame.Surface((size * 4, size * 4))
            newSurf.set_colorkey((0, 0, 0))
            newSurf.blit(lightCircle, (0, 0))
            newSurf.blit(self.surf, (0 + size, 0 + size))
            self.surf = newSurf
            self.flags = pygame.BLEND_RGB_ADD

    def draw(self, screen: pygame.Surface, delta):
        # adding the time of the last frame to a total time
        self.timeGone += delta
        # killing itself
        if self.timeGone >= self.lifespan or self.alpha <= 0:
            self.isAlive = False
            return
        screen.blit(self.surf, self.position, special_flags=self.flags)
        self.basePos += self.direction * (self.speed * delta)

    def colorfading(self, screen, delta):
        self.timeGone += delta
        if self.timeGone >= self.lifespan or self.alpha <= 0:
            self.isAlive = False
            return
        self.alpha -= 100 / (self.lifespan / delta)
        self.surf.set_alpha(self.alpha)
        screen.blit(self.surf, self.position, special_flags=self.flags)
        self.basePos += self.direction * (self.speed * delta)
