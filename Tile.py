import copy
import random

import numpy as np

np.set_printoptions(threshold=np.nan, linewidth=np.nan)

from array_helper import rotate as rotate
from util import find_doors


class Tile:
    doors = []
    tile_array = []
    floor_offset = 0
    floor = []  # pointer to main floor

    def __init__(self, tile_array, floor):
        self.tile_array = tile_array
        self.init_doors()
        self.floor = floor

    def __str__(self):
        tile_print = str(np.matrix(self.tile_array))
        tile_print += "\nDoors: "
        for door in self.doors:
            tile_print += (str(door))
        return tile_print

    def rotate(self):
        self.tile_array = rotate(self.tile_array)
        self.init_doors()

    def rotate_randomly(self):
        for i in range(0, random.randint(0, 3)):
            self.tile_array = rotate(self.tile_array)

    def can_fit(self, other):
        # check for same size door
        same_width_door_available = False
        for door in self.doors:
            if door in other.doors:
                same_width_door_available = True
                break

        if not same_width_door_available:
            print("No same-width doors available. Skipping tile.")
            return False

        return True

    def find_fit(self, other):

        if not self.can_fit(other):
            print("Cannot find fit - no same-width doors.")
            return False

    # todo: consider combining test and non-test methods
    def attach_doors(self, other, source_door, other_door):
        x = other_door.origin[0] - source_door.origin[0] + other.floor_offset[0]
        y = other_door.origin[1] - source_door.origin[1] + other.floor_offset[1]
        self.stamp((x, y))

    def test_attach_doors(self, other, source_door, other_door):
        x = other_door.origin[0] - source_door.origin[0] + other.floor_offset[0]
        y = other_door.origin[1] - source_door.origin[1] + other.floor_offset[1]
        return self.test_stamp((x, y))

    def stamp(self, offset):
        self.floor_offset = offset
        self.floor.stamped_tiles.append(self)
        x = offset[0]
        y = offset[1]
        # total_size = tile_array[0].length + tile_array[1].length
        tile_array = self.tile_array
        for i in range(0, len(tile_array)):
            for j in range(len(tile_array[0])):
                self.floor.floor_array[i + x][j + y] = tile_array[i][j]

    def test_stamp(self, offset):
        tile_array = self.tile_array
        temp_floor = copy.deepcopy(self.floor.floor_array)
        x = offset[0]
        y = offset[1]
        for i in range(0, len(tile_array)):
            for j in range(len(tile_array[0])):
                # todo: methodize these checks
                try:
                    if temp_floor[i + x][j + y] is 3 and tile_array[i][j] is not 3:
                        print("test stamp results in unmatched doors - skipping")
                        # pretty_print(temp_floor)
                        return False
                    if temp_floor[i + x][j + y] is 1:
                        temp_floor[i + x][j + y] = 9
                        print("test stamp results in collision - skipping")
                        # pretty_print(temp_floor)
                        return False
                    temp_floor[i + x][j + y] = tile_array[i][j]
                except IndexError as e:
                    print("bad things happened! - skipping")
                    print(e)
                    return False

        return True

    def init_doors(self):
        door_positions = []
        tile_array = self.tile_array
        for i in range(0, len(tile_array)):
            for j in range(len(tile_array[0])):

                # square is a door. Add it do the available door list
                if tile_array[i][j] is 3:
                    door_positions.append((i, j))

        self.doors = find_doors(door_positions)
