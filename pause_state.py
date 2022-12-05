import game_framework
from pico2d import *
import play_state
import title

image = None

def enter():
    global image
    image = load_image('resource\\pause_.png')

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
    number = 1
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if number == 2:
                number -= 1
                print(number)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if number == 1:
                number += 1
                print(number)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN):
            match number:
                case 1:
                    game_framework.pop_state()
                case 2:
                    game_framework.change_state(title)

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()


def update():
    pass