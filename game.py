from itertools import count
from matplotlib.pyplot import fill
import pygame
import window_game
import player_snake_information
import images
import random
  
def display_snake():
    global game_window
    for index in range(1, len(player_snake_block_list) + 1):
        game_window.blit(images.player_snake_body_block, 
                         (player_snake_block_list[-index][0], player_snake_block_list[-index][1]))
        
def display_player_snake_food():
    global game_window
    for food in player_snake_food_list:
        game_window.blit(images.player_snake_food, 
                         (food[0]+2, food[1]+2)) 

def display_score():
    global game_window
    text = pygame.font.SysFont(None, 30).render(f"Your score: {player_score}", True, (0, 255, 255))
    game_window.blit(text, (10, 10))
    

def display_screen():
    global game_window
    game_window.blit(images.ingame_background, (0, 0))
    display_player_snake_food()
    display_snake()
    display_score()

def random_coordinates_empty():
    max_cells_x = window_game.window_length // player_snake_information.player_snake_block_size - 2
    max_cells_y = window_game.window_width // player_snake_information.player_snake_block_size - 2
    max_cells_in_game = max_cells_x * max_cells_y
    cells_number_existing = len(player_snake_block_list) + len(player_snake_food_list)
    x = -1
    y = -1
    if cells_number_existing < max_cells_in_game:
        x = round(random.random() * max_cells_x) * player_snake_information.player_snake_block_size
        y = round(random.random() * max_cells_y) * player_snake_information.player_snake_block_size
        while [x, y] in player_snake_food_list:
            x = round(random.random() * max_cells_x) * player_snake_information.player_snake_block_size
            y = round(random.random() * max_cells_y) * player_snake_information.player_snake_block_size
    return [x, y]
    
def random_player_snake_food():
    global player_snake_food_list
    max_food = player_snake_information.player_snake_food_max
    create_food = True
    while create_food and (len(player_snake_food_list) < max_food):
        random_coordinates = random_coordinates_empty()
        if random_coordinates[0] != -1:
            player_snake_food_list.append(random_coordinates)
        else:
            create_food = False

def player_snake_move():
    global head_snake_x
    global head_snake_y
    global player_snake_block_list
    
    head_snake_x = (head_snake_x + x_speed) % window_game.window_length
    head_snake_y = (head_snake_y + y_speed) % window_game.window_width
    player_snake_block_list.insert(0, [head_snake_x, head_snake_y])
    del player_snake_block_list[len(player_snake_block_list) - 1]

def player_snake_eat_food():
    global x_speed
    global y_speed
    global player_snake_block_list
    global player_snake_food_list
    global player_score
    global player_snake_speed
    
    head_snake = player_snake_block_list[0]
    if head_snake in player_snake_food_list:
        player_snake_food_list.remove(head_snake)
        tail_snake = player_snake_block_list[len(player_snake_block_list) - 1]
        add_snake_block = [tail_snake[0] - x_speed, tail_snake[1] - y_speed]
        player_snake_block_list.append(add_snake_block)
        player_score += 1
        player_snake_speed = player_snake_information.player_snake_speed + player_score // 2

def update_status_of_player_snake():
    global game_over
    global head_snake_x
    global head_snake_y
    if player_snake_block_list.count([head_snake_x, head_snake_y]) > 1:
        game_over = True

def play_game():
    global game_over
    global head_snake_x
    global head_snake_y
    global player_snake_block_list
    global x_speed
    global y_speed

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
        random_player_snake_food()
        player_snake_move()
        player_snake_eat_food()
        update_status_of_player_snake()
        display_screen()
        pygame.display.update()
        
        clock.tick(player_snake_speed)         

# Main
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
player_snake_food_list = []
player_score = 0
player_snake_speed = player_snake_information.player_snake_speed

play_game()
    
pygame.quit()
quit()