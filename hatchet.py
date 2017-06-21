from array_helper import pretty_print as pretty_print
from array_helper import create_2d_array as create_2d_array
from array_helper import rotate as rotate

door_positions = []

tile_array1 = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 2, 2, 2, 1]
]

tile_array2 = [
    [1, 2, 2, 2, 1, 1, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 2],
    [1, 2, 2, 1, 1, 2, 1, 1, 1]

]


def stamp_tile(tile_array, offset, floor_array):
    x = offset[0]
    y = offset[1]
    # total_size = tile_array[0].length + tile_array[1].length
    for i in range(0, len(tile_array)):
        for j in range(len(tile_array[0])):
            floor_array[i + y][j + x] = tile_array[i][j]

            # tile is a door. Add it do the available door list
            if tile_array[i][j] == 2:
                door_positions.append({j + x, i + y})

    return floor_array


def main():
    print('Hello World')
    pretty_print(tile_array1)
    pretty_print(tile_array2)

    floor_array = create_2d_array(20, 20)
    pretty_print(floor_array)

    pretty_print(rotate(tile_array1))

    floor_array = stamp_tile(tile_array1, (7, 7), floor_array)
    floor_array = stamp_tile(tile_array1, (7, 11), floor_array)
    pretty_print(floor_array)

    print(door_positions)

if __name__ == '__main__':
    main()
