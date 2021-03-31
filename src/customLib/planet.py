def drawPlanet(planetSprite, window):
    """
    This function draws the planet sprite that was loaded 
    in the position that will be used for the game, this
    is needed as there will be multiple levels with different
    planet sprites
    """
    window.blit(planetSprite, (0, 275))


def rotatePlanet(planet, acceleration, pygame):  # https://www.pygame.org/wiki/RotateCenter?parent=CookBook
    """
    This function takes in the planet sprite and velocity that
    is desired for rotation, negative velocity will move the
    opposite direction, set the initial planet equal to the
    return of this function
    """
    origPlanet = planet.get_rect()
    accel = acceleration.accelerate()
    rotatedPlanet = pygame.transform.rotate(planet, accel)
    planetRect = origPlanet.copy()
    planetRect.center = rotatedPlanet.get_rect().center
    finalRotate = rotatedPlanet.subsurface(planetRect).copy()
    return finalRotate