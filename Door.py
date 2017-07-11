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