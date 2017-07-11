from Door import Door


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
