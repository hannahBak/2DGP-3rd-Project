import game_framework
import pico2d

import play_state

pico2d.open_canvas(720, 540)
game_framework.run(play_state)
pico2d.close_canvas()