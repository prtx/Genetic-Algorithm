import turtle
import math

tt = turtle.Turtle()
screen = tt.getscreen()

scale = 2
frame_rate = 0.25
height = screen.window_height()
width = screen.window_width()
x_offset = -width/2 + 100
y_offset = -height/2 + 100


def projectile(v, theta, gfx=True):
    if gfx:
        tt.speed("fastest")
        tt.penup()
        tt.goto(x_offset, y_offset)
        tt.pendown()

    t = 0
    while True:
        x = v * math.cos(math.radians(theta)) * t
        y = v * math.sin(math.radians(theta)) * t - 0.5 * 10 * t**2
        t += frame_rate
        if y<0: break
        if gfx: tt.goto(x/scale+x_offset, y/scale+y_offset)

    return x


blocks = []
def build_block(x, y, l):
    blockx, blocky = x_offset+x, y_offset+y
    blockl = l
    
    tt.penup()
    tt.goto(blockx, blocky)
    tt.pendown()
    
    for i in range(4):
        tt.forward(blockl)
        tt.left(90)

    if (blockx, blocky, blockl) not in blocks:
        blocks.append((blockx, blocky, blockl))


def collision(x, y):
    for blockx, blocky, blockl in blocks:
        if x>blockx and x<blockx+blockl and y>blocky and y<blocky+blockl:
            return True
    return False


def projectile_with_block(v, theta, gfx=True):
    if gfx:
        tt.speed("fastest")
        tt.penup()
        tt.goto(x_offset, y_offset)
        tt.pendown()

    t = 0
    while True:
        x = v * math.cos(math.radians(theta)) * t
        y = v * math.sin(math.radians(theta)) * t - 0.5 * 10 * t**2
        t += frame_rate
        
        if collision(x/scale+x_offset, y/scale+y_offset): return x
        if y<0: break
        if gfx: tt.goto(x/scale+x_offset, y/scale+y_offset)

    return x


if __name__ == "__main__":
    
    build_block(100, 0, 100)
    projectile_with_block(100, 45)
    # projectile(100, 30)
    # projectile(100, 60)
    screen.reset()
    screen._root.mainloop()
