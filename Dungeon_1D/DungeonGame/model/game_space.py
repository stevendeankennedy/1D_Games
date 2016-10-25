class GameSpace(object):
    """
    The 1D Game World.  It is made up of an array.

        world - array for world
        size = size of world
        rooms: size of rooms, in order

    """
    def __init__(self, size, rooms):
        self.world = [None] * size
        self.rooms = rooms

    def add(self, entity, index):
        if index >= len(self.world):
            print("Can't add {}.  Index {} out of bounds".format(entity.name, index))
            return False
        # add entity to world
        old = self.world[index]
        self.world[index] = entity

        return True

    def peek(self, index):
        if index < 0 or index >= len(self.world):
            return None
        return self.world[index]

    def remove(self, index):
        o = self.world[index]
        self.world[index] = None
        return o


