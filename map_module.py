class Map:
    def __init__(self, tiles):
        self.m = set()
        self.tiles = tiles
        self.init_map()

    def init_map(self):
        for i in range(self.tiles):
            self.m.add((0, i))
            self.m.add((self.tiles - 1, i))
            self.m.add((i, 0))
            self.m.add((i, self.tiles - 1))
    
    def get(self):
        return self.m
    