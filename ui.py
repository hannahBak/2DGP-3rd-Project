from pico2d import *
import random
import game_world
import game_framework

class Life1:
    image = None
    def __init__(self):
        if Life1.image == None:
            Life1.image = load_image('resource\\heart.png')
        self.y = 480
        self.x = 20

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass


class Life2:
    image = None
    def __init__(self):
        if Life2.image == None:
            Life2.image = load_image('resource\\heart.png')
        self.y = 480
        self.x = 50

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass


class Life3:
    image = None
    def __init__(self):
        if Life3.image == None:
            Life3.image = load_image('resource\\heart.png')
        self.y = 480
        self.x = 80

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass
