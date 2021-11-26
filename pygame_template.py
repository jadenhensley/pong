import pygame
from pygame.locals import *
import os, sys
from button import Button
from text import draw_text
from math import ceil
import path_util
from random import choice

# pygame project initialization and setup
PROJECT_PATH = path_util.get_project_directory()

pygame.init()
pygame.display.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()

screen_width = 900
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("pygame project")
clock = pygame.time.Clock()


# loading in fonts
pygame.font.init()
roboto_large = pygame.font.Font(f'{PROJECT_PATH}/fonts/Roboto-Bold.ttf', 72)
roboto_medium = pygame.font.Font(f'{PROJECT_PATH}/fonts/Roboto-Bold.ttf', 24)
roboto_small = pygame.font.Font(f'{PROJECT_PATH}/fonts/Roboto-Bold.ttf', 20)
roboto_italic_medium = pygame.font.Font(f'{PROJECT_PATH}/fonts/Roboto-BoldItalic.ttf', 28)
roboto_italic_small = pygame.font.Font(f'{PROJECT_PATH}/fonts/Roboto-BoldItalic.ttf', 18)
gravity_bold = pygame.font.Font(f'{PROJECT_PATH}/fonts/GravityBold8.ttf', 32)
gravity_bold_large = pygame.font.Font(f'{PROJECT_PATH}/fonts/GravityBold8.ttf', 72)


# main game loop
RUN, GAMEOVER = True, False

def game_main():
    global RUN, GAMEOVER


    while RUN:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                if (key[pygame.K_LCTRL] or key[pygame.K_LALT]) and (key[pygame.K_q] or key[pygame.K_w]):
                    pygame.quit()
                    sys.exit()
                    quit()
                if key[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()
                    quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                quit()

        screen.fill((0,0,0))
        

        # draw_text(screen, f"score: {SCORE_COUNT}", gravity_bold, (225, 255, 255), 600, 200)

        # if buttonNewGame.draw():
        #     pass

        # if buttonExitGame.draw():
        #     pygame.quit()
        #     sys.exit()
        #     quit()


        if GAMEOVER:
            pass
            # draw_text(screen, f"GAME OVER!!!", gravity_bold_large, (220, 30, 30), 100, 600)


        pygame.display.update()
        clock.tick(60)

    pygame.quit()

game_main()