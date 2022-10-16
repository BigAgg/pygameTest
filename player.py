# player.py
import pygame


class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.baseSize = 16
        self.velocity = pygame.Vector2()
        self.direction = pygame.Vector2()
        self.speed = 100
        self.position = (0, 0)
        self.image = pygame.image.load("textures/Actor/Characters/DarkNinja/SpriteSheet.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.w = self.baseSize
        self.rect.h = self.baseSize
        self.cropRect = (0, 0, self.rect.w, self.rect.h)
        self.lastPic = 0
        self.currentPic = 0
        self.direction = 0

    def ontick(self, delta):
        self.getInput()
        if self.velocity:
            self.velocity.normalize()
            self.position += self.velocity * self.speed * delta
            self.animate()
        else:
            self.cropRect = (self.direction * self.baseSize, 0, self.rect.w, self.rect.h)

    def draw(self, screen):
        screen.blit(self.image, self.rect, self.cropRect)

    def getInput(self):
        self.velocity = pygame.Vector2()
        pressed = pygame.key.get_pressed()
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

    def animate(self):
        if pygame.time.get_ticks() - self.lastPic > 150:
            self.currentPic += 1
            if self.currentPic > 3:
                self.currentPic = 0
            self.cropRect = (self.direction * self.baseSize, self.currentPic * self.baseSize, self.rect.w, self.rect.h)
            self.lastPic = pygame.time.get_ticks()
