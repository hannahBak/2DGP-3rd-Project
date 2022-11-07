from pico2d import *

class Bath:
    def __init__(self):
        self.bath = load_image('bath.png')

    def draw(self):
        self.bath.draw(360, 270)


    def update(self): pass