from array_helper import pretty_print as pretty_print
from array_helper import create_2d_array as create_2d_array
from array_helper import rotate as rotate
import numpy as np

FLOOR_ARRAY = []

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


class Tile:
    doors = []
    door_positions = []
    tile_array = []

    def __init__(self, tile_array):
        self.tile_array = tile_array

    def __str__(self):
        return str(np.matrix(self.tile_array))

    def stamp(self, offset):
        x = offset[0]
        y = offset[1] - 1 #todo: why?
        # total_size = tile_array[0].length + tile_array[1].length
        tile_array = self.tile_array
        for i in range(0, len(tile_array)):
            for j in range(len(tile_array[0])):
                FLOOR_ARRAY[i + x][j + y] = tile_array[i][j]

                # square is a door. Add it do the available door list
                if tile_array[i][j] is 3:
                    self.door_positions.append((i + x, j + y))


class Door:
    origin = (0, 0)
    width = 0

    def __init__(self, origin, width):
        self.origin = origin
        self.width = width

    def __str__(self):
        return str(self.origin) + " , " + str(self.width)


def find_door_width(door_positions):
    size = 0
    horizontal_doors = []
    horizontal_one_width_doors = []
    # determine length of doors by getting count of matching y values
    for i in range(0, len(door_positions)):
        # continuous door is found
        if i + 1 is len(door_positions):
            next_door = None
        else:
            next_door = door_positions[i + 1]

        this_door = door_positions[i]
        if next_door is not None and this_door[0] == next_door[0] - 1 and this_door[1] == next_door[1]:
            size = size + 1
        else:
            # don't count 1 width doors
            if size > 0:
                # first door, increase size by one

                door_origin_position = door_positions[i - size]
                # door_origin_position.width = size + 1

                door = Door(door_origin_position, size + 1)
                horizontal_doors.append(door)
                size = 0
            else:
                horizontal_one_width_doors.append(Door(this_door, 1))

    vertical_doors = []
    vertical_one_width_doors = []
    size = 0
    # determine length of doors by getting count of matching x values
    for j in range(0, len(door_positions)):
        # continuous door is found
        if j + 1 == len(door_positions):
            next_door = None
        else:
            next_door = door_positions[j + 1]

        this_door = door_positions[j]
        if next_door is not None and this_door[1] == next_door[1] - 1 and this_door[0] == next_door[0]:
            size = size + 1
        else:
            # don't count 1 width doors
            if size > 0:
                # first door, increase size by one

                door_origin_position = door_positions[j - size]
                door = Door(door_origin_position, size + 1)
                vertical_doors.append(door)
                size = 0
            else:
                vertical_one_width_doors.append(Door(this_door, 1))

    one_width_doors = []
    for k in range(len(horizontal_one_width_doors)):
        for l in range(len(vertical_one_width_doors)):
            if horizontal_one_width_doors[k].origin[0] == vertical_one_width_doors[l].origin[0] \
                    and horizontal_one_width_doors[k].origin[1] == vertical_one_width_doors[l].origin[1]:
                one_width_doors.append(horizontal_one_width_doors[k])

    return horizontal_doors + vertical_doors + one_width_doors


def main():
    print('Hello World')

    global FLOOR_ARRAY
    FLOOR_ARRAY = create_2d_array(30, 30)

    tile_1 = Tile(tile_array1)
    str(tile_1)

    tile_2 = Tile(tile_array2)

    tile_1.stamp((7, 8))

    doors = find_door_width(tile_1.door_positions)
    for door in doors:
        print(str(door))

    # floor_array = stamp_tile2(rotate(rotate(tile_array1)), doors[0], floor_array)
    tile_2.stamp(doors[0].origin)

    pretty_print(FLOOR_ARRAY)

    print('DONE')


if __name__ == '__main__':
    main()
