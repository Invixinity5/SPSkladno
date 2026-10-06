import pygame
from settings import *
import random
class Block(pygame.sprite.Sprite):
    def __init__(self,speed=BLOCK_SPEED,speed_multiplier=MULTIPLIER,death_count=COUNT):
        super().__init__()
        x = random.randrange(0 + (BLOCK_WIDTH // 2), WIDTH - (BLOCK_WIDTH // 2))
        y = 0
        self.image = pygame.image.load(BLOCK_IMAGE_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.image, (BLOCK_WIDTH, BLOCK_HEIGHT))
        self.rect = self.image.get_rect(bottom=y, centerx=x) # center = (x,y)¨
        self.speed = speed
        self.speed_multiplier = speed_multiplier
        self.death_count = death_count

    def update(self):
        if self.death_count >= 10:
            self.death_count = COUNT
            self.speed_multiplier += 0.1
        self.rect.y += self.speed * self.speed_multiplier
        if self.rect.top > HEIGHT+1:
            self.kill()
            self.death_count += 1


if __name__ == "__main__":
    import main