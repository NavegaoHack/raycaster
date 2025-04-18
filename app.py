from pygame import init, quit
from screen_module import *
from map_module import *
from player_module import *

# pygame setup
size = 480
tiles = 32 
fps = 30

init()
map = Map(tiles)
map.add_wall((5, 5))
map.add_wall((24, 24))
map.add_wall((24, 25))
map.add_wall((25, 24))
screen = Screen(size, fps, tiles)
player = Player((tiles // 2, tiles // 2), (1, 0), 4)

print(map.get())

while screen.run:
    # poll for events

    screen.event()

    if not screen.pause_inputs:
        player.check_collission(map.m)
        player.move()

    # fill the screen with a color to wipe away anything from last frame
    screen.draw_bg()
    if screen.change_rendering:
        screen.draw_walls(map.m)
        screen.draw_ray(player, map.m, screen.size)
        screen.draw_player(player.pos, player.dir)
    else:
        screen.draw_raycast(player, map.m, screen.size)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    screen.render()

quit()