class Dungeon1D(object):
    def update(self, delta):
        self.map.update(delta)
        if self.game_over:
            return

    def collision(self, obj1, obj2):
        print("{} fights {}".format(obj1.name, obj2.name))

    def __init__(self, the_map):
        """
        :param the_map: The world containing all game objects.
        """
        self.player_pos = 0
        self.map = the_map
        self.game_over = False
