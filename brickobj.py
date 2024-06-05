import pygame
from pygame.locals import *

class BrickObj():
    # Note : position of default parameter
    def __init__(self, coordX, coordY, screen):
        self.coordX = coordX
        self.coordY = coordY
        self.screen = screen

    def brickDraw(self):
        self.loc = [self.coordX, self.coordY]
        pygame.draw.rect(self.screen, BLUE1, [self.coordX, self.coordY, BRICK_WIDTH, BRICK_HEIGHT])

    def isContact(self, ball_pos):
        if (ball_pos[0] >= (self.loc[0] - BALL_RADIUS)) and (ball_pos[0] <= (self.loc[0] + BALL_RADIUS + BRICK_WIDTH)) \
                and (ball_pos[1] >= (self.loc[1] - BALL_RADIUS)) and (
                ball_pos[1] <= (self.loc[1] + BALL_RADIUS + BRICK_HEIGHT)):
            return True
        else:
            return False
