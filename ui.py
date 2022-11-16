from pico2d import *
import random
import game_world
import game_framework
list = []

from coin import Coin

class Life:
    image = None
    def __init__(self):
        if Life.image == None:
            Life.image = load_image('heart.png')
        self.y = 480
        global list
        self.x = random.choice([20, 50, 80])
        while self.x in list:
            self.x = random.choice([20, 50, 80])
        list.append(self.x)


    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def remove(self):
        game_world.remove_object(self)
    def handle_collision(boy, enemy, group):
        if group == 'boy:enemy':
            Life.remove()


