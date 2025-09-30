from ursina import *

app = Ursina()

player = Entity(model='cube', color=color.azure, scale=(1,2,1), collider='box')
player_speed = 5

camera.parent = player
camera.position = (0, 2, -10)
camera.rotation_x = 10

floor = Entity(model='plane', scale=(20,20), color=color.gray, collider='box')

door = Entity(model='cube', scale=(1,3,2), position=(0,1.5,8), color=color.brown, collider='box')
door_open = False

button = Entity(model='cube', scale=(1,0.5,1), position=(0,0.25,3), color=color.red, collider='box')

def update():
    move = Vec3(
        held_keys['d'] - held_keys['a'],
        0,
        held_keys['w'] - held_keys['s']
    ).normalized()
    player.position += move * time.dt * player_speed

def input(key):
    global door_open
    if key == 'e' and not door_open:
        if distance(player.position, button.position) < 2:
            door.animate_position((-3, 1.5, 8), duration=1)
            door.collider = None
            button.color = color.green
            door_open = True

app.run()
