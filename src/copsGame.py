import pygame
import sys
import shapesHelpers
import os

# TODO make stuff look nicer, add blocks behind selection, make buttons change color when hovered, shooting star background
print()
pygame.init()
window = pygame.display.set_mode((400, 400))  # creating pygame window
pygame.display.set_caption("Space Force")
# The below assets will need to be changed to your own paths atm
mars = pygame.image.load(r"Repo\ViperPyweek\src\assets\mars.png") 
splashScreen = pygame.image.load(r"Repo\ViperPyweek\src\assets\splashScreen.png").convert()
font = pygame.font.Font(r"Repo\ViperPyweek\src\assets\gameFont.ttf", 35)
shapesHelpers.init(window)
#font = pygame.font.SysFont('Corbel', 35)
menuDisp = True
pauseDisp = False
splashed = False
white = (255, 255, 255)


def drawPlanet(planetSprite):
    global window
    window.blit(planetSprite, (0, 275))

def mainMenu():
    exitButton = font.render('Exit', True, white)
    window.blit(exitButton , (170, 250))
    startButton = font.render('Start', True, white)
    window.blit(startButton , (160, 150))

def pauseScreen():
    shapesHelpers.rect(0, 0, 400, 400, red=0, green=0, blue=0)
    resumeButton = font.render('Resume', True, white)
    window.blit(resumeButton, (150, 150))
    menuButton = font.render('Main Menu', True, white)
    window.blit(menuButton, (130, 250))

def splashScrDisp():
    pressSpace = font.render('Press Space', True, white)
    window.blit(splashScreen, (0, 0))
    window.blit(pressSpace, (105, 300))

def inputMgmt():
    global pauseDisp, menuDisp, splashed
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if 260 >= mouse[0] >= 150 and 250 <= mouse[1] <= 285 and menuDisp and splashed:
                pygame.quit()
                sys.exit()
            elif 260 >= mouse[0] >= 150 and 150 <= mouse[1] <= 185 and menuDisp and splashed:
                menuDisp = False
            elif 260 >= mouse[0] >= 150 and 150 <= mouse[1] <= 185 and pauseDisp:
                pauseDisp = False
            elif 260 >= mouse[0] >= 150 and 250 <= mouse[1] <= 285 and pauseDisp:
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
            sys.exit()

while True: # gameloop
    pygame.time.wait(100)
    inputMgmt()
    if not splashed:
        splashScrDisp()
    if splashed:
        if not pauseDisp:
            shapesHelpers.rect(1, 1, 400, 400, red=0, green=0, blue=0)
        if not menuDisp and not pauseDisp:
            drawPlanet(mars)
        if menuDisp:
            mainMenu()
    pygame.display.update()  # updates the display
