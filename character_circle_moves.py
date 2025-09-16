from pico2d import *

import math

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

width = get_canvas_width()
height = get_canvas_height()

x = width / 2
y = 90
cx = width / 2
cy = height / 2
count = 0
theta = 1.0
radius = cy -90
x =  cx + radius * math.sin( theta *2* math.pi)
y =  cy + radius * math.cos( theta *2* math.pi)
while True:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    theta += 0.01
    x = cx + radius * math.sin(theta * math.pi)
    y = cy + radius * math.cos(theta * math.pi)
    delay(0.05)

close_canvas()