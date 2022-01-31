# NAME OF AUTHOR: Rocco Crupi
# NAME OF THE PROGRAM: Snake game 

import pygame
import random
import time
from pygame import Color, draw, display, time

pygame.init()

yellow = (255, 255, 102)
black = (0, 0, 0)

dis_width = 600
dis_height = 400

clock = pygame.time.Clock()

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Rocco')

snake_block = 10
snake_speed = 10
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
 
def theSnake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
  