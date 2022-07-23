import pygame
import player_snake_information
import window_game

player_snake_body_block = pygame.transform.scale(pygame.image.load("assets\player_snake\player_snake_body_block.png")
                                                 , (player_snake_information.player_snake_block_size, 
                                                    player_snake_information.player_snake_block_size))

player_snake_food = pygame.transform.scale(pygame.image.load("assets\player_snake_food\player_snake_food.png")
                                                 , (player_snake_information.player_snake_block_size-4, 
                                                    player_snake_information.player_snake_block_size-4))

ingame_background = pygame.transform.scale(pygame.image.load("assets\ingame\\background.png")
                                                 , (window_game.window_length, window_game.window_width))