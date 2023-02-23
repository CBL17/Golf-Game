import pygame
import math

#Usuable Colors
GREY  = ( 210, 210, 210 ) 
BLACK = ( 0, 0, 0 )
WHITE = ( 255, 255, 255 )
GREEN = ( 0, 255, 0 )
RED   = ( 255, 0, 0 )

class Ball:
    def __init__(self):
        self.x = 30
        self.y = 360
        self.angle = 0
        self.velocity = 0
        self.radius = 10
        self.friction = 0.001
        self.newFriction = self.friction

        self.xvelocity = self.velocity * math.cos(math.radians(self.angle))
        self.yvelocity = self.velocity * math.sin(math.radians(self.angle))

    def draw(self):
        pygame.draw.circle(DISPLAY, RED, (self.x,self.y), self.radius)

    def move(self):
        
        #Position Changes
        self.x+= self.xvelocity
        self.y+= self.yvelocity

        #Velocity Changes for outside border
        if (self.x > SCREENWIDTH-self.radius) or (self.x < self.radius):
            self.xvelocity *= -0.95
        if (self.y > SCREENHEIGHT-self.radius) or (self.y < self.radius):
            self.yvelocity *= -0.95

        #Velocity Changes for Hole 1
        if (self.x < 961+self.radius and (self.y < 241+self.radius or self.y > 479-self.radius) and (self.y > 240 and self.y < 480)):
            self.yvelocity *= -0.95
        if (self.x < 961+self.radius and (self.y < 241+self.radius or self.y > 479-self.radius) and (self.x > 960)):
            self.xvelocity *= -0.95

        #Velocity Dependent Retarding Force
        self.newFriction *= 1.01
        self.xvelocity *= math.exp(-self.newFriction)
        self.yvelocity *= math.exp(-self.newFriction)
        

    def swing(self):
        print(f'{self.x : .2f}', f'{self.y : .2f}')
        if pygame.mouse.get_pressed()[0]:
            direction = pygame.mouse.get_pos()
            self.newFriction = self.friction
            self.xvelocity = 3*math.cos(math.atan2(direction[1]-self.y, direction[0]-self.x))
            self.yvelocity = 3*math.sin(math.atan2(direction[1]-self.y, direction[0]-self.x))

pygame.init()

#Screen Initialization
SCREENWIDTH  = 1280
SCREENHEIGHT = 720
size = (SCREENWIDTH, SCREENHEIGHT)
DISPLAY = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#Background
hole1 = pygame.image.load("utils\Hole 1.png")

#Game Parameters
FPS = 144

#Ball Initialization
player1 = Ball()

#Game
carryOn = True
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
            
    #Game Logic
    DISPLAY.blit(hole1, (0,0))
    pygame.display.set_caption(f'{clock.get_fps() :.0f}')
    player1.draw()
    player1.move()
    player1.swing()

    #Frame/Sec
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()