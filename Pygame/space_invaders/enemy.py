import pygame
import random as rand
import settings
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        alien_type = rand.randint(1,5)
        self.image = pygame.image.load(settings.ENEMY_IMAGE_PATH.format(alien_type)).convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*settings.ENEMY_SCALE,self.image.get_height()*settings.ENEMY_SCALE))
        self.rect = self.image.get_rect(top=y,centerx=x)
        self.speed = settings.ENEMY_SPEED
        self.direction = "right"
        self.counter = -140
    def update(self):
        if self.direction == "left":
            self.rect.move_ip(-self.speed,0)
            self.counter -= 1
        else:
            self.rect.move_ip(self.speed,0)
            self.counter += 1
        if self.counter == 140:
            self.direction = "left"
            self.rect.y += 50
        elif self.counter == -140:
            self.direction = "right"
            self.rect.y += 50