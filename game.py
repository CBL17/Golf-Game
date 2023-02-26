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
Hole1 = Hole("utils/Hole 1.png", DISPLAY)
bazinga = Ball(size)
player1 = Player(bazinga, "Emma")

Hole1.barrierCheck("cringe.txt")

#Game Loop
carryOn = True
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    #Game Logic
    Hole1.show()
    bazinga.drawBall(DISPLAY, (255,255,255))
    bazinga.barrierCheck()
    bazinga.move()
    bazinga.swing()
    
    #Frame/Sec
    pygame.display.flip()
    clock.tick(FRAME_RATE)
pygame.quit()