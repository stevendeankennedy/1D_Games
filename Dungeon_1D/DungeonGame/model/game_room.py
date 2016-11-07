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
            return True
        else:
            return False

    def add_obstacle(self, entity):
        """
        Puts something at the back of the room.
        :param entity: Thing to put in
        :return: Whether add was successful
        """
        pos = len(self.spaces) - 2
        if self.spaces[pos] is None:
            self.spaces[pos] = entity
            return True
        else:
            return False

    def update(self, dt):
        for e in self.spaces:
            if e is not None:
                e.update(dt)