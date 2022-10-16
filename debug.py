# debug.py
import pygame

pygame.font.init()
# font = pygame.font.Font("textures/HUD/Font/game.ttf", 50)
font = pygame.font.SysFont("arial.ttf", 25)


def debug(screen, content):
    if str(content) != "":
        textToRender = font.render(str(content), 1, (255, 255, 255))
        textRect = textToRender.get_rect()
        textRect.topleft = (0, 0)
        pygame.draw.rect(screen, "black", textRect)
        screen.blit(textToRender, textRect)
