import pygame
import window_game
import images

def display_snake_block(x, y):
    game_window.blit(images.player_snake_body_block_01, (x, y))
    pygame.display.update()
    clock.tick(1)
    game_window.blit(images.player_snake_body_block_02, (x, y))
    pygame.display.update()
    clock.tick(1)
  
def display_snake():
    for snake_block in player_snake_block_list:
        display_snake_block(snake_block[0], snake_block[1])      

pygame.init()
game_window = pygame.display.set_mode((window_game.window_length, window_game.window_width))
pygame.display.update()

clock = pygame.time.Clock()

game_over = False
head_snake_x = window_game.window_length / 2
head_snake_y = window_game.window_width / 2
player_snake_block_list = [[head_snake_x, head_snake_y]]
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    display_snake_block(100, 100)
    
pygame.quit()
quit()