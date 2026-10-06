import pygame
from Settings import *
class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(PLAYER_IMAGE_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.image,(PLAYERS_WIDTH,PLAYERS_HEIGHT))
        self.rect = self.image.get_rect(center = (WIDTH//2,HEIGHT-30))
        self.speed = PLAYER_SPEED
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < WIDTH:
            self.rect.x += self.speed