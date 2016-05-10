import random
import os

from pico2d import *

import game_framework
import start_state

name = "MainState"
image = None

def enter():
    global image
    image = load_image('background.jpg')

def exit():
    global image
    del(image)

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

def update():
    pass

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

