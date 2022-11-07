from pico2d import *

#1 : 이벤트 정의
RD, LD, RU, LU = range(4)
event_name = ['RD', 'LD', 'RU', 'LU']

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU
}


#2 : 상태의 정의
class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')


    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 6


    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.character.clip_draw(self.frame * 120, 420, 120, 160, self.x, self.y)
        else:
            self.character.clip_draw(self.frame * 120, 580, 120, 160, self.x, self.y)


class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir


    def do(self):
        self.frame = (self.frame + 1) % 6
        self.x += self.dir * 25

        if self.x > 720:
            self.x -= self.dir * 25
        elif self.x < 0:
            self.x = 0


    def draw(self):
        if self.dir == -1:
            self.character.clip_draw(self.frame * 120, 580, 120, 160, self.x, self.y)
        elif self.dir == 1:
            self.character.clip_draw(self.frame * 120, 420, 120, 160, self.x, self.y)


#3. 상태 변환 구현

next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE}
}




class Boy:

    def __init__(self):
        self.x, self.y = 360, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.character = load_image('boyCharacter.png')

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)



    def update(self):

        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print('ERROR:', self.cur_state.__name__, '  ',  event_name[event])
            self.cur_state.enter(self, event)




    def draw(self):

        self.cur_state.draw(self)
        debug_print('PPPP')
        debug_print(f'Face Dir: {self.face_dir}, Dir: {self.dir}')

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)



