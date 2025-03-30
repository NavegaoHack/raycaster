from pygame import init, quit
from screen_module import *

# pygame setup
size = 480

init()
screen = Screen(720, 30)

while screen.run:
    # poll for events
    screen.event()

    # fill the screen with a color to wipe away anything from last frame
    screen.draw_bg()

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    screen.render()

quit()