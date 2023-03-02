from pygame import Surface, image
from re import findall

class Hole:
    def __init__(self, background_file: str, filename: str, DISPLAY: Surface) -> None:
        self.background = image.load(background_file)
        self.DISPLAY = DISPLAY
        self.points = []

        with open(filename, 'r') as file:
            for line in file:
                self.points.append(list(map(int, findall(r'\d+', line))))

    def show(self):
        self.DISPLAY.blit(self.background, (0,0))
    
#TODO: Draw lines between points using multiple Arrays of Tuples
#      Also eventually make sure to have for loop check every ball in the course if it's over/on barriers
#      ^ There might be a better place to do this, but at least have the barriers created here
        #raise ValueError("Something")
    
    def startingPos(self) -> tuple:
        return (self.points[0][0],self.points[0][1])