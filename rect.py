import pygame
from pygame.locals import *

class Rect():
    # def __init__(self, window, screen):
        def __init__(self, screen):
                # self.window = window
                        self.screen = screen

                            def draw(self, loc):
                                    self.loc = loc
                                            pygame.draw.rect(self.screen, WHITE, [loc[0], loc[1], RECT_WIDTH, RECT_HEIGHT])

                                                def isContact(self, ball_pos):
                                                        if (ball_pos[0] >= self.loc[0]) and (ball_pos[0] <= (self.loc[0] + RECT_WIDTH)):
                                                                    # if (ball_pos[1] + BALL_RADIUS) >= self.loc[1]:
                                                                                if self.loc[1] <= (ball_pos[1] + BALL_RADIUS):
                                                                                                return True
                                                                                                        return False

                                                                                                            def isGameOver(self, ball_pos):
                                                                                                                    if ball_pos[1] >= 530:
                                                                                                                                return True
                                                                                                                                        return False

