import game_framework
from pico2d import *
import play_state

image = None

def enter():
    global image
    image = load_image('resource\\heart.png')

def exit():
    global image
    del image

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(360, 270)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_1:
                    game_framework.pop_state()


def update():
    pass