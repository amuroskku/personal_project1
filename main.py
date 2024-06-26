import pygame
from pygame.locals import *
import sys
import pygwidgets
import random, math
from ball import Ball
from rect import Rect
from button import Button
from brickobj import BrickObj
from pkm import Pkm
from items import Item

LIGHT_GRAY = (197, 250, 250)
RED - (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (219, 72, 41)
CELEBI = (200, 247, 203)
JIRACHI = (249, 255, 194)
Jir_num = 0
jirachi_count = 0
BLUE1 = (0, 138, 230)
LIFE = 3

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 680
FRAMES_PER_SECOND = 30
SCREEN_SIZE = [400, 400]

LEADERBOARD_WIDTH = 400
LEADERBOARD_HEIGHT = 500
display_leaderboard = False
font = pygame.font.Font(None, 36)

Ref_X = 250
Ref_Y = 500
Org_X = 250
Org_Y = 500
BALL_ORG_X = 300
BALL_ORG_Y = 400

BRICK_HEIGHT = 20
BRICK_WIDTH = 50

BRICK_NUM_ROW = 10

RECT_WIDTH = 100
RECT_HEIGHT = 20

NUM_BRICKS = 3
NUM_LOC = 200
BALL_RADIUS = 8
SCORE = 0
scores = []

leaderscreen = pygame.display.set_mode((LEADERBOARD_WIDTH, LEADERBOARD_HEIGHT))
screen = pygame.display.set_mode(SCREEN_SIZE)


ce_1 = pygame.image.load("images/ceframe1.gif")
ce_2 = pygame.image.load("images/ceframe2.gif")
ce_3 = pygame.image.load("images/ceframe3.gif")
ce_4 = pygame.image.load("images/ceframe4.gif")
ce_5 = pygame.image.load("images/ceframe5.gif")
ce_6 = pygame.image.load("images/ceframe6.gif")
ce_7 = pygame.image.load("images/ceframe7.gif")
ce_8 = pygame.image.load("images/ceframe8.gif")
ce_9 = pygame.image.load("images/ceframe9.gif")
ce_10 = pygame.image.load("images/ceframe10.gif")
ce_11 = pygame.image.load("images/ceframe11.gif")
ce_12 = pygame.image.load("images/ceframe12.gif")
ce_13 = pygame.image.load("images/ceframe13.gif")
ce_14 = pygame.image.load("images/ceframe14.gif")
ce_15 = pygame.image.load("images/ceframe15.gif")

ji_1 = pygame.image.load("images/jiframe1.gif")
ji_2 = pygame.image.load("images/jiframe2.gif")
ji_3 = pygame.image.load("images/jiframe3.gif")
ji_4 = pygame.image.load("images/jiframe4.gif")
ji_5 = pygame.image.load("images/jiframe5.gif")
ji_6 = pygame.image.load("images/jiframe6.gif")
ji_7 = pygame.image.load("images/jiframe7.gif")
ji_8 = pygame.image.load("images/jiframe8.gif")
ji_9 = pygame.image.load("images/jiframe9.gif")
ji_10 = pygame.image.load("images/jiframe10.gif")
ji_11 = pygame.image.load("images/jiframe11.gif")
ji_12 = pygame.image.load("images/jiframe12.gif")
ji_13 = pygame.image.load("images/jiframe13.gif")


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

oInputField = pygwidgets.InputText(window, (100, 230), value='Enter your name: ', fontSize=30)

oButton1 = pygwidgets.TextButton(window, (100, 600), 'Start', upColor=(57, 158, 158), overColor=(197, 250, 250), downColor=(195, 227, 227))
bttn1Rect = oButton1.getRect()
oButton2 = pygwidgets.TextButton(window, (400, 600), 'Reset', upColor=(57, 158, 158), overColor=(197, 250, 250), downColor=(195, 227, 227))
bttn2Rect = oButton2.getRect()
oButton3 = pygwidgets.TextButton(window, (250, 600), 'Next', upColor=(57, 158, 158), overColor=(197, 250, 250), downColor=(195, 227, 227))
bttn3Rect = oButton3.getRect()
oRef = Rect(screen)
ctrlButton = Button(oButton1, window, screen, NUM_BRICKS)

N_PIXELS_TO_MOVE = 20
BALL_PIXELS_TO_MOVE = 8
oBall = Ball(screen, WHITE)
brickSet = []
ballPos = [BALL_ORG_X, BALL_ORG_Y]
xSpeed = 0
ySpeed = BALL_PIXELS_TO_MOVE
GAME_START = False
curNumBrick = NUM_BRICKS
while True:
    for event in pygame.event.get():
        TextDraw = False
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if ctrlButton.handleEvent(event, bttn1Rect):
            random_prob = random.random()
            Ref_X, Ref_Y, brickSet, PkmSet, jir_set, oBall, item_set = ctrlButton.game_Start()
            ballPos = [BALL_ORG_X, BALL_ORG_Y]
            xSpeed = 0
            ySpeed = BALL_PIXELS_TO_MOVE
            curNumBrick = NUM_BRICKS
            GAME_START = True
            PKMHELPED = False
            Jir_num = 0
            SCORE = 0
            jirachi_count = 0

        if ctrlButton.handleEvent(event, bttn2Rect): # Game reset
            oInputField.draw()
            for event in pygame.event.get():
                if oInputField.handleEvent(event):
                    userText = oInputField.getText()
                    UserTextInput = True
                    rStr = userText.split(' ')
                    name = rStr[len(rStr) - 1]
            scores.append({'NAME ': name, 'SCORE ': SCORE})
            screen.fill((0, 0, 0))
            pygame.display.flip()
            NUM_BRICKS = 3
            ctrlButton = Button(oButton1, window, screen, NUM_BRICKS)
            GAME_START = False
            ballPos = [BALL_ORG_X, BALL_ORG_Y]
            xSpeed = 0
            ySpeed = BALL_PIXELS_TO_MOVE
            curNumBrick = NUM_BRICKS
            ToNext = False
            PKMHELPED = False
            Jir_num = 0
            SCORE = 0
            jirachi_count = 0
            UserTextInput = False

        if ctrlButton.handleEvent(event, bttn3Rect):
            if ToNext == True:
                NUM_BRICKS += 2
                random_prob = random.random()
                ctrlButton = Button(oButton1, window, screen, NUM_BRICKS)
                Ref_X, Ref_Y, brickSet, PkmSet,jir_set, oBall, item_set = ctrlButton.game_Start()
                ballPos = [BALL_ORG_X, BALL_ORG_Y]
                xSpeed = 0
                ySpeed = BALL_PIXELS_TO_MOVE
                curNumBrick = NUM_BRICKS
                GAME_START = True
                ToNext = False
                PKMHELPED = False
                Jir_num = 0
                jirachi_count = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if Ref_X >= 53:
                    Ref_X = Ref_X - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_RIGHT:
                if Ref_X <= 440:
                    Ref_X = Ref_X + N_PIXELS_TO_MOVE
            elif event.key == pygame.K_l:
                display_leaderboard = not display_leaderboard

    window.fill(LIGHT_GRAY)

    oButton1.draw()
    oButton2.draw()
    pygame.draw.rect(screen, BLACK, [50, 50, 500, 500])
    oRef.draw((Ref_X, Ref_Y))

    if display_leaderboard:
        # Sort the scores by score in descending order
        scores.sort(key=lambda x: x['SCORE '], reverse=True)

        # Clear the screen
        leaderscreen.fill(BLACK)

        # Display the scores
        y = 50
        for score in scores:
            text = f"{score['NAME ']}: {score['SCORE ']}"
            text_surface = font.render(text, True, BLUE1)
            screen.blit(text_surface, (50, y))
            y += 50

        # Update the display
        pygame.display.flip()

    if GAME_START == True:
        levtxt = "Level " + str(NUM_BRICKS//2)
        levSurface = ctrlButton.font.render(levtxt, True, BLACK)
        ctrlButton.window.blit(levSurface, [270, 25])
        scoretext = "SCORE  " +str(SCORE)
        scoreSurface = ctrlButton.font.render(scoretext, True, WHITE)
        ctrlButton.window.blit(scoreSurface, [50, 50])
        for i in range(len(brickSet)):
            brickSet[i].brickDraw()
        if len(PkmSet) >= 1:
            if random_prob > 0.8:
                PkmSet[0].drawCE()
        if Jir_num >= 70:
            if len(jir_set) >=1:
                jir_set[0].drawJI()
        for i in item_set:
            item.itemDraw()
        for item in itemSet:
        if item.isContact(ballPos):
            if item.item_type == 1:  # Adding life
                pass
            elif item.item_type == 2:  # Add new ball
                pass
            itemSet.remove(item)
        if oRef.isContact(ballPos) == True:
            if (ballPos[0] - Ref_X) <= 0.5 * RECT_WIDTH:
                changeRate = (RECT_WIDTH * 0.5 - (ballPos[0] - Ref_X)) / (RECT_WIDTH * 0.5)
                xSpeed = -changeRate * BALL_PIXELS_TO_MOVE
            else:
                changeRate = (ballPos[0] - Ref_X - RECT_WIDTH * 0.5) / (RECT_WIDTH * 0.5)
                xSpeed = changeRate * BALL_PIXELS_TO_MOVE
            ySpeed = -ySpeed
        elif (ballPos[0] <= 50 + BALL_RADIUS) or (ballPos[0] >= 550 - BALL_RADIUS):
            xSpeed = -xSpeed
            ySpeed = ySpeed
        elif (ballPos[1] <= 50 + BALL_RADIUS):
            ySpeed = -ySpeed
        elif curNumBrick <= 0:
            ctrlButton.endGame(NUM_BRICKS - curNumBrick)
            if PKMHELPED == 'celebi':
                victxt = "Celebi helped blow away the bricks!"
                vicSurface = ctrlButton.font.render(victxt, True, CELEBI)
            elif PKMHELPED =='jirachi':
                victxt = "Jirachi broke " + str(jirachi_count) + " bricks for you!"
                vicSurface = ctrlButton.font.render(victxt, True, JIRACHI)
            else:
                victxt = "You win! Congrats!"
                vicSurface = ctrlButton.font.render(victxt, True, WHITE)
            ctrlButton.window.blit(vicSurface, [100, 130])
            xSpeed = 0
            ySpeed = 0
            oButton3.draw()
            ToNext = True
        elif oRef.isGameOver(ballPos) == True:
            ctrlButton.endGame(NUM_BRICKS - curNumBrick)
            overtxt = "You lose."
            overSurface = ctrlButton.font.render(overtxt, True, WHITE)
            ctrlButton.window.blit(overSurface, [100, 130])
            xSpeed = 0
            ySpeed = 0
            ctrlButton = Button(oButton1, window, screen, NUM_BRICKS)
            ToNext = False
        else:
            for brickObj in brickSet:
                if brickObj.isContact(ballPos) == True:
                    xSpeed = -xSpeed
                    ySpeed = -ySpeed
                    brickSet.remove(brickObj)
                    curNumBrick = curNumBrick - 1
                    if Jir_num < 70:
                        Jir_num = Jir_num + random.randint(20, 60)
                    SCORE = SCORE + (NUM_BRICKS//2) * 100
                    break
            for x in PkmSet:
                if random_prob > 0.8:
                    if x.isContact(ballPos) == True:
                        xSpeed = -xSpeed
                        ySpeed = -ySpeed
                        PkmSet.remove(x)

                        screen.fill(CELEBI)
                        screen.blit(ce_1, (50, 150))
                        pygame.display.flip()
                        pygame.time.delay(100)

                        screen.blit(ce_2, (50, 150))
                        pygame.display.flip()
                        pygame.time.delay(100)

                        screen.blit(ce_3, (50, 150))
                        pygame.display.flip()
                        pygame.time.delay(100)

                        screen.blit(ce_4, (50, 150))
                        pygame.display.flip()
                        pygame.time.delay(100)

                        screen.blit(ce_5, (50, 150))
                        pygame.display.flip()
                        pygame.time.delay(100)

                        screen.blit(ce_6, (50, 150))
                        pygame.display.flip()
                        pygame.time.delay(100)

                        screen.blit(ce_7, (50, 150))
                        pygame.display.flip()
                        pygame.time.delay(100)

                        screen.blit(ce_8, (50, 150))
                        pygame.display.flip()
                        pygame.time.delay(100)

                        screen.blit(ce_9, (50, 150))
                        pygame.display.flip()
                        pygame.time.delay(100)

                        screen.blit(ce_10, (50, 150))
                        pygame.display.flip()
                        pygame.time.delay(100)

                        screen.blit(ce_11, (50, 150))
                        pygame.display.flip()
                        pygame.time.delay(100)

                        screen.blit(ce_12, (50, 150))
                        pygame.display.flip()
                        pygame.time.delay(100)

                        screen.blit(ce_13, (50, 150))
                        pygame.display.flip()
                        pygame.time.delay(100)

                        screen.blit(ce_14, (50, 150))
                        pygame.display.flip()
                        pygame.time.delay(100)

                        screen.blit(ce_15, (50, 150))
                        pygame.display.flip()
                        pygame.time.delay(100)

                        screen.fill((0, 0, 0))
                        pygame.display.flip()

                        brickSet = []
                        PKMHELPED = 'celebi'
                        curNumBrick = 0
                        SCORE = SCORE + NUM_BRICKS * 1500
                        break
                for x in jir_set:
                    if Jir_num >= 70:
                        if x.isContact(ballPos) == True:
                            xSpeed = -xSpeed
                            ySpeed = -ySpeed
                            jir_set.remove(x)

                            screen.fill(JIRACHI)
                            screen.blit(ji_1, (50, 150))
                            pygame.display.flip()
                            pygame.time.delay(130)

                            screen.blit(ji_2, (50, 150))
                            pygame.display.flip()
                            pygame.time.delay(130)

                            screen.blit(ji_3, (50, 150))
                            pygame.display.flip()
                            pygame.time.delay(130)

                            screen.blit(ji_4, (50, 150))
                            pygame.display.flip()
                            pygame.time.delay(130)

                            screen.blit(ji_5, (50, 150))
                            pygame.display.flip()
                            pygame.time.delay(130)

                            screen.blit(ji_6, (50, 150))
                            pygame.display.flip()
                            pygame.time.delay(130)

                            screen.blit(ji_7, (50, 150))
                            pygame.display.flip()
                            pygame.time.delay(130)

                            screen.blit(ji_8, (50, 150))
                            pygame.display.flip()
                            pygame.time.delay(130)

                            screen.blit(ji_9, (50, 150))
                            pygame.display.flip()
                            pygame.time.delay(130)

                            screen.blit(ji_10, (50, 150))
                            pygame.display.flip()
                            pygame.time.delay(130)

                            screen.blit(ji_11, (50, 150))
                            pygame.display.flip()
                            pygame.time.delay(130)

                            screen.blit(ji_12, (50, 150))
                            pygame.display.flip()
                            pygame.time.delay(130)

                            screen.blit(ji_13, (50, 150))
                            pygame.display.flip()
                            pygame.time.delay(130)

                            screen.fill((0, 0, 0))
                            pygame.display.flip()

                            PKMHELPED = 'jirachi'
                            for x in range(3):
                                if len(brickSet) >= 1:
                                    brickSet.remove(brickSet[0])
                                    curNumBrick = curNumBrick -1
                                    jirachi_count += 1
                            SCORE = SCORE + 1000 * jirachi_count
                            Jir_num = 0
                            break



        ballPos[0] = ballPos[0] + xSpeed
        ballPos[1] = ballPos[1] + ySpeed

        oBall.drawBall(ballPos[0], ballPos[1])

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
