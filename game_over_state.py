import game_framework
from pico2d import *
import title
import time

image = None
current_time = time.time()

def enter():
    global image
    image = load_image('resource\\gameover.png')

def exit():
    global image
    del image

def draw():
    clear_canvas()
    image.draw(360, 270)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()


def update():
    logo_time = time.time() - current_time
    if logo_time > 5.0:
        game_framework.change_state(title)
    pass