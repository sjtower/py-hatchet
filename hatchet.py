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
            print("Tiles fit. continuing")

            skip = False
            i = j = rotations = 0
            while not tile.test_attach_doors(target_tile, tile.doors[i], target_tile.doors[j]):
                print('rotating')  # todo: flip
                tile.rotate()
                rotations += 1
                if rotations >= 3:
                    print("tried full 360 rotation - try another door")  # todo: log instead of print
                    i += 1
                    rotations = 0
                    if len(tile.doors) is 1 or i is len(tile.doors) - 1:
                        print("tried all source doors - try another target door")
                        i = 0
                        j += 1
                        if len(target_tile.doors) is 1 or j is len(target_tile.doors) - 1:
                            skip = True
                            print("no tiles could fit - skipping")
                            break  # should not be possible?
                            # todo: clean this shit up - shouldn't need indexes just go thru each door list

            if not skip:
                #  todo: remove placed doors
                print('attaching')
                tile.attach_doors(target_tile, tile.doors[i], target_tile.doors[j])
                pretty_print(floor.floor_array)

    pretty_print(floor.floor_array)
    print('DONE')


if __name__ == '__main__':
    main()
