import pygame, sys, math
from pygame.locals import *
import random
from random import randint

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

height = 600
width = 800
# set up the window
DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
WHITE = (255, 255, 255)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
catSpeed = 5
backgroundImg = pygame.image.load('space.png')
monsterImg = pygame.image.load('monster.png')
monsterX = 100
monsterY = 100

gunx = width/2
guny = height - 100
gunAngle = 90

font = pygame.font.SysFont("comicsansms", 50)
text = font.render("0", True, (0, 54, 0))
newFont = pygame.font.SysFont("comicsansms", 50)

# Main Menu
def main_menu():

    menu=True
    selected="start"

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    game_start()
                elif event.key==pygame.K_2:
                    settings_menu()
                elif event.key==pygame.K_3:
                    about_menu()
                elif event.key==pygame.K_4:
                    pygame.quit()
                    quit()

        # Main Menu UI
        DISPLAYSURF.fill(BLUE)
        titleFont = pygame.font.SysFont("comicsansms", 80)
        title=titleFont.render("Hunt the cat", 0, YELLOW)

        if selected=="start":
            text_start=newFont.render("1. START", True, BLACK)
        else:
            text_quit=font.render("4. QUIT", 0, WHITE)
            text_setting=font.render("2. SETTINGS",0,WHITE)
            text_about=font.render("3. ABOUT",0,WHITE)

        if selected=="quit":
            text_quit=newFont.render("4. QUIT", True, BLACK)
        else:
            text_start=font.render("1. START", 0, WHITE)
            text_setting=font.render("2. SETTINGS",0,WHITE)
            text_about=font.render("3. ABOUT",0,WHITE)

        if selected=="settings":
            text_setting=newFont.render("2. SETTINGS", True, BLACK)
        else:
            text_start=font.render("1. START", 0, WHITE)
            text_about=font.render("3. ABOUT",0,WHITE)
            text_quit=font.render("4. QUIT",0,WHITE)


        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        about_rect=text_about.get_rect()
        quit_rect=text_quit.get_rect()
        settings_rect=text_setting.get_rect()

        # Main Menu Text
        DISPLAYSURF.blit(title, (width/2 - (title_rect[2]/2), 80))
        DISPLAYSURF.blit(text_start, (width/2 - (start_rect[2]/2), 300))
        DISPLAYSURF.blit(text_setting, (width/2 - (settings_rect[2]/2), 360))
        DISPLAYSURF.blit(text_about, (width/2 - (settings_rect[2]/2), 420))
        DISPLAYSURF.blit(text_quit, (width/2 - (quit_rect[2]/2), 480))


        pygame.display.update()
        fpsClock.tick(FPS)



def game_start():
        while True: # the main game loop
            DISPLAYSURF.fill(WHITE)
            global gunStart
            global gunEndx
            global gunEndy
            global catx
            global caty

            pygame.draw.line(DISPLAYSURF, Color("black"), (width/2+5,height), (width/2+5,height-10), 5)
            pygame.draw.line(DISPLAYSURF, Color("black"), (width/2+50,height), (width/2+5,height-10), 5)

            DISPLAYSURF.blit(backgroundImg,[0,0])
            DISPLAYSURF.blit(catImg, (catx, caty))
            DISPLAYSURF.blit(monsterImg, (monsterX - randint(0,50), monsterY-randint(0,50)))


            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        catx -= 10
                    if event.key == pygame.K_RIGHT:
                        catx += 10
                    if event.key == pygame.K_UP:
                        caty -= 10
                    if event.key == pygame.K_DOWN:
                        caty += 10

            pygame.display.update()
            fpsClock.tick(FPS)

def settings_menu():
    menu=True
    global catSpeed

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    catSpeed += 5
                elif event.key==pygame.K_DOWN:
                    catSpeed -= 5
                if event.key==pygame.K_BACKSPACE:
                    main_menu()



        # Main Menu UI
        DISPLAYSURF.fill(BLUE)

        title=font.render("Cat speed", 0, YELLOW)
        text_speed=font.render(str(catSpeed), 0, BLACK)
        returnToMenu=font.render("Backspace to return to main menu", 0, YELLOW)

        title_rect=title.get_rect()
        start_rect=text_speed.get_rect()
        return_rect =returnToMenu.get_rect()

        # Main Menu Text
        DISPLAYSURF.blit(title, (width/2 - (title_rect[2]/2), 80))
        DISPLAYSURF.blit(text_speed, (width/2 - (start_rect[2]/2), 300))
        DISPLAYSURF.blit(returnToMenu,(width/2 - (return_rect[2]/2), 400))

        pygame.display.update()
        fpsClock.tick(FPS)
        pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")

def about_menu():
    menu=True
    global catSpeed

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:

                if event.key==pygame.K_BACKSPACE:
                    main_menu()



        # Main Menu UI
        DISPLAYSURF.fill(BLUE)

        explanation=font.render("created by Hamit Taylan", 0, YELLOW)
        returnToMenu=font.render("Backspace to return to main menu", 0, YELLOW)

        explanation_rect=explanation.get_rect()
        return_rect =returnToMenu.get_rect()

        DISPLAYSURF.blit(explanation,(width/2 - (explanation_rect[2]/2), 300))
        DISPLAYSURF.blit(returnToMenu,(width/2 - (return_rect[2]/2), 400))

        pygame.display.update()
        fpsClock.tick(FPS)
        pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")


main_menu()
