# player.py
import pygame
from pygame.locals import *

import particles
import random


class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # base image size
        self.baseSize = 16
        # setting player values
        self.speed = 100
        self.position = pygame.Vector2(480, 270)
        self.velocity = pygame.Vector2()
        self.actualMousePos = pygame.Vector2(0, 0)
        # loading player image
        self.image = pygame.image.load("textures/Actor/Characters/DarkNinja/SpriteSheet.png").convert_alpha()
        # values for animation
        self.direction = 0
        self.lastPic = 0
        self.currentPic = 0
        # setting up player rect
        self.rect = self.image.get_rect()
        self.rect.w = self.baseSize
        self.rect.h = self.baseSize
        # cropRect for bliting the right image on screen
        self.cropRect = (0, 0, self.rect.w, self.rect.h)
        # particle array
        self.particles = []

    def ontick(self, delta, events):
        # called every frame
        self.getInput(events)
        # checking if movement happened, moving player
        if self.velocity:
            self.velocity.normalize()
            self.velocity = self.velocity * self.speed * delta
            self.position += self.velocity
            # animate player picture
            self.animate()
        else:
            self.cropRect = (self.direction * self.baseSize, 0, self.rect.w, self.rect.h)

    def draw(self, screen):
        # drawing all particles emitted by the player
        for particle in self.particles:
            particle.position = particle.basePos - (self.position - (478, 274))
            particle.draw(screen, 0.02)
            if not particle.isAlive:
                self.particles.remove(particle)
        # blit player on given screen
        screen.blit(self.image, self.rect, self.cropRect)

    def getInput(self, events):
        # setting velocity to 0
        self.velocity = pygame.Vector2()
        # get all the pressed keys
        pressed = pygame.key.get_pressed()
        # handle movement
        if pressed[pygame.K_w]:
            self.velocity.y -= 1
            self.direction = 1
        if pressed[pygame.K_s]:
            self.velocity.y += 1
            self.direction = 0
        if pressed[pygame.K_a]:
            self.velocity.x -= 1
            self.direction = 2
        if pressed[pygame.K_d]:
            self.velocity.x += 1
            self.direction = 3
        # getting just pressed keys here
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    for i in range(10000):
                        genPos = self.actualMousePos + (random.randint(-300, 300), random.randint(-300, 300))
                        cc = (random.randint(150, 255), random.randint(0, 255), 0)
                        testParticle = particles.particles(1, random.randint(10, 200) / 100, self.position, genPos, random.randint(1000, 2000) / 10, cc, random.randint(0, 1), random.randint(0, 1))
                        self.particles.append(testParticle)

    def animate(self):
        # getting if movement happend, animate player and generate footstep particles if true
        if pygame.time.get_ticks() - self.lastPic > 125:
            self.particles.append(particles.particles(2, random.randint(20, 25) / 10, (self.position[0] + random.randint(-3, 3), self.position[1] + random.randint(-2, 2)), (0, 0), 0, (60, 60, 60), True))
            self.currentPic += 1
            if self.currentPic > 3:
                self.currentPic = 0
            self.cropRect = (self.direction * self.baseSize, self.currentPic * self.baseSize, self.rect.w, self.rect.h)
            self.lastPic = pygame.time.get_ticks()
