import pygame
import sys
import shapesHelpers
import os

pygame.init()
window = pygame.display.set_mode((400, 400))  # creating pygame window
pygame.display.set_caption("Space Force")
mars = pygame.image.load(os.path.join('src/assets', 'mars.png'))
shapesHelpers.init(window)
font = pygame.font.SysFont('Corbel', 35)
menuDisp = True
pauseDisp = False
white = (255, 255, 255)

def drawPlanet(planetSprite):
    global window
    window.blit(planetSprite, (0, 275))

def mainMenu():
    exitButton = font.render('Exit', True, white)
    window.blit(exitButton , (250, 100))
    startButton = font.render('Start', True, white)
    window.blit(startButton , (75, 100))

def pauseScreen():
    shapesHelpers.rect(0, 0, 400, 400, red=0, green=0, blue=0)
    resumeButton = font.render('Resume', True, white)
    window.blit(resumeButton, (150, 150))
    menuButton = font.render('Main Menu', True, white)
    window.blit(menuButton, (130, 250))

def rotatePlanet(planet, angle): # https://www.pygame.org/wiki/RotateCenter?parent=CookBook
    origPlanet = planet.get_rect()
    rotatedPlanet = pygame.transform.rotate(planet, angle)
    planetRect = origPlanet.copy()
    planetRect.center = rotatedPlanet.get_rect().center
    finalRotate = rotatedPlanet.subsurface(planetRect).copy()
    return finalRotate

while True:
    pygame.time.wait(100)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if 305 >= mouse[0] >= 250 and 100 <= mouse[1] <= 135 and menuDisp:
                pygame.quit()
                sys.exit()
            elif 140 >= mouse[0] >= 75 and 100 <= mouse[1] <= 135 and menuDisp:
                menuDisp = False
            elif 260 >= mouse[0] >= 150 and 150 <= mouse[1] <= 185 and pauseDisp:
                pauseDisp = False
            elif 260 >= mouse[0] >= 150 and 250 <= mouse[1] <= 285 and pauseDisp:
                pauseDisp = False
                menuDisp = True
        elif event.type == pygame.KEYDOWN:
            if not menuDisp and pygame.K_ESCAPE and pauseDisp:
                pauseDisp = False
            elif not menuDisp and pygame.K_ESCAPE:
                pauseScreen()
                pauseDisp = True
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if not pauseDisp:
        shapesHelpers.rect(1, 1, 400, 400, red=0, green=0, blue=0)
    if not menuDisp and not pauseDisp:
        drawPlanet(mars)
        angle = 45  # play around with this a bit
        mars = rotatePlanet(mars, angle)
    if menuDisp:
        mainMenu()
    pygame.display.update()  # updates the display
    window.fill([0,0,0]) # black (consider storing in variable)
