import pygame
import math
from hole import Hole
from player import Player
from ball import Ball

#Game Parameters
FRAME_RATE = 144
SCREENWIDTH  = 1280
SCREENHEIGHT = 720

#Game Initializers 
pygame.init()
clock = pygame.time.Clock()

#Screen Initialization
size = (SCREENWIDTH, SCREENHEIGHT)
DISPLAY = pygame.display.set_mode(size)

#Object Initializations
Hole1 = Hole("holes\Hole 1\Hole 1.png", "holes\Hole 1\hole1pts.txt", DISPLAY)
bazinga = Ball()
player1 = Player(bazinga, "Emma")

holeList = [Hole1]
playerList = [player1]

#Game Loop

for hole in holeList:
    for player in playerList:
            
        player.ball.x, player.ball.y = hole.startingPos()
        carryOn = True
        while carryOn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    carryOn = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    starting = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONUP:
                    player.ball.swing(starting, pygame.mouse.get_pos())

            hole.show()
            pygame.draw.circle(hole.DISPLAY, (255,255,255), (player.ball.x, player.ball.y), player.ball.radius)
            player.ball.VelocityChange()
            player.ball.move()


            #Frame/Sec
            pygame.display.flip()
            clock.tick(FRAME_RATE)
pygame.quit()