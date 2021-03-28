import pygame
import sys

pygame.init()
# if make this into a library remember to change the window in draw functions
window = pygame.display.set_mode((400, 400))  # creating pygame window
pygame.display.set_caption("Space Force")
mars = pygame.image.load(r"Repo\ViperPyweek\src\assets\mars.png")


def rect(x, y, width, height, red=155, green=155, blue=155):  # rectangle drawing function
    pygame.draw.rect(window, (red, green, blue), (x, y, width, height))


def line(x1, y1, x2, y2, red=155, green=155, blue=155, strokeWeight=1):  # line drawing function
    pygame.draw.line(window, (red, green, blue),
                     (x1, y1), (x2, y2), strokeWeight)


def ellipse(x, y, width, height, red=155, green=155, blue=155):  # ellipse drawing function
    pygame.draw.ellipse(window, (red, green, blue), (x, y, width, height))


def triangle(x1, y1, x2, y2, x3, y3, red=155, green=155, blue=155):  # triangle drawing function
    pygame.draw.polygon(window, (red, green, blue),
                        ((x1, y1), (x2, y2), (x3, y3)))


# takes in a list of coordinates must be a list
def polygon(coorList, red=155, green=155, blue=255):
    coorListLen = len(coorList)
    if coorListLen % 2 != 0:
        return
    # the line below is taken from https://stackoverflow.com/questions/1624883/alternative-way-to-split-a-list-into-groups-of-n
    coorGen = zip(*(iter(coorList),) * 2)
    coorSets = list(coorGen)
    pygame.draw.polygon(window, (red, green, blue), (coorSets))


def drawPlanet(planetSprite):
    global window
    window.blit(planetSprite, (0, 275))


while True:
    for event in pygame.event.get():
        # if the user wants to quit(presses the X in top right)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    drawPlanet(mars) # weird blotch on it, when i take out of loop it disappears?
    angle = 90  # play around with this a bit
    # mars = pygame.transform.rotate(window, angle) # cant get it rotating right, try uncommenting this line to see current rotation
    pygame.display.update()  # updates the display


# load sprite of planet and rotate it
