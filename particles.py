# particles.py
import pygame

class particles():
    def __init__(self, size, lifespan, position, direction, speed, color, colorfade):
        self.size = size
        self.lifespan = lifespan
        self.position = pygame.Vector2(position)
        self.basePos = self.position
        self.direction = pygame.Vector2(direction)
        self.colorfade = colorfade
        self.speed = speed
        self.color = color
        self.timeGone = 0
        self.isAlive = True
        self.highestColor = 0
        for col in color:
            if col > self.highestColor:
                self.highestColor = col
    
    def draw(self, screen):
        self.timeGone += 1
        if self.timeGone >= self.lifespan or self.highestColor <= 0:
            self.isAlive = False
            return
        if self.colorfade:
            r = self.color[0] - 1
            if r < 0:
                r = 0
            g = self.color[1] - 1
            if g < 0:
                g = 0
            b = self.color[2] - 1
            if b < 0:
                b = 0
            self.color = (r, g, b)
            self.highestColor -= 1
        pygame.draw.circle(screen, self.color, self.position, self.size)
        if self.direction:
            self.basePos += self.direction.normalize() * self.speed
