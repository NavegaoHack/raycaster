import pygame as pg

class Player:
    def __init__(self, pos, dir, rotation):
        self.pos = pg.Vector2(pos)
        self.dir = pg.Vector2(dir)
        self.step = self.dir / 10
        self.rotation = rotation

    def rotate(self, deg):
        self.dir = self.dir.rotate(deg)
        self.step = self.dir / 10
    
    def move(self):
        key = pg.key.get_pressed()
        mouse = pg.mouse.get_rel()
        if key[pg.K_w]:
            self.pos += self.step
        if key[pg.K_s]:
            self.pos -= self.step

        self.rotate(-self.rotation) if mouse[0] < 0 else self.rotate(self.rotation) if mouse[0] > 0 else None