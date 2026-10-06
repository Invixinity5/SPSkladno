import pygame
import random
from Settings import *
class Blok(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        x = random.randrange(0 + (BLOK_WIDTH//2),WIDTH - (BLOK_WIDTH//2))
        y = 0
        self.image = pygame.image.load(BLOK_IMAGE_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.image,(BLOK_WIDTH,BLOK_HEIGHT))
        self.rect = self.image.get_rect(center = (x,y))
        self.speed = BLOK_SPEED
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill