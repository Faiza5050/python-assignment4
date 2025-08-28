import pygame
from pygame.locals import *
import time
import random

print("Python Project # 17 - Snake")
print("Welcome To Snake Game!")
print("Let's Play The Game!")

pygame.init()
red = (255, 0, 0)
grey = (0, 255, 0)
green = (51, 182, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (20, 20, 20)

win_width = 700
win_height = 500
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake Game by Faiza")
time.sleep(1)

snake = 10
snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 26)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    window.blit(value, [10, 10])

def game_snake(snake, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake, snake])

def message(msg):
    msg = font_style.render(msg, True, yellow)
    window.blit(msg, [win_width / 6, win_height / 3])

def game_loop():
    game_over = False
    game_close = False

    x1 = win_width / 2
    y1 = win_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            window.fill(black)
            message = font_style.render("You Lost! Press P-Play Again or Q-Quit", True, yellow)
            window.blit(message, [win_width / 6, win_height / 3])
            your_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake
                    x1_change = 0

        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(black)
        pygame.draw.rect(window, red, [foodx, foody, snake, snake])
        snake_size = []
        snake_size.append(x1)
        snake_size.append(y1)
        snake_list.append(snake_size)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_size:
                game_close = True

        game_snake(snake, snake_list)
        your_score(snake_length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
            foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    print("Final Score:", snake_length - 1)
    quit()

game_loop()
