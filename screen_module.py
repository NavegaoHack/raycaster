import pygame as pg

class Screen:
    run = True
    def __init__(self, size, fps, tiles):
        self.size = size
        self.tile_size = size / tiles
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

    def draw_walls(self, walls):
        for wall in walls:
            top_left = pg.Vector2(wall) * self.tile_size
            top_left.x += 2
            top_left.y += 2

            bottom_right = pg.Vector2(self.tile_size)
            bottom_right.x -= 4
            bottom_right.y -= 4

            pg.draw.rect(
                self.w,
                "white",
                (
                    top_left,
                    bottom_right
                )
            )

    def draw_player(self, player_pos, player_dir):
        radius = 10
        pos = player_pos * self.tile_size
        dir = pos + (player_dir * radius)
        pg.draw.circle(
            self.w,
            "white",
            pos,
            radius
        )
        pg.draw.line(
            self.w,
            "purple",
            pos,
            dir,
            2
        )



    def render(self):
        pg.display.flip()
        self.clock.tick(self.fps)