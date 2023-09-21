from pico2d import *
import math

open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

def render_frame(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.1)

def run_circle() :
    print('Circle')
    
    cx, cy, r = 400, 300, 200
    for deg in range(0, 360, 5):
        x = cx + r * math.cos(math.radians(deg - 90))
        y = cy + r * math.sin(math.radians(deg - 90))
        render_frame(x, y)


run_circle()

close_canvas()
