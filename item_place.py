from pico2d import *

class bomb_place:
    image = None
    def __init__(self):
        if bomb_place.image == None:
            bomb_place.image = load_image('resource\\bomb.png')
        self.y = 500
        self.x = 600

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass