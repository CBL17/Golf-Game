from pygame import Surface, image
from re import findall

class Hole:
    def __init__(self, background_file: str, DISPLAY: Surface) -> None:
        self.background = image.load(background_file)
        self.DISPLAY = DISPLAY

    def show(self):
        self.DISPLAY.blit(self.background, (0,0))
    
#TODO: Draw lines between points using multiple Arrays of Tuples
#      Also eventually make sure to have for loop check every ball in the course if it's over/on barriers
#      ^ There might be a better place to do this, but at least have the barriers created here

#      Also need to use map() to convert string(s) to tuple(s)

    def barrierCheck(self, filename: str) -> None:
        array = []
        i = 0
        file = open(filename, 'r')
        for line in file:
            array.append(list(map(int, findall(r'\d+', line))))
        print(array)

        #raise ValueError("Something")