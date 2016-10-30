class GameSpace(object):
    """
    The 1D Game World.  It is made up of an array.

        world - array for world
        size = size of world
        rooms: size of rooms, in order

    """

    def __init__(self, rooms):
        self.rooms = rooms
        # Set up exit pointers
        for i in range(len(self.rooms) - 1):  # last room's pointer stays None
            self.rooms[i].next = i + 1

    def add(self, entity, room):
        success = self.rooms[room].add_entity(entity)
        return success
