from pico2d import*
import random

class Bath:
    def __init__(self):
        self.bath = load_image('bath.png')

    def draw(self):
        self.bath.draw(360, 270)

class Boy:
    def __init__(self):
        self.x, self.y = 360, 90
        self.frame = 0
        self.character = load_image('boyCharacter.png')
        self.h = None
        self.y = 90
        self.f = 120

    def update(self):
        self.frame = (self.frame + 1) % 6
        self.x += dir * 25
        self.h = h
        self.f = f
        if self.x > 720:
            self.x -= dir * 25
        elif self.x < 0:
            self.x = 0

    def draw(self):
        self.character.clip_draw(self.frame*self.f, self.h, 120, 160, self.x, self.y)
        delay(0.1)

class Enemy:
    def __init__(self):
        self.y = 540
        self.x = random.randint(0, 720)
        self.enemy = load_image('smile_poop.png')
        self.speed = 20

    def update(self):
        self.y -= self.speed
        if self.y < 0:
            self.y = 540
            self.x = random.randint(0, 720)
            self.speed += 5

    def draw(self):
        self.enemy.draw(self.x, self.y)

class Item:
    def __init__(self):
        self.y = 540
        self.x = random.randint(0, 720)
        self.coin = load_image('coin.png')
        self.bomb = load_image('Bomb.png')
        self.speed = 30

    def update(self):
        self.y -= self.speed
        if self.y < 0:
            self.y = 540
            self.x = random.randint(0, 720)
            self.speed += 3

    def draw(self):
        self.coin.draw(self.x, self.y)

def handle_events():
    global running
    global dir
    global h, f
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                Boy.y = 90
                h = 420
                f = 120
            elif event.key == SDLK_LEFT:
                h = 580
                dir -= 1
                Boy.y = 90
                f = 120
            elif event.key == SDLK_SPACE:
                if h == 580:
                    h = 60
                elif h == 420:
                    h = 250
                f = 130
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1

bath = None
boy = None
enemy = None
item = None
running = True
dir = 0
h = 420
f = 120

def enter():
    global bath, boy, enemy, item, running
    boy = Boy()
    bath = Bath()
    enemy = Enemy()
    item = Item()


def exit():
    global bath, boy, enemy, item
    del bath
    del boy
    del enemy
    del item

def update():
    boy.update()
    enemy.update()
    item.update()
    pass

def draw():
    clear_canvas()
    bath.draw()
    boy.draw()
    enemy.draw()
    item.draw()
    update_canvas()

def pause():
    pass
def resume():
    pass

open_canvas(720, 540)
enter()
while running:
    handle_events()
    update()
    draw()
exit()
close_canvas()