from pico2d import *

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

width = get_canvas_width()
height = get_canvas_height()

x = 0
y = 90
while (1):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    if(x < width -25):
        x += 2
    delay(0.01)

close_canvas()
