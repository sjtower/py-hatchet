from Tile import Tile
from array_helper import create_2d_array as create_2d_array
from array_helper import pretty_print as pretty_print

tile_array1 = [
    [2, 2, 2, 2, 2],
    [2, 1, 1, 1, 2],
    [2, 1, 1, 1, 2],
    [2, 3, 3, 3, 2]
]

tile_array2 = [
    [2, 3, 3, 3, 2, 2, 3, 3, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 3],
    [2, 1, 1, 1, 1, 1, 1, 1, 3],
    [3, 1, 1, 1, 1, 1, 1, 1, 3],
    [3, 1, 1, 1, 1, 1, 1, 1, 3],
    [2, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 3],
    [2, 3, 3, 2, 2, 3, 2, 2, 2]

]

tile_array3 = [
    [2, 2, 2, 2],
    [2, 1, 1, 2],
    [2, 1, 1, 2],
    [2, 3, 3, 2]
]

tile_array4 = [
    [2, 2, 2, 2, 2, 2],
    [2, 1, 1, 1, 1, 2],
    [2, 1, 1, 1, 1, 2],
    [2, 3, 3, 3, 3, 2]
]

tile_array5 = [
    [2, 2, 2, 2, 2],
    [2, 1, 1, 1, 2],
    [2, 1, 1, 1, 2],
    [2, 3, 3, 3, 2]
]

tiles = [tile_array1, tile_array2, tile_array3]


class Floor:
    floor_array = []
    door_positions = []


floor = Floor()


# todo: list of available tiles
#       start tile chosen at random and placed in center
#       attempt to attach random tiles from list to start tile
#       doors move to floor once stamped
def main():
    global floor
    floor.floor_array = create_2d_array(30, 30)

    # todo: passing around floor like this is a smell. Floor has list of tiles? floor.make_tile?
    tile_2 = Tile(tile_array2, floor)
    str(tile_2)

    tile_1 = Tile(tile_array1, floor)
    str(tile_1)

    tile_3 = Tile(tile_array3, floor)
    str(tile_3)

    tile_4 = Tile(tile_array4, floor)
    str(tile_4)

    tile_5 = Tile(tile_array5, floor)
    str(tile_5)

    tile_1.stamp((10, 10))

    if tile_5.can_fit(tile_1):
        print("Tiles fit. continuing")

        while not tile_5.test_attach_doors(tile_1, tile_5.doors[0], tile_1.doors[0]):
            print('rotating')  # todo: flip
            tile_5.rotate()

    print('attaching')
    tile_5.attach_doors(tile_1, tile_5.doors[0], tile_1.doors[0])

    pretty_print(floor.floor_array)

    print('DONE')


if __name__ == '__main__':
    main()
