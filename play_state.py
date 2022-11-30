from pico2d import *
import game_framework
import game_world
import game_over_state
import threading
import time

from boy import Boy
from enemy import Enemy
from enemy import Angry
from bath import Bath
from ui import Life1, Life2, Life3
from coin import Coin, Score

boy = None
bath = None
coins = []
lifes = []
enemys = []
angrys = []


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
    global boy, bath, coins, angrys, score
    bath = Bath()
    game_world.add_object(bath, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    score = Score()
    game_world.add_object(score, 1)

    coins = [Coin() for i in range(1)]
    game_world.add_objects(coins, 1)

    global lifes
    lifes = [Life3(), Life2(), Life1()]
    game_world.add_objects(lifes, 1)


    global enemys
    enemys = [Enemy() for i in range(1)]
    game_world.add_objects(enemys, 1)

    angrys = [Angry() for i in range(1)]
    game_world.add_objects(angrys, 1)

    game_world.add_collision_group(boy, enemys, 'boy:enemy')
    game_world.add_collision_group(boy, coins, 'boy:coin')
    game_world.add_collision_group(boy, angrys, 'boy:angry')


# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for life in lifes:
        for enemy in enemys:
            if collide(boy, enemy):
                enemys.remove(enemy)
                game_world.remove_object(enemy)
                enemys.append(Enemy())
                game_world.add_objects(enemys, 1)
                lifes.remove(life)
                game_world.remove_object(life)

    for life in lifes:
        for angry in angrys:
            if collide(boy, angry):
                angrys.remove(angry)
                game_world.remove_object(angry)
                angrys.append(Angry())
                game_world.add_objects(angrys, 1)
                lifes.remove(life)
                game_world.remove_object(life)

    for coin in coins:
        if collide(boy, coin):
            coins.remove(coin)
            game_world.remove_object(coin)
            coins.append(Coin())
            game_world.add_objects(coins, 1)
            Score.score += 1

    if len(lifes) < 1:
        game_framework.change_state(game_over_state)

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('COLLISION ', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)


def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():

    pass

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
