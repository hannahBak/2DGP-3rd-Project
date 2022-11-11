from pico2d import *
import game_framework
import game_world
import threading
import time

from boy import Boy
from enemy import Enemy
from enemy import Angry_enemy
from bath import Bath

boy = None
bath = None
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
    global boy, bath
    bath = Bath()
    boy = Boy()
    enemys.append(Enemy())
    threading.Timer(5, add_enemy).start()
    threading.Timer(5, add_Angry).start()
    game_world.add_object(bath, 0)
    game_world.add_object(boy, 1)
    game_world.add_object(enemys, 1)
    game_world.add_object(angrys, 1)



# 종료
def exit():
    game_world.clear()

def update():

    boy.update()
    for enemy in enemys:
        enemy.update()
    for angry in angrys:
        angry.update()

def draw_world():

    bath.draw()
    boy.draw()
    for enemy in enemys:
        enemy.draw()
    for angry in angrys:
        angry.draw()



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
    angrys.append(Angry_enemy())



def test_self():
    import play_state
    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
