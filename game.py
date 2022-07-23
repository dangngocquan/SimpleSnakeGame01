import pygame
import window_game
import player_snake_information
import images
  
def display_snake():
    game_window.fill((0, 0, 0))
    for player_snake_block in player_snake_block_list:
        game_window.blit(images.player_snake_body_block, 
                         (player_snake_block[0], player_snake_block[1]))
    
             

pygame.init()
game_window = pygame.display.set_mode((window_game.window_length, window_game.window_width))
pygame.display.set_caption(window_game.game_caption)
pygame.display.update()

clock = pygame.time.Clock()

game_over = False
head_snake_x = window_game.window_length / 2
head_snake_y = window_game.window_width / 2
x_speed = 0
y_speed = 0

player_snake_block_list = [[head_snake_x, head_snake_y]]
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                x_speed = 0
                if y_speed != player_snake_information.player_snake_block_size:
                    y_speed = -player_snake_information.player_snake_block_size
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                x_speed = 0
                if y_speed != -player_snake_information.player_snake_block_size:
                    y_speed = player_snake_information.player_snake_block_size
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if x_speed != player_snake_information.player_snake_block_size:
                    x_speed = -player_snake_information.player_snake_block_size
                y_speed = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if x_speed != -player_snake_information.player_snake_block_size:
                    x_speed = player_snake_information.player_snake_block_size
                y_speed = 0
    head_snake_x = (head_snake_x + x_speed) % window_game.window_length
    head_snake_y = (head_snake_y + y_speed) % window_game.window_width
    player_snake_block_list.insert(0, [head_snake_x, head_snake_y])
    del player_snake_block_list[len(player_snake_block_list) - 1]
    display_snake()
    pygame.display.update()
    
    clock.tick(player_snake_information.player_snake_speed)
    
pygame.quit()
quit()