import pygame
import math

class Ball:
    def __init__(self, width, height):
        self.SCREENWIDTH = width
        self.SCREENHEIGHT = height
        
        self.x = 90
        self.y = 360
        self.angle = 0
        self.velocity = 0

        self.radius = 10
        self.friction = 0.001
        self.newFriction = self.friction

        self.xvelocity = self.velocity * math.cos(math.radians(self.angle))
        self.yvelocity = self.velocity * math.sin(math.radians(self.angle))

    def drawBall(self, DISPLAY, COLOR):
        pygame.draw.circle(DISPLAY, COLOR, (self.x,self.y), self.radius)

    def move(self):
        
        #Position Changes
        self.x+= self.xvelocity
        self.y+= self.yvelocity

        #Velocity Dependent Retarding Force
        self.newFriction *= 1.01
        self.xvelocity *= math.exp(-self.newFriction)
        self.yvelocity *= math.exp(-self.newFriction)
    
    def barrierCheck(self):

        #Velocity Changes for outside border
        if (self.x > self.SCREENWIDTH-self.radius-1) or (self.x < self.radius+1):
            self.xvelocity *= -0.95
        if (self.y > self.SCREENHEIGHT-self.radius-1) or (self.y < self.radius+1):
            self.yvelocity *= -0.95

        #Velocity Changes for Hole 1
        if (self.x < 960+self.radius and (self.y < 240+self.radius or self.y > 480-self.radius) and (self.y > 240 and self.y < 480)):
            self.yvelocity *= -0.95
            self.xvelocity *= 0.95
        if (self.x < 960+self.radius and (self.y < 240+self.radius or self.y > 480-self.radius) and (self.x > 960)):
            self.xvelocity *= -0.95
            self.yvelocity *= 0.95        

    def swing(self):
        if(pygame.mouse.get_pressed()[0]):
            direction = pygame.mouse.get_pos()
            self.newFriction = self.friction
            self.xvelocity = -5*math.cos(math.atan2(direction[1]-self.y, direction[0]-self.x))
            self.yvelocity = -5*math.sin(math.atan2(direction[1]-self.y, direction[0]-self.x))