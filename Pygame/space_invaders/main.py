import pygame
from Character import *
from Enemy import *
from settings import *
from Bullet import *
import random as rand
pygame.init()
spawn_counter = 0
enemy_shoot = 0
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
enemy = Enemy(50,20)
hrac = Character()
hrac_group = pygame.sprite.Group()
hrac_group.add(hrac)
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
dalsi_enemy = pygame.USEREVENT + 1
pygame.time.set_timer(dalsi_enemy, 750)
restart_spawn = pygame.USEREVENT + 2
shoot = pygame.USEREVENT +3
pygame.time.set_timer(shoot,1500)
def vypis_menu():
    screen.blit(title_text, title_rect)
    screen.blit(play_text,play_rect)
    screen.blit(settings_text,settings_rect)
    screen.blit(exit_text,exit_rect)
state = "MENU"
running = True
while running == True:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        if event.type == restart_spawn and state == "PLAYING":
            spawn_counter = 0
            pygame.time.set_timer(restart_spawn, 0)
        if event.type == dalsi_enemy and state == "PLAYING" and spawn_counter <= 19:
            enemy_group.add(Enemy(50,20))
            spawn_counter += 1
        if spawn_counter == 19:
            pygame.time.set_timer(restart_spawn, 15000)
        if keys[pygame.K_SPACE] and hrac.cooldown == 0:
            bullet = Bullet(hrac.rect.centerx,hrac.rect.centery-25,"PLAYER")
            hrac_group.add(bullet)
            hrac.cooldown = pygame.time.get_ticks()
        if event.type == shoot:
            for enemy in enemy_group:
                enemy_shoot = rand.randint(0,100)
                if enemy_shoot <=20:
                    enemy_bullet = Bullet(enemy.rect.centerx,enemy.rect.centery+25,"ALIEN")
                    bullet_group.add(enemy_bullet)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if state == "MENU":
                if play_rect.collidepoint(mouse_pos):
                    state = "PLAYING"
                elif settings_rect.collidepoint(mouse_pos):
                    state = "SETTINGS"
                elif exit_rect.collidepoint(mouse_pos):
                    running = False
    if state == "MENU":
        screen.fill((0,0,0))
        vypis_menu()
    elif state == "PLAYING":
        screen.fill((0,0,0))
        hrac_group.update()
        hrac_group.draw(screen)
        enemy_group.update()
        enemy_group.draw(screen)
        bullet_group.update()
        bullet_group.draw(screen)
        if pygame.sprite.spritecollide(hrac, enemy_group, True, pygame.sprite.collide_mask):
            pygame.time.delay(2000)
            state = "GAME_OVER"
        if pygame.sprite.spritecollide(hrac, bullet_group, True, pygame.sprite.collide_mask):
            pygame.time.delay(2000)
            state = "GAME_OVER"
        if pygame.sprite.groupcollide(enemy_group, hrac_group, True, True, pygame.sprite.collide_mask):
            pass
    elif state == "SETTINGS":
        pass
    elif state == "GAME_OVER":
        state = "MENU"
    pygame.display.update()
    clock.tick(30)
pygame.quit()