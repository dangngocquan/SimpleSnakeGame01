import pygame
import player_snake_information
import AI_snake_information
import window_game_information

player_snake_body_block = pygame.transform.scale(pygame.image.load("assets\player_snake\player_snake_body_block.png")
                                                 , (player_snake_information.player_snake_block_size, 
                                                    player_snake_information.player_snake_block_size))

player_snake_food = pygame.transform.scale(pygame.image.load("assets\player_snake_food\player_snake_food.png")
                                                 , (player_snake_information.player_snake_block_size-4, 
                                                    player_snake_information.player_snake_block_size-4))

ingame_background = pygame.transform.scale(pygame.image.load("assets\ingame\\background.png")
                                                 , (window_game_information.window_length, window_game_information.window_width))

AI_snake_body_block = pygame.transform.scale(pygame.image.load("assets\AI_snake\AI_snake_body_block.png")
                                                 , (AI_snake_information.AI_snake_block_size, 
                                                    AI_snake_information.AI_snake_block_size))

AI_snake_food =  pygame.transform.scale(pygame.image.load("assets\player_snake_food\player_snake_food.png")
                                                 , (player_snake_information.player_snake_block_size-4, 
                                                    player_snake_information.player_snake_block_size-4))