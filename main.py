import pygame
from sys import exit
from random import randint
from math import sqrt
from time import sleep
pygame.init()
pygame.display.set_caption("Snake Game v2")
pygame.display.set_icon(pygame.image.load("snake.webp"))
font = pygame.font.Font("freesansbold.ttf", 20)
score = 0
def score_func():
    score_text = font.render("Score: " + str(score), True, (255,255,255))
    screen.blit(score_text, (5,5))
pygame.mixer_music.load("bg music.mp3")
pygame.mixer_music.play(-1)
munch = pygame.mixer.Sound("munch.mp3")
over = pygame.mixer.Sound("over.mp3")
screen = pygame.display.set_mode((600, 400))
background = pygame.image.load("bg.jpg")
snake_head = pygame.image.load("snake head.png")
snake_body = pygame.image.load("snake copy.png")
apple_img = pygame.image.load("apple.png")
snake_up = pygame.transform.rotate(snake_head, 180)
snake_right = pygame.transform.rotate(snake_head, 90)
snake_left = pygame.transform.rotate(snake_head, -90)
snake_down = pygame.transform.rotate(snake_head, 0)
snake_list = [[0,30], [0,10], [0,0]]
state = "down"
eating = False
class fruit:
    def __init__(self):
        self.x = randint(50, 550)
        self.y = randint(50, 350)
    def apple_spawn(self):
        screen.blit(apple_img, (self.x, self.y))
apple = fruit()
def down():
    snake_list.insert(0, (snake_list[0][0], snake_list[0][1] + 10))
    snake_list.pop(-1)
def up():
    snake_list.insert(0, (snake_list[0][0], snake_list[0][1] - 10))
    snake_list.pop(-1)
def right():
    snake_list.insert(0, (snake_list[0][0] + 10, snake_list[0][1]))
    snake_list.pop(-1)
def left():
    snake_list.insert(0, (snake_list[0][0] - 10, snake_list[0][1]))
    snake_list.pop(-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if state == "up":
                    pass
                else:
                    state = "down"
                    down()
            elif event.key == pygame.K_RIGHT:
                if state == "left":
                    pass
                else:
                    state = "right"
                    right()
            elif event.key == pygame.K_LEFT:
                if state == "right":
                    pass
                else:
                    state = "left"
                    left()
            elif event.key == pygame.K_UP:
                if state == "down":
                    pass
                else:
                    state = "up"
                    up()
    screen.blit(background, (0,0))
    apple.apple_spawn()
    apple_distance = sqrt(pow(snake_list[0][0] - apple.x, 2) + pow(snake_list[0][1] - apple.y, 2))
    n = -1
    if state == "down":
        down()
        snake_head = snake_down
    elif state == "up":
        up()
        snake_head = snake_up
    elif state == "right":
        right()
        snake_head = snake_right
    elif state == "left":
        left()
        snake_head = snake_left
    for i in snake_list:
        n += 1
        if n == 0:
            screen.blit(snake_head, (snake_list[n][0], snake_list[n][1]))
        else:
            screen.blit(snake_body, (snake_list[n][0], snake_list[n][1]))
    if apple_distance < 27:
        if state == "right" or state == "left":
            snake_list.insert(0, [apple.x, snake_list[0][1]])
        elif state == "up" or state == "down":
            snake_list.insert(0, [snake_list[0][0], apple.y])
        apple = fruit()
        score += 1
        eating = True
        pygame.mixer.Sound.play(munch)
    eating = False
    if snake_list[0][0] > 558 or snake_list[0][1] > 359 or snake_list[0][0] < -20 or snake_list[0][1] < -30:
        pygame.mixer.Sound.play(over)
        sleep(1)
        exit()
    if snake_list[0] in snake_list[1:]:
        if eating == False:
            pygame.mixer.Sound.play(over)
            sleep(1)
            exit()
    score_func()
    pygame.display.update()
    pygame.time.Clock().tick(20)