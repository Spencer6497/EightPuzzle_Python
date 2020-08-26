import numpy as np

class State:
    tile_seq = []
    depth = 0
    weight = 0
    def __init__(self, tile_seq = [], depth = 0, weight = 0):
        self.tile_seq = tile_seq
        self.depth = depth
        self.weight = weight

    def getTile_1d(self):
        tiles = np.zeros(len(self.tile_seq) * len(self.tile_seq[0]))
        index = 0
        for row in self.tile_seq:
            for item in row:
                tiles[index] = item
                index += 1
        return tiles


    def equals(self, obj):
        op = obj.tile_seq
        comparison = self.tile_seq == op
        return comparison.all()

        '''if self.tile_seq == op:
            return True
        else :
            return False
        '''