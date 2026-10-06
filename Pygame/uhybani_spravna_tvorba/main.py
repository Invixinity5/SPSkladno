import pygame
from Player import *
from Block import Block
from settings import *
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Uhybani")
running = True
body = BODY
with open('skore.txt','r') as soubor:
    highscore = int(soubor.read())
clock = pygame.time.Clock()
base_font = pygame.font.Font(None, 40)
score_text = base_font.render(f"score: {body}", True, (0,0,0))
highscore_text = base_font.render(f"highscore: {highscore}", True, (0,0,0))
hrac = Player()
hrac_group = pygame.sprite.Group()
hrac_group.add(hrac)
blok = Block()
blok_group = pygame.sprite.Group()
blok_group.add(blok)
BLOK_SPAWN = pygame.USEREVENT + 1
pygame.time.set_timer(BLOK_SPAWN, 500)
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == BLOK_SPAWN:
            blok_group.add(Block())
    hrac_group.update()
    hrac_group.draw(screen)
    blok_group.update()
    blok_group.draw(screen)
    for blok in blok_group:
        if blok.rect.top >= HEIGHT:
            body += 1
            score_text = base_font.render(f"score: {body}", True, (0,0,0))
    if body > highscore:
        highscore += 1
        highscore_text = base_font.render(f"highscore: {highscore}", True, (0,0,0))
    screen.blit(score_text,(10,50))
    screen.blit(highscore_text,(10,80))
    if pygame.sprite.spritecollide(hrac, blok_group, True, pygame.sprite.collide_mask):
        print("KOLIZE!")
        with open('skore.txt','w') as soubor:
            soubor.write(str(highscore))
        pygame.time.delay(1000)
        running = False

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()