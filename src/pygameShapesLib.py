import pygame

pygame.init()
# if i make this into a library remember to change the window in draw functions
window = pygame.display.set_mode((400, 400))  # creating pygame window
pygame.display.set_caption("Pygame game")


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
    # one line below is taken from https://stackoverflow.com/questions/1624883/alternative-way-to-split-a-list-into-groups-of-n
    coorGen = zip(*(iter(coorList),) * 2)
    coorSets = list(coorGen)
    pygame.draw.polygon(window, (red, green, blue), (coorSets))


gameLoop = True
while gameLoop:
    pygame.time.delay(100)
    for event in pygame.event.get():
        # if the user wants to quit(presses the X in top right)
        if event.type == pygame.QUIT:
            gameLoop = False
    rect(200, 200, 20, 20, red=255, green=0, blue=0)
    line(1, 1, 400, 400)
    ellipse(100, 100, 20, 20)
    triangle(200, 10, 200, 50, 350, 10)
    polygon([1, 1, 100, 40, 93, 86])
    pygame.display.update()  # updates the display

pygame.quit()
