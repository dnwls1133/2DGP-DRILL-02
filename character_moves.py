from pico2d import *

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

width = get_canvas_width()
height = get_canvas_height()

x = 10
y = 90
count = 0
boy_width = 30
boy_height = 140
while True:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    if count <= (width-boy_width)//2:
        x += 2
    elif (width-boy_width)//2 < count <= (width-boy_width + height-boy_height)//2:
        y += 2
    elif (width-boy_width + height-boy_height)//2 < count <= ((width-boy_width) * 2 + height-boy_height)//2:
        x -= 2
    elif ((width-boy_width) * 2 + height-boy_height)//2 < count <= ((width-boy_width) * 2 + (height -boy_height) *2)//2:
        y -= 2
    else:
        count = 0
    count += 1
    delay(0.005)

close_canvas()
