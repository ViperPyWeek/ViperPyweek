import pygame
import sys
import shapesHelpers

pygame.init()
window = pygame.display.set_mode((400, 400))  # creating pygame window
pygame.display.set_caption("Space Force")
mars = pygame.image.load(r"Repo\ViperPyweek\src\assets\mars.png")
#shapesHelpers.init(window)
#shapesHelpers.line(1, 1, 400, 400) # shapehelpers is working

def drawPlanet(planetSprite):
    global window
    window.blit(planetSprite, (0, 275))

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
        # if the user wants to quit(presses the X in top right)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    drawPlanet(mars) # weird blotch on it, when i take out of loop it disappears?
    angle = -1  # play around with this a bit
    mars = rotatePlanet(mars, angle)
    pygame.display.update()  # updates the display
