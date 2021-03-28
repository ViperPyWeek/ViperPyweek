import pygame


def init(sizeX, sizeY):
    global window
    window = pygame.display.set_mode((sizeX, sizeY))

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

