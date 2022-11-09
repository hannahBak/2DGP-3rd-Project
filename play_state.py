from pico2d import *
import game_framework
import game_world
import threading
import time

from boy import Boy
from enemy import Enemy
from bath import Bath

boy = None
bath = None
enemys = []

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
    global boy, bath
    bath = Bath()
    boy = Boy()
    enemys.append(Enemy())
    threading.Timer(3, add_enemy).start()


# 종료
def exit():
    global boy, bath
    del bath
    del boy
    for enemy in enemys:
        del enemy

def update():

    boy.update()
    for enemy in enemys:
        enemy.update()


def draw_world():
    delay(0.05)
    bath.draw()
    boy.draw()
    for enemy in enemys:
        enemy.draw()



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


def test_self():
    import play_state
    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
