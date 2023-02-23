import pygame
import math
from ball import Ball

pygame.init()

#Usuable Colors
BLACK = ( 0, 0, 0 )
WHITE = ( 255, 255, 255 )
GREEN = ( 0, 255, 0 )
RED   = ( 255, 0, 0 )

#Game Parameters
FPS = 144
SCREENWIDTH  = 1280
SCREENHEIGHT = 720

#Screen Initialization
size = (SCREENWIDTH, SCREENHEIGHT)
DISPLAY = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#Background
hole1 = pygame.image.load("utils\Hole 1.png")

#Ball Initialization
player1 = Ball(SCREENWIDTH, SCREENHEIGHT)

#Game Loop
carryOn = True
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
    #Tab Name
    pygame.display.set_caption(f'{clock.get_fps() :.0f}')

    #Game Logic
    DISPLAY.blit(hole1, (0,0))
    player1.draw(DISPLAY, WHITE)
    player1.barrierCheck()
    player1.move()
    player1.swing()
    
    #Frame/Sec
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()