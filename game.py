from itertools import count
from matplotlib.pyplot import fill
import pygame
import window_game_information
import player_snake_information
import AI_snake_information
import images
import random

# player_snake
def display_player_snake():
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
    

def display_screen_player_snake():
    global game_window
    display_player_snake_food()
    display_player_snake()
    display_score()

def random_coordinates_empty_for_player():
    max_cells_x = window_game_information.window_length // player_snake_information.player_snake_block_size - 2
    max_cells_y = window_game_information.window_width // player_snake_information.player_snake_block_size - 2
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
        random_coordinates = random_coordinates_empty_for_player()
        if random_coordinates[0] != -1:
            player_snake_food_list.append(random_coordinates)
        else:
            create_food = False

def player_snake_move():
    global head_snake_x
    global head_snake_y
    global player_snake_block_list
    
    head_snake_x = (head_snake_x + x_speed) % window_game_information.window_length
    head_snake_y = (head_snake_y + y_speed) % window_game_information.window_width
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
        add_snake_block = [head_snake[0] - x_speed, head_snake[1] - y_speed]
        player_snake_block_list.append(add_snake_block)
        player_score += 1
        player_snake_speed = player_snake_information.player_snake_speed + player_score // 20

def player_snake_food_move():
    global player_snake_food_list
    for index in range(len(player_snake_food_list)):
        food_change_x = 0
        food_change_y = 0
        direction = get_random_number(4)
        if direction == 1:
            food_change_x = 0
            food_change_y = -player_snake_information.player_snake_block_size
        elif direction == 2:
            food_change_x = 0
            food_change_y = player_snake_information.player_snake_block_size
        elif direction == 3:
            food_change_x = -player_snake_information.player_snake_block_size
            food_change_y = 0
        elif direction == 4:
            food_change_x = player_snake_information.player_snake_block_size
            food_change_y = 0
        player_snake_food_list[index] = [player_snake_food_list[index][0] + food_change_x, 
                                         player_snake_food_list[index][1] + food_change_y]
                
        

def update_status_of_player_snake():
    global game_over
    global head_snake_x
    global head_snake_y
    if player_snake_block_list.count([head_snake_x, head_snake_y]) > 1 or [head_snake_x, head_snake_y] in AI_snake_block_list:
        game_over = True


# AI_snake
def create_AI_snake():
    global AI_snake_list
    global AI_snake_block_list
    coordinates = random_coordinates_empty_for_player()
    while coordinates[0] == player_snake_block_list[0][0] or coordinates[1] == player_snake_block_list[0][1]:
        coordinates = random_coordinates_empty_for_player()
    if coordinates[0] != -1:
        AI_snake = [coordinates]
        AI_snake_list.append(AI_snake)
        AI_snake_block_list.append(coordinates)

# def display_AI_snake_food():
#     global game_window
#     for food in AI_snake_food_list:
#         game_window.blit(images.player_snake_food, 
#                          (food[0]+2, food[1]+2))
        
def display_AI_snake_list():
    global game_window
    for AI_snake in AI_snake_list:
        for AI_snake_body_block in AI_snake:
            game_window.blit(images.AI_snake_body_block, (AI_snake_body_block[0], AI_snake_body_block[1]))

def get_random_number(choose_number):
    return 1 + round(random.random() * choose_number)

def AI_snake_move():
    global AI_snake_list
    for AI_snake in AI_snake_list:
        AI_x_speed = 0
        AI_y_speed = 0
        while AI_x_speed == 0 and AI_y_speed == 0:
            direction = get_random_number(100)
            if direction % 4 == 1:
                AI_x_speed = 0
                AI_y_speed = -AI_snake_information.AI_snake_block_size
            elif direction % 4 == 2:
                AI_x_speed = 0
                AI_y_speed = AI_snake_information.AI_snake_block_size
            elif direction % 4 == 3:
                AI_x_speed = -AI_snake_information.AI_snake_block_size
                AI_y_speed = 0
            elif direction % 4 == 4:
                AI_x_speed = AI_snake_information.AI_snake_block_size
                AI_y_speed = 0
            
            if [(AI_snake[0][0] + AI_x_speed) % window_game_information.window_length, 
                (AI_snake[0][1] + AI_y_speed) % window_game_information.window_width] in AI_snake:
                AI_x_speed = 0
                AI_y_speed = 0

        AI_snake.insert(0, [(AI_snake[0][0] + AI_x_speed) % window_game_information.window_length, 
                            (AI_snake[0][1] + AI_y_speed) % window_game_information.window_width])
        del AI_snake[len(AI_snake) - 1]

