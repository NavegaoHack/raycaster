from pygame import init, quit
from screen_module import *
from map_module import *
from player_module import *

# pygame setup
size = 480
tiles = 16
fps = 30

init()
map = Map(tiles)
screen = Screen(size, fps, tiles)
player = Player((tiles // 2, tiles // 2), (1, 0), 4)

print(map.get())

while screen.run:
    # poll for events
    screen.event()

    # fill the screen with a color to wipe away anything from last frame
    screen.draw_bg()
    screen.draw_walls(map.get())

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    screen.render()

quit()