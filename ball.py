import pygame
from pygame.locals import *

class Ball():
    def __init__(self, screen, color, centerX=BALL_ORG_X, centerY=BALL_ORG_Y):
        self.centerX = centerX
        self.centerY = centerY
        self.screen = screen
        self.color = color

    def drawBall(self, coord_X=BALL_ORG_X, coord_Y=BALL_ORG_Y):
        pygame.draw.circle(self.screen, self.color, [coord_X, coord_Y], BALL_RADIUS)

    def retPos(self):
        return self.centerX, self.centerY