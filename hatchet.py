from array_helper import pretty_print as pretty_print
from array_helper import create_2d_array as create_2d_array
from array_helper import rotate as rotate
import numpy as np

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

tiles = [tile_array1, tile_array2, tile_array3]


class Floor:
    floor_array = []
    door_positions = []


floor = Floor()


class Tile:
    doors = []
    tile_array = []
    floor_offset = 0

    def __init__(self, tile_array):
        self.tile_array = tile_array
        self.init_doors()

    def __str__(self):
        return str(np.matrix(self.tile_array))

    def check_fit(self, other_tile):
        # check for same size door
        same_width_door_available = False
        for door in self.doors:
            if door in other_tile.doors:
                same_width_door_available = True
                break

        if not same_width_door_available:
            return False

    def attach_doors(self, tile, source_door, tile_door):
        x = tile_door.origin[0] - source_door.origin[0] + tile.floor_offset[0]
        y = tile_door.origin[1] - source_door.origin[1] + tile.floor_offset[1]
        self.stamp((x, y))

    def stamp(self, offset):
        self.floor_offset = offset
        x = offset[0]
        y = offset[1]
        # total_size = tile_array[0].length + tile_array[1].length
        tile_array = self.tile_array
        global floor
        for i in range(0, len(tile_array)):
            for j in range(len(tile_array[0])):
                floor.floor_array[i + x][j + y] = tile_array[i][j]

    def init_doors(self):
        door_positions = []
        tile_array = self.tile_array
        for i in range(0, len(tile_array)):
            for j in range(len(tile_array[0])):

                # square is a door. Add it do the available door list
                if tile_array[i][j] is 3:
                    door_positions.append((i, j))

        self.doors = find_doors(door_positions)


class Door:
    origin = (0, 0)
    width = 0

    def __init__(self, origin, width):
        self.origin = origin
        self.width = width

    def __str__(self):
        return str(self.origin) + " , " + str(self.width)

    def __eq__(self, other):
        return self.width == other.width


def find_doors(door_positions):
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
        if next_door is not None and this_door[0] == next_door[0] and this_door[1] == next_door[1] - 1:
            size = size + 1
        else:
            # don't count 1 width doors
            if size > 0:
                door_origin_position = door_positions[i - size]
                door = Door(door_origin_position, size + 1)
                horizontal_doors.append(door)
                size = 0
            else:
                horizontal_one_width_doors.append(Door(this_door, 1))

    # sort doors by y value
    door_positions.sort(key=lambda tup: tup[1])

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
        if next_door is not None and this_door[1] == next_door[1] and this_door[0] == next_door[0] - 1:
            size = size + 1
        else:
            # don't count 1 width doors
            if size > 0:
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
    global floor
    floor.floor_array = create_2d_array(30, 30)

    tile_2 = Tile(tile_array2)
    str(tile_2)

    tile_1 = Tile(tile_array1)
    str(tile_1)

    tile_3 = Tile(tile_array3)
    str(tile_3)

    tile_2.stamp((10, 10))

    for door in tile_2.doors:
        print(str(door))

    tile_3.attach_doors(tile_2, tile_3.doors[0], tile_2.doors[0])

    # floor_array = stamp_tile2(rotate(rotate(tile_array1)), doors[0], floor_array)
    # tile_2.stamp(doors[0].origin)

    pretty_print(floor.floor_array)

    print('DONE')


if __name__ == '__main__':
    main()
