import pygame
from Character import *
from Settings import *
from Blok import *
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("uhýbání")
clock = pygame.time.Clock()
running = True
blok = Blok()
hrac = Character()
blok_group = pygame.sprite.Group()
hrac_group = pygame.sprite.Group()
hrac_group.add(hrac)
blok_group.add(blok)

while running:
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    screen.fill((0,0,0))
    keys = pygame.key.get_pressed()
    
    dalsi_blok = pygame.USEREVENT
    pygame.time.set_timer(dalsi_blok, 2000)
    if event.type == dalsi_blok:
        blok_group.add(blok)
    
    if keys[pygame.K_F11]:
        pygame.display.toggle_fullscreen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    hrac_group.update()
    hrac_group.draw(screen)
    blok_group.update()
    blok_group.draw(screen)

    if pygame.sprite.spritecollide(hrac, blok_group, True, pygame.sprite.collide_mask):
        pygame.time.delay(1000)
        running = False
        print("collision")
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()