import pygame

# main player class
class Player(object):
    def __init__(self,image, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 0 # incase we move the character forward or back
        self.walk = True
        self.walkCount = 0
        self.rect = image.get_rect()
        self.isJump = False
        self.shoot = False

    def draw(self, image, window):
        if not self.isJump:
            window.blit(pygame.transform.scale(image[self.walkCount], (self.width, self.height)), (self.x, self.y))
            self.walkCount += 1
            if self.walkCount == 3:
                self.walkCount = 0