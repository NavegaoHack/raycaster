import pygame as pg

class Player:
    forward = True
    backward = True
    def __init__(self, pos, dir, rotation):
        self.pos = pg.Vector2(pos)
        self.dir = pg.Vector2(dir)
        self.step = self.dir / 10
        self.rotation = rotation

    def rotate(self, deg):
        self.dir = self.dir.rotate(deg)
        self.step = self.dir / 10

    def check_collission(self, walls):
        forward_pos = self.pos + self.step
        backward_pos = self.pos - self.step
        
        if (int(forward_pos.x), int(forward_pos.y)) in walls: self.forward = False 
        else: self.forward = True

        if (int(backward_pos.x), int(backward_pos.y)) in walls: self.backward = False 
        else: self.backward = True

    def move(self):
        key = pg.key.get_pressed()
        mouse = pg.mouse.get_rel()

        if key[pg.K_w] and self.forward:
            self.pos += self.step
        if key[pg.K_s] and self.backward:
            self.pos -= self.step

        self.rotate(-self.rotation) if mouse[0] < 0 else self.rotate(self.rotation) if mouse[0] > 0 else None