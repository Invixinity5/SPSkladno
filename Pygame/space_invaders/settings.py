import pygame
pygame.init()


WIDTH = 1248
HEIGHT = 720
FPS = 60

PLAYERS_WIDTH = 50
PLAYERS_HEIGHT = 50
PLAYER_SPEED = 5
PLAYER_BULLET_SPEED = -10
PLAYER_IMAGE_PATH = 'img/spaceship.png'
PLAYER_BULLET_IMG = 'img/bullet.png'
ENEMY_SCALE = 1.24
ENEMY_SPEED = 4
ENEMY_BULLET_SPEED = 5
ENEMY_IMAGE_PATH = 'img/alien{}.png'
ENEMY_BULLET_IMG = 'img/alien_bullet.png'

menu_font = pygame.font.SysFont('Arial',50)
title_text = menu_font.render("Space Invaders", True, (255,255,255))
title_rect = title_text.get_rect(center=(624,50))
play_text = menu_font.render("Play", True, (255,255,255))
play_rect = play_text.get_rect(center=(624,200))
settings_text = menu_font.render("Settings", True, (255,255,255))
settings_rect = settings_text.get_rect(center=(624,300))
exit_text = menu_font.render("Exit", True, (255,255,255))
exit_rect = exit_text.get_rect(center=(624,400))