def random_coordinates_empty_for_AI():
    max_cells_x = window_game_information.window_length // AI_snake_information.AI_snake_block_size - 2
    max_cells_y = window_game_information.window_width // AI_snake_information.AI_snake_block_size - 2
    max_cells_in_game = max_cells_x * max_cells_y
    cells_number_existing = len(AI_snake_block_list) + len(AI_snake_food_list)
    x = -1
    y = -1
    if cells_number_existing < max_cells_in_game:
        x = round(random.random() * max_cells_x) * AI_snake_information.AI_snake_block_size
        y = round(random.random() * max_cells_y) * AI_snake_information.AI_snake_block_size
        while [x, y] in AI_snake_food_list:
            x = round(random.random() * max_cells_x) * AI_snake_information.AI_snake_block_size
            y = round(random.random() * max_cells_y) * AI_snake_information.AI_snake_block_size
    return [x, y]

def random_AI_snake_food():
    global AI_snake_food_list
    max_food = AI_snake_information.AI_snake_food_max
    create_food = True
    while create_food and (len(AI_snake_food_list) < max_food):
        random_coordinates = random_coordinates_empty_for_AI()
        if random_coordinates[0] != -1:
            AI_snake_food_list.append(random_coordinates)
        else:
            create_food = False

def AI_snake_eat_food():
    global AI_snake_list
    global AI_snake_food_list
    for AI_snake in AI_snake_list:
        if AI_snake[0] in AI_snake_food_list:
            AI_snake.insert(0, AI_snake[0])
            AI_snake_food_list.remove(AI_snake[0])

def update_AI_snake_block():
    global AI_snake_block_list
    AI_snake_block_list.clear()
    for AI_snake in AI_snake_list:
        for AI_snake_block in AI_snake:
            AI_snake_block_list.append(AI_snake_block)

def display_screen_AI_snakes():
    # display_AI_snake_food()
    display_AI_snake_list()

def update_AI_snake_number():
    while len(AI_snake_list) < player_score // 25:
        create_AI_snake()

# Display all AI and Player
def display_all():
    game_window.fill((0, 0, 0))
    display_screen_AI_snakes()
    display_screen_player_snake()  

# Play game
def play_game():
    global clock
    global game_over
    global head_snake_x
    global head_snake_y
    global player_snake_block_list
    global x_speed
    global y_speed
    global temp_count

    while not game_over:
        temp_count += 1
        temp_count %= 60
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
        update_AI_snake_number()
        random_player_snake_food()
        random_AI_snake_food()
        if temp_count % 12 == 0:
            AI_snake_move()
        if temp_count % 60 == 0:
            player_snake_food_move()
        player_snake_move()
        AI_snake_eat_food()
        player_snake_eat_food()
        update_AI_snake_block()
        update_status_of_player_snake()
        display_all()
        pygame.display.update()
        
        clock.tick(player_snake_speed) 

# # Main
    
if __name__ == '__main__':
    pygame.init()
    game_window = pygame.display.set_mode((window_game_information.window_length, window_game_information.window_width))
    pygame.display.set_caption(window_game_information.game_caption)
    pygame.display.update()
    clock = pygame.time.Clock()

    game_over = False
    head_snake_x = window_game_information.window_length // 2
    head_snake_y = window_game_information.window_width // 2
    x_speed = 0
    y_speed = 0
    player_snake_block_list = [[head_snake_x, head_snake_y]]
    player_snake_food_list = []
    player_score = 0
    player_snake_speed = player_snake_information.player_snake_speed

    AI_snake_speed = AI_snake_information.AI_snake_speed
    AI_snake_list = []
    AI_snake_block_list = []
    AI_snake_food_list = []
    temp_count = 0

    play_game()
        
    pygame.quit()
    quit()