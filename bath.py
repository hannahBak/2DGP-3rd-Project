from pico2d import *

class Bath:
    def __init__(self):
        self.bath = load_image('resource\\bath.png')
        self.bgm = load_music('resource\\avoidingpoop.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()

    def draw(self):
        self.bath.draw(360, 270)


    def update(self): pass