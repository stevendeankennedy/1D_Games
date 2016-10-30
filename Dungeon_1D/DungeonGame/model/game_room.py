class GameRoom:
    """
        A Room in the dungeon.

        size:   size of room
        spaces: an array of spaces (which could contain GameEntity objects
        type:   the kind of room (overworld, cave, lava)
        next:   this room exits into the next room
    """

    def __init__(self, size, room_type):
        self.size = size
        self.spaces = [None] * self.size
        self.type = room_type
        self.next = None

    def add_entity(self, entity):
        if self.spaces[0] is None:
            self.spaces[0] = entity
        else:
            return False
