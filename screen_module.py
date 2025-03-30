import pygame as pg

class Screen:
    run = True
    def __init__(self, size, fps):
        self.size = size
        self.fps = fps
        self.w = pg.display.set_mode((size, size))
        self.clock = pg.time.Clock()

    def event(self):
        # pygame.QUIT event means the user clicked X to close your window
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.run = False

    def draw_bg(self):
        self.w.fill("purple")

    def render(self):
        pg.display.flip()
        self.clock.tick(self.fps)