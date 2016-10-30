class Dungeon1D(object):
    def update(self, delta):
        if self.game_over:
            return

    def collision(self, obj1, obj2):
        print("{} fights {}".format(obj1.name, obj2.name))

    def __init__(self, the_map):
        self.player_pos = 0
        self.map = the_map
        self.game_over = False
