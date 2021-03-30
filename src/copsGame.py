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

startButtonXStart, startButtonXEnd = 250, 305
startButtonYStart, startButtonYEnd = 100, 135
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

def drawPlanet(planetSprite):
    global window
    window.blit(planetSprite, (0, 275))

def mainMenu():
    exitButton = font.render('Exit', True, white)
    window.blit(exitButton , (exitButtonXStart, exitButtonYStart))
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
            xMousePosition, yMousePosition = pygame.mouse.get_pos()
            # if on menuDisplay clicks on EXIT exit the game
            if exitButtonXStart <= xMousePosition <= exitButtonXEnd and exitButtonYStart <= yMousePosition <= exitButtonYEnd and menuDisp:
                pygame.quit()
                sys.exit()
            # if on menuDisplay and clicks on start then start
            elif 140 >= xMousePosition >= 75 and 100 <= yMousePosition <= 135 and menuDisp:
                menuDisp = False
            elif 260 >= xMousePosition >= 150 and 150 <= yMousePosition <= 185 and pauseDisp:
                pauseDisp = False
            elif 260 >= xMousePosition >= 150 and 250 <= yMousePosition <= 285 and pauseDisp:
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
