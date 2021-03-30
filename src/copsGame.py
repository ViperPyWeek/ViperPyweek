import pygame
import sys
import shapesHelpers
import os


"""
MAKING CONSTANT VARIABLES FOR BUTTON BOUNDS
WE CAN DO IT IN OTHER FILE OR LOCATION
"""

# vars start

exitButtonXStart, exitButtonXEnd = 250, 305
exitButtonYStart, exitButtonYEnd = 100, 135

startButtonXStart, startButtonXEnd = 75, 140
startButtonYStart, startButtonYEnd = 100, 135

resumeButtonXStart, resumeButtonXEnd = 150, 260
resumeButtonYStart, resumeButtonYEnd = 130, 185


mainMenuButtonXStart, mainMenuButtonXEnd = 150, 260
mainMenuButtonYStart, mainMenuButtonYEnd = 250, 285

# vars end


pygame.init()
window = pygame.display.set_mode((400, 400))  # creating pygame window
pygame.display.set_caption("Space Force")
mars = pygame.image.load(os.path.join('src/assets', 'mars.png'))
shapesHelpers.init(window)
font = pygame.font.SysFont('Corbel', 35)
menuDisp = True
pauseDisp = False
white = (255, 255, 255)
black = (0, 0, 0)

def drawPlanet(planetSprite):
    global window
    window.blit(planetSprite, (0, 275))

def mainMenu():
    exitButton = font.render('Exit', True, white)
    window.blit(exitButton , (exitButtonXStart, exitButtonYStart))
    startButton = font.render('Start', True, white)
    window.blit(startButton , (startButtonXStart, startButtonYStart))

def pauseScreen():
    shapesHelpers.rect(0, 0, 400, 400, red=0, green=0, blue=0)
    resumeButton = font.render('Resume', True, white)
    window.blit(resumeButton, (resumeButtonXStart, resumeButtonYStart))
    menuButton = font.render('Main Menu', True, white)
    window.blit(menuButton, (mainMenuButtonXStart, mainMenuButtonYStart))

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
            xMousePosition, yMousePosition = pygame.mouse.get_pos()
            # we can just check state wise instead of checking step each time, it will be more splitted
            if menuDisp:
                # if clicks on EXIT exit the game
                if exitButtonXStart <= xMousePosition <= exitButtonXEnd and exitButtonYStart <= yMousePosition <= exitButtonYEnd:
                    pygame.quit()
                    sys.exit()
                # if on menuDisplay and clicks on start then start
                elif startButtonXStart <= xMousePosition <= startButtonXEnd and startButtonYStart <= yMousePosition <= startButtonYEnd:
                    menuDisp = False
            elif pauseDisp:
                if resumeButtonXStart <= xMousePosition <= resumeButtonXEnd and resumeButtonYStart <= yMousePosition <= resumeButtonYEnd:
                    pauseDisp = False
                elif mainMenuButtonXStart <= xMousePosition <= mainMenuButtonXEnd and mainMenuButtonYStart <= yMousePosition <= mainMenuButtonYEnd:
                    pauseDisp = False
                    menuDisp = True
        elif event.type == pygame.KEYDOWN:
            if not menuDisp and pygame.K_ESCAPE and pauseDisp:
                pauseDisp = False
            elif not menuDisp and pygame.K_ESCAPE:
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
    elif pauseDisp:
        pauseScreen()
    pygame.display.update()  # updates the display
    window.fill(black)
