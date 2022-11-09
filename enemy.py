from pico2d import *
import random

class Enemy:
    image = None

    def __init__(self):
        if Enemy.image == None:
            Enemy.image = load_image('smile_poop.png')
        self.y = 540
        self.x = random.randint(0, 720)
        self.speed = 20

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= self.speed
        if self.y < 0:
            self.y = 540
            self.x = random.randint(0, 720)
            self.speed += 1


class Angry_enemy:
    image = None

    def __init__(self):
        if Angry_enemy.image == None:
            Angry_enemy.image = load_image('angry_poop.png')
        self.y = 540
        self.x = random.randint(0, 720)
        self.speed = 20

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= self.speed
        if self.y < 0:
            self.y = 540
            self.x = random.randint(0, 720)
            self.speed += 1