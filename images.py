import pygame
import player_snake_information

player_snake_body_block = pygame.transform.scale(pygame.image.load("assets\player_snake\player_snake_body_block_01.png")
                                                 , (player_snake_information.player_snake_block_size, 
                                                    player_snake_information.player_snake_block_size))
