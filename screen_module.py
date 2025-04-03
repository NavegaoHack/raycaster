import pygame as pg

class Screen:
    white = pg.Vector3(255, 255, 255)
    run = True
    def __init__(self, size, fps, tiles):
        self.size = size
        self.half_size = size / 2
        self.tile_size = size / tiles
        self.fps = fps
        self.w = pg.display.set_mode((size, size))
        self.clock = pg.time.Clock()
        self.bg = pg.Vector3(163, 67, 67)
        self.diff = self.white - self.bg
        self.change_rendering = True
        self.pause_inputs = False

    def event(self):
        # pygame.QUIT event means the user clicked X to close your window
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.run = False
            if e.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                if keys[pg.K_c]:
                    self.change_rendering = not self.change_rendering
                if keys[pg.K_p]:
                    self.pause_inputs = not self.pause_inputs
                    

    def draw_bg(self):
        self.w.fill(self.bg)

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

        
    def draw_ray(self, player, map, size):
        step = player.step.copy()
        step = step.rotate(-(player.fov / 2))
        rotate_inc = player.fov / size

        for each_ray in range(size):
            ray = player.pos.copy()

            while (ray.x//1, ray.y//1) not in map:
                ray += step
            
            step = step.rotate(rotate_inc)
            
            pg.draw.line(
                self.w,
                "white",
                player.pos * self.tile_size,
                ray * self.tile_size
            )
    
    def color_pseudoalpha(self, wall_height):
        final_diff = self.diff * (wall_height / self.half_size)
        bg_color = self.bg + final_diff
        bg_color_b = pg.Vector3()

        bg_color_b.x = bg_color.x if bg_color.x < 255 else 255 
        bg_color_b.y = bg_color.y if bg_color.y < 255 else 255 
        bg_color_b.z = bg_color.z if bg_color.z < 255 else 255 

        return bg_color_b


    def draw_raycast(self, player, map, size):
        step = player.step.copy()
        step = step.rotate(-(player.fov / 2))
        rotate_inc = player.fov / size

        for each_ray in range(size):
            ray = player.pos.copy()

            while (ray.x//1, ray.y//1) not in map:
                ray += step

            distance = ray.distance_to(player.pos)
            wall_height = (size / 2) / distance
            self.color_pseudoalpha(wall_height) 

            step = step.rotate(rotate_inc)

            point_up = (each_ray, (size / 2) - wall_height)
            point_down = (each_ray, (size / 2) + wall_height)

            pg.draw.line(
                self.w,
                self.color_pseudoalpha(wall_height),
                point_up,
                point_down
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