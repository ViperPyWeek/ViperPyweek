# Default libraries
from customLib.planet import *
import pygame
from sys import exit
from requests import get
from io import BytesIO
import os

# Classes
from classes.acceleration import Acceleration
from classes import player as hero

# Custom libraries
from customLib.constants import *

# library initializations
pygame.init()

window = pygame.display.set_mode(
    (WIN_WIDTH, WIN_HEIGHT))  # creating pygame window
pygame.display.set_caption('Space Force Cops')


def loadImage(fileName):
    return pygame.image.load('src' + os.sep + 'assets' + os.sep + fileName)


def linkToFile(hostLink):
    img = get(hostLink)
    convertImg = BytesIO(img.content)
    return pygame.image.load(convertImg)


def loadFont(hostLink):
    file = get(hostLink)
    convert = BytesIO(file.content)
    return pygame.font.Font(convert, 35)


# pygame constants

try:
    MARSIMG = loadImage('mars.png')
except:
    MARSIMG = linkToFile(
        'https://github.com/ViperPyWeek/gameAssets/blob/main/mars.png')

try:
    SPLASHIMG = loadImage('splashScreen.png').convert()
except:
    SPLASHIMG = linkToFile(
        'https://github.com/ViperPyWeek/gameAssets/blob/main/splashScreen.png').convert()


try:
    FONT = pygame.font.Font('src' + os.sep + 'assets' +
                            os.sep + 'gameFont.ttf', 35)
except:
    FONT = loadFont(
        'https://github.com/ViperPyWeek/gameAssets/blob/main/gameFont.ttf')

try:
    COP_IMAGE = [
                 loadImage('cop' + os.sep + 'Walk' + os.sep + 'walk1.png'),
                 loadImage('cop' + os.sep + 'Walk' + os.sep + 'walk2.png'),
                 loadImage('cop' + os.sep + 'Walk' + os.sep + 'walk3.png')
                 ]
except:
    COP_IMAGE = [
                 linkToFile('https://github.com/ViperPyWeek/gameAssets/blob/main/cop/Walk/walk1.png'),
                 linkToFile('https://github.com/ViperPyWeek/gameAssets/blob/main/cop/Walk/walk2.png'),
                 linkToFile('https://github.com/ViperPyWeek/gameAssets/blob/main/cop/Walk/walk1.png')
                 ]


# Vars
accelRate = 1
iterCt = 0
menuDisp = True
pauseDisp = False
splashed = False
mars = MARSIMG

# create a cop using the player class
cop = hero.player(COP_IMAGE[0], COP_X, COP_Y, COP_WIDTH, COP_HEIGHT)

# Classes (before vars as some vars may depend on classes)

acceleration = Acceleration(0, 10, accelRate, pygame)

# methods for visualizing

# planet functions


# button and prompting functions


def mainMenu():
    '''Generates the main menu and buttons'''
    exitButton = FONT.render('Exit', True, WHITE)
    window.blit(exitButton, (EXITBUTTONXSTART, EXITBUTTONYSTART))
    startButton = FONT.render('Start', True, WHITE)
    window.blit(startButton, (STARTBUTTONXSTART, STARTBUTTONYSTART))


def pauseScreen():
    '''Generates the pause screen and buttons'''
    resumeButton = FONT.render('Resume', True, WHITE)
    window.blit(resumeButton, (RESUMEBUTTONXSTART, RESUMEBUTTONYSTART))
    menuButton = FONT.render('Main Menu', True, WHITE)
    window.blit(menuButton, (MENUBUTTONXSTART, MENUBUTTONYSTART))


def inputMgmt():
    '''Manages all input and events'''
    global pauseDisp, menuDisp, splashed
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            if menuDisp and splashed:
                # EXIT BUTTON
                if EXITBUTTONXSTART <= mouseX <= EXITBUTTONXEND and EXITBUTTONYSTART <= mouseY <= EXITBUTTONYEND:
                    pygame.quit()
                    exit()
                # START BUTTON
                elif STARTBUTTONXSTART <= mouseX <= STARTBUTTONXEND and STARTBUTTONXSTART <= mouseY <= STARTBUTTONXEND:
                    menuDisp = False
            elif pauseDisp:
                # RESUME
                if RESUMEBUTTONXSTART <= mouseX <= RESUMEBUTTONXEND and RESUMEBUTTONYSTART <= mouseY <= RESUMEBUTTONYEND:
                    pauseDisp = False
                if MENUBUTTONXSTART <= mouseX <= MENUBUTTONXEND and MENUBUTTONYSTART <= mouseY <= MENUBUTTONYEND:
                    pauseDisp = False
                    menuDisp = True
        if keys[pygame.K_ESCAPE] and not menuDisp and pauseDisp:
            pauseDisp = False
        elif not menuDisp and keys[pygame.K_ESCAPE]:
            pauseScreen()
            pauseDisp = True
        elif not splashed and keys[pygame.K_SPACE]:
            splashed = True
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()


# Other


def splashScrDisp():
    '''Generates splash screen at launch'''
    pressSpace = FONT.render('Press Space', True, WHITE)
    window.blit(SPLASHIMG, ORIGIN)
    window.blit(pressSpace, (105, 300))


def printAcceleration():
    global iterCt
    if iterCt < 1:
        try:
            print(acceleration)
            iterCt += 1
        except TypeError:
            pass

 # Mainloop


while True:
    pygame.time.wait(100)
    inputMgmt()
    if not splashed:
        splashScrDisp()
    if splashed:
        if not pauseDisp:
            window.fill(BLACK)
        if not menuDisp and not pauseDisp:
            drawPlanet(mars, window)
            mars = rotatePlanet(mars, acceleration, pygame)
            cop.draw(COP_IMAGE, window)
        if menuDisp:
            mainMenu()
    printAcceleration()
    pygame.display.update()  # updates the display
