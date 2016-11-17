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

    def add_entity_at_pos(self, entity, p):
        if p < 0 or p >= len(self.spaces):
            return False
        if self.spaces[p] is None:
            self.spaces[p] = entity
            return True
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

    def finish_update(self):
        """
        Confirm that room has been updated.
        Makes sure all objects will be updated next time around.
        This is necessary since entities can change rooms.
        """
        for e in self.spaces:
            if e is not None:
                e.update_ready()

    def update(self, dt):

        updated = {}  # objects that should be adjusted here

        # Update all objects
        # for e in self.spaces:
        for i in range(len(self.spaces)):
            e = self.spaces[i]
            if e is not None:
                e.update(dt)
                if e.move > 0:
                    self.spaces[i] = None  # remove from room temporarily
                    updated[e] = i  # e as key for attempted update along with original position

        for e, pos in updated.items():
            mov = e.move
            npos = pos + mov

            if (npos >= len(self.spaces)) and (self.next is not None):
                self.next.add_entity(e)
            else:
                self.add_entity_at_pos(e, npos)

            e.updated()
