import pygame
from pygame.locals import *
import os, sys
from button import Button
from text import draw_text
from math import ceil
import path_util
import random

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

# game buttons
imgNewGame = pygame.image.load(f'{PROJECT_PATH}/img/startgame.png')
imgExitGame = pygame.image.load(f'{PROJECT_PATH}/img/exitgame.png')
buttonNewGame = Button(screen, 30, 100, imgNewGame)
buttonExitGame = Button(screen, 30, 400, imgExitGame)


def game_main():
    global RUN, GAMEOVER, screen_width, screen_height

    states = ['menu','start','playing','win','gameover']
    gamestate = states[0]
    PLAYER_WON = False

    p1rect = pygame.Rect(30, 90, 20, 90)
    p2rect = pygame.Rect(screen_width-50, screen_height-180, 20, 90)
    pong = pygame.Rect(screen_width // 2 - 90, screen_height // 2 - 30, 25, 25)

    P1SCORE = 0
    P2SCORE = 0
    SCORE_THRESHOLD = 8

    direction_x = random.choice([-1, 1])
    direction_y = random.choice([-1, 1])

    pong_velocity_x = random.randint(6, 10) * direction_x
    pong_velocity_y = random.randint(2, 10) * direction_y

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
                if gamestate == states[1]:
                    if key[pygame.K_SPACE]:
                        gamestate = states[2]
                if gamestate == states[2]:
                    if key[pygame.K_s]:
                        p1rect.y += 50
                    if key[pygame.K_w]:
                        p1rect.y -= 50
                    if key[pygame.K_DOWN]:
                        p2rect.y += 50
                    if key[pygame.K_UP]:
                        p2rect.y -= 50
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                quit()

        screen.fill((0,0,0))
        
        if gamestate == states[0]:
            draw_text(screen, f"PONG", gravity_bold_large, (0, 200, 0), 600, 200)

            if buttonNewGame.draw():
                gamestate = states[1]

            if buttonExitGame.draw():
                pygame.quit()
                sys.exit()
                quit()

        if gamestate == states[1]:
            draw_text(screen, "spacebar to start", gravity_bold, (0,200,0), screen_width // 2 - 90, screen_height // 2 - 30)
            pygame.draw.rect(screen, (255,255,255), p1rect)
            pygame.draw.rect(screen, (255,255,255), p2rect)


        elif gamestate == states[2]:
            draw_text(screen, f"{P1SCORE}", gravity_bold, (255,255,255), 240, 30)
            draw_text(screen, f"{P2SCORE}", gravity_bold, (255,255,255), screen_width - 300, 30)
            pygame.draw.rect(screen, (255,255,255), p1rect)
            pygame.draw.rect(screen, (255,255,255), p2rect)
            pygame.draw.rect(screen, (0,200,0), pong)
            pong.x += pong_velocity_x
            pong.y += pong_velocity_y

            if P1SCORE == SCORE_THRESHOLD or P2SCORE == SCORE_THRESHOLD:
                gamestate = states[4]

            if pong.right >= screen_width:
                pong.x, pong.y = screen_width // 2 - 90, screen_height // 2 - 30

                direction_x = random.choice([-1, 1])
                direction_y = random.choice([-1, 1])

                pong_velocity_x = random.randint(6, 10) * direction_x
                pong_velocity_y = random.randint(2, 5) * direction_y
                P1SCORE += 1
            if pong.left <= 0:
                pong.x, pong.y = screen_width // 2 - 90, screen_height // 2 - 30
                
                direction_x = random.choice([-1, 1])
                direction_y = random.choice([-1, 1])

                pong_velocity_x = random.randint(6, 10) * direction_x
                pong_velocity_y = random.randint(2, 10) * direction_y
                P2SCORE += 1
            if pong.top <= 0 or pong.bottom >= screen_height:
                pong_velocity_y *= -1

            collision_tolerance = 10
            if pong.colliderect(p1rect) or pong.colliderect(p2rect):
                if abs(pong.left - p1rect.right) < collision_tolerance:
                    pong_velocity_x *= -1
                if abs(pong.right - p2rect.left) < collision_tolerance:
                    pong_velocity_x *= -1


        if gamestate == states[4]:
            draw_text(screen, "game over", gravity_bold, (0,200,0), screen_width // 2 - 90, screen_height // 2 - 30)
            if P1SCORE == SCORE_THRESHOLD:
                draw_text(screen, "Player 1 wins!", gravity_bold, (0,200,0), screen_width // 2 - 40, screen_height // 2 + 30)
            elif P2SCORE == SCORE_THRESHOLD:
                draw_text(screen, "Player 2 wins!", gravity_bold, (0,200,0), screen_width // 2 - 40, screen_height // 2 + 30)
            


        pygame.display.update()
        clock.tick(60)

    pygame.quit()

game_main()