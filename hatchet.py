import copy
import random

from Tile import Tile
from array_helper import create_2d_array as create_2d_array
from array_helper import pretty_print as pretty_print
from input import input_tiles


class Floor:
    floor_array = []
    door_positions = []
    available_tiles = []
    stamped_tiles = []

    def add_tile(self, tile):
        tile = Tile(tile, self)
        self.available_tiles.append(tile)


floor = Floor()


# todo: doors move to floor once stamped?
def main():
    global floor
    floor.floor_array = create_2d_array(50, 50)

    for tile in input_tiles:
        floor.add_tile(tile)

    tiles = floor.available_tiles
    start_tile = random.choice(tiles)
    start_tile.stamp((20, 20))
    pretty_print(floor.floor_array)

    for x in range(0, 128):

        tile = random.choice(floor.available_tiles)
        tile.rotate_randomly()  # todo: flip

        target_tile = random.choice(floor.stamped_tiles)

        if tile.can_fit(target_tile):
            print("tiles fit - continuing")
            attach_tile(target_tile, tile)

    pretty_print(floor.floor_array)
    print('DONE')


# test each door in the source tile against a single target door. If no matches, use another target door and repeat
def attach_tile(target_tile, tile):
    random.shuffle(target_tile.doors)
    random.shuffle(tile.doors)

    for target_door in target_tile.doors:
        for source_door in tile.doors:
            for i in range(0, 3):
                if tile.test_attach_doors(target_tile, source_door, target_door):
                    print('attaching')
                    tile.attach_doors(target_tile, source_door, target_door)
                    # todo: not breaking at this point seems to improve room generation?
                    # todo: remove placed doors
                else:
                    tile.rotate()  # todo: flip
            print("tried full 360 rotation - try another source door")  # todo: log instead of print
        print("tried all source doors - try another target door")
    print("could not match tile - skipping")


if __name__ == '__main__':
    main()
