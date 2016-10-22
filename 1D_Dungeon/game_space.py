class GameSpace:
    'The 1D Game World.  It is made up of an array.'

    # world - array for world
    # size = size of world

    def __init__(self, size):
        self.world = [None] * size

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

    def as_string(self):
        line = ''
        for i in range(len(self.world)):
            if self.world[i] is None:
                line += '[-]'
            else:
                line += "[" + self.world[i].name + ']'
        return line
