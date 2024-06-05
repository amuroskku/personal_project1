import pygame
from pygame.locals import *

class Item():
    def __init__(self, coordX, coordY, screen, item_type):
        self.coordX = coordX
        self.coordY = coordY
        self.screen = screen
        self.item_type = item_type

    def itemDraw(self):
        if self.item_type == 1:
            pygame.draw.rect(self.screen, RED, [self.coordX, self.coordY, BRICK_WIDTH, BRICK_HEIGHT])  # Red heart
        elif self.item_type == 2:
            font = pygame.font.SysFont(None, 30)
            text_surface = font.render("NEW_BALL", True, WHITE)  # Display "NEW_BALL" text
            text_rect = text_surface.get_rect(center=(self.coordX + BRICK_WIDTH // 2, self.coordY + BRICK_HEIGHT // 2))
            self.screen.blit(text_surface, text_rect)

    def isContact(self, ball_pos):
        if (ball_pos[0] >= (self.loc[0] - BALL_RADIUS)) and (ball_pos[0] <= (self.loc[0] + BALL_RADIUS + BRICK_WIDTH)) \
                and (ball_pos[1] >= (self.loc[1] - BALL_RADIUS)) and (
                ball_pos[1] <= (self.loc[1] + BALL_RADIUS + BRICK_HEIGHT)):
            return True
        else:
            return False
