from pico2d import *
import random
import game_framework
import game_world
import time

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KPH = 40.0  # 마라토너의 평속
RUN_SPEED_MPM = (RUN_SPEED_KPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Item:
    image = None

    def __init__(self):
        if Item.image == None:
            Item.image = load_image('resource\\bomb.png')
        self.y = 540
        self.x = random.randint(0, 720)
        self.dir = 1

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        Item.image = load_image('resource\\bomb.png')
        self.y -= self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.dir += 0.0001
        if self.y < 0:
            self.y = 540
            self.x = random.randint(0, 720)

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def handle_collision(self, other, group):
        if group == 'boy:item':
            print('collide item')
            Item.image = load_image('resource\\coin.png')



