from pico2d import *
import game_framework
import game_world
import game_over_state
import pause_state
import time

from boy import Boy
from enemy import Enemy
from enemy import Angry
from bath import Bath
from ui import Life1, Life2, Life3
from coin import Coin, Score
from item import Item
from item_place import bomb_place, Boom

boy = None
bath = None
items = []
coins = []
lifes = []
enemys = []
angrys = []
item_type = None
bombs = []


def handle_events():
    global item_type
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(pause_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_e):
            item_play()
            item_type = None
        else:
            boy.handle_event(event)


# 초기화
def enter():
    global boy, bath, coins, angrys, score, items
    bath = Bath()
    game_world.add_object(bath, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    score = Score()
    game_world.add_object(score, 1)

    coins = [Coin() for i in range(1)]
    game_world.add_objects(coins, 1)

    items = [Item() for i in range(1)]
    game_world.add_objects(items, 1)

    global lifes
    lifes = [Life3(), Life2(), Life1()]
    game_world.add_objects(lifes, 1)


    global enemys
    enemys = [Enemy()]
    game_world.add_objects(enemys, 1)

    angrys = [Angry() for i in range(1)]
    game_world.add_objects(angrys, 1)

    game_world.add_collision_group(boy, enemys, 'boy:enemy')
    game_world.add_collision_group(boy, coins, 'boy:coin')
    game_world.add_collision_group(boy, angrys, 'boy:angry')
    game_world.add_collision_group(boy, items, 'boy:item')


# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    # for item in items:
    #     if collide(boy, item):
    #         items.remove(item)
    #         game_world.remove_object(item)
    #         items.append(Item())
    #         game_world.add_objects(items, 1)
    #         if len(lifes) < 2:
    #             lifes.append(Life2())
    #             game_world.add_objects(lifes, 1)
    #         elif len(lifes) < 3:
    #             lifes.append(Life3())
    #             game_world.add_objects(lifes, 1)

    for life in lifes:
        for enemy in enemys:
            if collide(boy, enemy):
                Enemy.eat_sound.play()
                enemys.remove(enemy)
                game_world.remove_object(enemy)
                enemys.append(Enemy())
                game_world.add_objects(enemys, 1)
                if len(lifes) == 3:
                    lifes.remove(life)
                    game_world.remove_object(life)
                elif len(lifes) == 2:
                    lifes.remove(life)
                    game_world.remove_object(life)
                elif len(lifes) == 1:
                    lifes.remove(life)
                    game_world.remove_object(life)

    for angry in angrys:
        if collide(boy, angry):
            angrys.remove(angry)
            game_world.remove_object(angry)
            game_framework.change_state(game_over_state)

    for item in items:
        if collide(boy, item):
            global item_type
            items.remove(item)
            game_world.remove_object(item)
            item_type = 'bomb'
            bombs = [bomb_place()]
            game_world.add_objects(bombs, 1)

    for coin in coins:
        if collide(boy, coin):
            coins.remove(coin)
            game_world.remove_object(coin)
            coins.append(Coin())
            Coin.eat_sound.play()
            game_world.add_objects(coins, 1)
            Score.score += 1

    if len(lifes) < 1:
        game_framework.change_state(game_over_state)

    # if item_type == None:
    #     boom = None

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

def item_play():
    current_time = time.time()

    if item_type == 'bomb':
        for angry in angrys:
            angrys.remove(angry)
            game_world.remove_object(angry)
            angrys.append(Angry())
            game_world.add_objects(angrys, 1)

        for enemy in enemys:
            enemys.remove(enemy)
            game_world.remove_object(enemy)
            enemys.append(Enemy())
            game_world.add_objects(enemys, 1)

    # now_time = time.time() - current_time
    # boom = Boom()
    # game_world.add_object(boom, 1)

    # if now_time > 1.0:
    #     del boom[0]

    # boom = load_image('resource\\boom.png')
    # boom.draw(300, 300)

    # for bomb in bombs:
    #     bombs.remove(bomb)
    #     game_world.remove_object(bomb)

def test_self():
    import play_state
    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
