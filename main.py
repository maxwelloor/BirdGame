import resources
import pygame
import sys

## COLOURS ##
white = (255, 255, 255)
black = (0, 0, 0)

## SCREEN SIZE ##
screen_w = 1280
screen_h = 720

## Sets the game clock
clock = pygame.time.Clock()
FPS = 30

# The list for storing entities
entity_list = []

bird_timer = 0
bird_spawn_delay = 20

player_lives = 3

pygame.init()

font = pygame.font.SysFont('arial', 32)

display = pygame.display.set_mode((screen_w, screen_h))

while True:

    if player_lives <= 0:
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.fill(white)

    for bird in resources.Bird.birds:
        bird.update(display)
        if bird.y > 720:
            player_lives -= 1
            bird.destroy(0)
    
    resources.Bird.check_for_clicks()

    ## Makes birds appear
    bird_timer += 1

    if bird_timer >= bird_spawn_delay:
        resources.Bird(screen_w, screen_h)
        bird_timer = 0

    # Score and lives.
    score_display = font.render(str(resources.Bird.player_score), 1, black)
    display.blit(score_display, (30, 20))

    life_display = font.render('Lives: ' + str(player_lives), 1, black)
    display.blit(life_display, (30, 60))

    pygame.event.pump()
    pygame.display.update()
    clock.tick(FPS)
