from vpython import *

scene.width = 1500
scene.height = 800   

ball1 = sphere(pos=vector(-5, 0, 0), radius=0.5, color=color.red, make_trail=True)
ball2 = sphere(pos=vector(5, 0, 0), radius=0.5, color=color.blue, make_trail=True)

ball3 = sphere(pos=vector(0, -5, 0), radius=0.5, color=color.green, make_trail=True)
ball4 = sphere(pos=vector(0, 5, 0), radius=0.5, color=color.orange, make_trail=True)

v1 = vector(0.1, 0, 0)   
v2 = vector(-0.1, 0, 0)  
v3 = vector(0, 0.1, 0)   
v4 = vector(0, -0.1, 0) 

left_wall = -5
right_wall = 5
bottom_wall = -5
top_wall = 5

while True:
    rate(40)

    ball1.pos += v1
    ball2.pos += v2
    ball3.pos += v3
    ball4.pos += v4

    if ball1.pos.x >= right_wall or ball1.pos.x <= left_wall:
        v1.x *= -1
    if ball2.pos.x >= right_wall or ball2.pos.x <= left_wall:
        v2.x *= -1

    if ball3.pos.y >= top_wall or ball3.pos.y <= bottom_wall:
        v3.y *= -1
    if ball4.pos.y >= top_wall or ball4.pos.y <= bottom_wall:
        v4.y *= -1
