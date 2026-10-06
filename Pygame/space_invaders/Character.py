import pygame
import settings
class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(settings.PLAYER_IMAGE_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.image,(settings.PLAYERS_WIDTH,settings.PLAYERS_HEIGHT))
        self.rect = self.image.get_rect(center = (settings.WIDTH//2,settings.HEIGHT-30))
        self.speed = settings.PLAYER_SPEED
        self.cooldown = 0
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > 50:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < settings.WIDTH-50:
            self.rect.x += self.speed
        if self.cooldown +1500 < pygame.time.get_ticks():
            self.cooldown = 0