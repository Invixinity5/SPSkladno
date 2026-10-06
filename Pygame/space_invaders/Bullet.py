import pygame
import settings
import random as rand

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,shooter = "ALIEN"):
        super().__init__()
        self.shooter = shooter
        if shooter == "ALIEN":
            self.image = pygame.image.load(settings.ENEMY_BULLET_IMG).convert_alpha()
            self.rect = self.image.get_rect(center=(x,y))
            self.speed = settings.ENEMY_BULLET_SPEED
        else:
            self.image = pygame.image.load(settings.PLAYER_BULLET_IMG).convert_alpha()
            self.rect = self.image.get_rect(center=(x,y))
            self.speed = settings.PLAYER_BULLET_SPEED
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom<0 or self.rect.top>settings.HEIGHT:
            self.kill