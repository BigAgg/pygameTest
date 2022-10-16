# particles.py
import pygame

def circleSurf(size, color):
    surf = pygame.Surface((size*2, size*2))
    pygame.draw.circle(surf, color, (size, size), size)
    surf.set_colorkey((0,0,0))
    return surf

class particles():
    def __init__(self, size, lifespan, position, direction, speed, color, colorfade, light=False):
        self.size = size
        self.lifespan = lifespan
        self.position = pygame.Vector2(position)
        self.basePos = self.position
        self.direction = pygame.Vector2(direction)
        self.colorfade = colorfade
        self.speed = speed
        self.timeGone = 0
        self.isAlive = True
        self.surf = circleSurf(size, color)
        self.alpha = 100
        self.light = light
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
            self.lightCircle = circleSurf(size*2, (r, g, b))
            self.lightPos = (self.position.x - size, self.position.y - size)
    
    def draw(self, screen, delta):
        self.timeGone += delta
        if self.timeGone >= self.lifespan  or self.alpha <= 0:
            self.isAlive = False
            return
        if self.colorfade:
            self.alpha -= 1
            self.surf.set_alpha(self.alpha)
        if self.light:
            self.lightPos = (self.position.x - self.size, self.position.y - self.size)
            screen.blit(self.lightCircle, self.lightPos, special_flags=pygame.BLEND_RGB_ADD)
        screen.blit(self.surf, self.position)
        if self.direction:
            self.basePos += self.direction.normalize() * (self.speed * delta)
