import time

from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

window.borderless = False
app = Ursina()
window.color = color.white
camera.orientation = True
camera.fov = 1
ground = Entity(
    model = 'cube',
    color = color.olive.tint(-.4),
    z = -.1,
    y = -1,
    origin_y = .5,
    scale = (1000, 100, 10),
    collider = 'box',
    ignore = True,
)

for i in range(10):
    Entity(
        model = 'cube', color = color.dark_gray, collide='box', ignore=True,
        position =(random.randint(-20,20), random.randint(0,10)),
        scale=(random.randint(1,20), random.randint(2,5),10)
    )

player = PlatformerController2d()
player.x = 1
player.y = raycast(player.world_position, player.down).world_point[1] + .01
camera.add_script(SmoothFollow(target=player, offset=[0,5,-30], speed=4))

input_handler.bind('right arrow', 'd')
input_handler.bind('left arrow', 'a')
input_handler.bind('up arrow', 'space')
input_handler.bind('gamepad dpag right', 'd')
input_handler.bind('gamepad dpag left', 'a')
input_handler.bind('gamepad a', 'space')

player.add_script(NoclipMode2d())

app.run()