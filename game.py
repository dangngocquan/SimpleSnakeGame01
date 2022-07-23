import pygame
import display_information
import images

def display_snake_block(x, y):
    game_display.blit(images.player_snake_body_block_01, (x, y))
    pygame.display.update()
    game_display.blit(images.player_snake_body_block_02, (x, y))
    pygame.display.update()
        

pygame.init()
game_display = pygame.display.set_mode((display_information.game_display_length, display_information.game_display_width))
pygame.display.update()
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    display_snake_block(100, 100)
    
pygame.quit()
quit()