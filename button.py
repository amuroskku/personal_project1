import pygame
from pygame.locals import *

class Button():
    def __init__(self, button, window, screen, brickNum):
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 25)
        self.button = button
        self.brickNum = brickNum
        self.window = window
        self.screen = screen

    def _detYCoord(self, num):
        for idx in range(0, 20):
            if num >= (idx * 10) and num < ((idx + 1) * 10):
                return 50 + idx * BRICK_HEIGHT

    def game_Start(self):
        store = []
        random_prob = random.random()
        while True:
            if len(store) == self.brickNum+2:
                break
            else:
                cand = random.randint(0, NUM_LOC - 1)
                if cand not in store:
                    store.append(cand)

        brickSet = []
        PkmSet = []
        jir_set = []
        item_set = []
        for idx in range(self.brickNum):
            brickX = (store[idx] % BRICK_NUM_ROW) * BRICK_WIDTH + 50
            brickY = self._detYCoord(store[idx])

            tbrick = BrickObj(brickX, brickY, self.screen)
            tbrick.brickDraw()
            brickSet.append(tbrick)
        PkmX =  (store[-1] % BRICK_NUM_ROW) * BRICK_WIDTH + 50
        PkmY = self._detYCoord(store[-1])
        Pkmbrick = Pkm(PkmX, PkmY, self.screen)
        PkmSet.append(Pkmbrick)
        if random_prob > 0.8:
            Pkmbrick.drawCE()
        JirX = (store[-2] % BRICK_NUM_ROW) * BRICK_WIDTH + 50
        JirY = self._detYCoord(store[-2])
        Jirbrick = Pkm(JirX, JirY, self.screen)
        jir_set.append(Jirbrick)
        if Jir_num >= 70:
            Jirbrick.drawJI()
        oBall = Ball(self.screen, WHITE)
        oBall.drawBall(BALL_ORG_X, BALL_ORG_Y)
        for i in range(2):  # You can adjust the number of items created
            itemX = random.randint(50, 250)  # Random x-coordinate
            itemY = random.randint(50, 400)  # Random y-coordinate
            itemType = random.randint(1, 2)  # Random item type (1 or 2)
            item = Item(itemX, itemY, self.screen, itemType)
            item_set.append(item)

        return Org_X, Org_Y, brickSet, PkmSet, jir_set, oBall, item_set

    def handleEvent(self, eventObj, textButtonRect):
        if eventObj.type == pygame.MOUSEBUTTONDOWN:
            return textButtonRect.collidepoint(eventObj.pos)
        else:
            return False

    def endGame(self, curNumBricks):
        resultxt = "You smashed " + str(curNumBricks) + " bricks."
        textSurface = self.font.render(resultxt, True, WHITE)
        self.window.blit(textSurface, [100, 100])