import pygame
from ball import Ball

class Player:
    def __init__(self, ball: Ball, name: str):
        self.ball = ball
        self.name = name

        self.strokes = 0
        self.score = 0