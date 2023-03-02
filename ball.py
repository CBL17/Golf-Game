from pygame import Surface, draw, mouse
import math

class Ball:
    x = 0
    y = 0
    angle = 0
    velocity = 0
    radius = 10
    FRICTION = 0.001
    newFriction = 0
    xvelocity = velocity * math.cos(math.radians(angle))
    yvelocity = velocity * math.sin(math.radians(angle))

    def move(self):
        
        #Position Changes
        self.x+= self.xvelocity
        self.y+= self.yvelocity

        #Velocity Dependent Retarding Force
        self.newFriction *= 1.01
        self.xvelocity *= math.exp(-self.newFriction)
        self.yvelocity *= math.exp(-self.newFriction)
    
#TODO remove barrier checks but add bounces (velocity changes)

    # def xVelocityChange(self) -> None:

        # self.xvelocity *= -0.95
        # self.yvelocity *= 0.95

    def VelocityChange(self) -> None:

        # self.yvelocity *= -0.95
        # self.xvelocity *= 0.95

        #Velocity Changes for outside border
        if (self.x > 1280 - self.radius-1) or (self.x < self.radius+1):
            self.xvelocity *= -0.95
        if (self.y > 720 - self.radius-1) or (self.y < self.radius+1): 
            self.yvelocity *= -0.95

        #Velocity Changes for Hole 1
        if (self.x < 960+self.radius and (self.y < 240+self.radius or self.y > 480-self.radius) and (self.y > 240 and self.y < 480)):
            self.yvelocity *= -0.85
            self.xvelocity *= 0.85
        if (self.x < 960+self.radius and (self.y < 240+self.radius or self.y > 480-self.radius) and (self.x > 960)):
            self.xvelocity *= -0.85
            self.yvelocity *= 0.85

    def swing(self, direction: tuple, direction2: tuple) -> None:
        self.newFriction = self.FRICTION
        dx = direction2[0]-direction[0]
        dy = direction2[1]-direction[1]
        power = math.sqrt(dx*dx + dy*dy)
        self.xvelocity = power * -0.015 * math.cos(math.atan2(direction2[1]-direction[1], direction2[0]-direction[0]))
        self.yvelocity = power * -0.015 * math.sin(math.atan2(direction2[1]-direction[1], direction2[0]-direction[0]))