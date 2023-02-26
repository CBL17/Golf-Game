from pygame import Surface, image

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
        self.file = open(filename)
        points = [line.split(" ") for line in self.file.readlines()]
        print(points[0][0])
        #raise ValueError("Something")