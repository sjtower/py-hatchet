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


class Door:
    origin = (0, 0)
    width = 0

    def __init__(self, origin, width):
        self.origin = origin
        self.width = width

    def __str__(self):
        return str(self.origin) + " , " + str(self.width)


def stamp_tile(tile_array, offset, floor_array):
    x = offset[0]
    y = offset[1]
    # total_size = tile_array[0].length + tile_array[1].length
    for i in range(0, len(tile_array)):
        for j in range(len(tile_array[0])):
            floor_array[i + y][j + x] = tile_array[i][j]

            # tile is a door. Add it do the available door list
            if tile_array[i][j] == 2:
                door_positions.append((j + x, i + y))

    return floor_array


def find_door_width():
    size = 0
    horizontal_doors = []
    horizontal_one_width_doors = []
    # determine length of doors by getting count of matching y values
    for i in range(0, len(door_positions)):
        # continuous door is found
        if i + 1 == len(door_positions):
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

    # door_positions.sort(mysortfunction)

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
    pretty_print(tile_array1)
    pretty_print(tile_array2)

    floor_array = create_2d_array(20, 20)
    pretty_print(floor_array)

    pretty_print(rotate(tile_array1))

    floor_array = stamp_tile(tile_array1, (0, 7), floor_array)
    floor_array = stamp_tile(rotate(tile_array1), (7, 11), floor_array)
    pretty_print(floor_array)

    print(door_positions)

    doors = find_door_width()
    for door in doors:
        print(str(door))

    print('DONE')


if __name__ == '__main__':
    main()
