import pygame

class Hole:
    def __init__(self, filename: str) -> None:
        self.background = pygame.image.load(filename)
        self.DISPLAY = pygame.display.set_mode([1280,720])
    def show(self):
        self.DISPLAY.blit(self.background, (0,0))