import pygame
from pygame import draw
from hole import Hole
from player import Player

class Turn:
    def __init__(self, hole: Hole, player: Player) -> None:
        self.hole = hole
        self.player = player
    
    def start(self) -> None:
        self.hole.show()
        draw.circle(self.hole.DISPLAY, (255,255,255), self.hole.startingPos(), self.player.ball.radius)
        self.player.ball.swing()
        #all ball physics probably need to be done in the ball class
        #possibly w/o being called elsewhere