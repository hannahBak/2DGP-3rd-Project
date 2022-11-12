from pico2d import *
import game_framework
import game_world
import threading
import time

from boy import Boy
from enemy import Enemy
from enemy import Angry_enemy
from bath import Bath
from ui import Life
from coin import Coin

boy = None
bath = None
coin = None
lifes = []
enemys = []
score = None


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)


# 초기화
def enter():
    global boy, bath, coin
    bath = Bath()
    game_world.add_object(bath, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    coin = Coin()
    game_world.add_object(coin, 1)


    global lifes
    lifes = [Life() for i in range(3)]
    game_world.add_objects(lifes, 1)


    global enemys
    enemys.append(Enemy())
    threading.Timer(5, add_enemy).start()
    threading.Timer(10, add_Angry).start()
    enemys = [Enemy() for i in range(1)] + [Angry_enemy() for i in range(0)]
    game_world.add_objects(enemys, 1)


    game_world.add_collision_group(boy, coin, 'boy:coin')


# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for enemy in enemys:
        enemy.update()

    for life in lifes.copy():
        if collide(boy, enemy):
            lifes.remove(life)
            game_world.remove_object(life)

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('COLLISION ', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)


def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

    for enemy in enemys:
        enemy.draw()

    for life in lifes:
        life.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():

    pass

def add_enemy():
    enemys.append(Enemy())

def add_Angry():
    enemys.append(Angry_enemy())

def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb : return False
    if ra < lb : return False
    if ta < bb : return False
    if ba > tb : return False

    return True


def test_self():
    import play_state
    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
