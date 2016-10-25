class Dungeon1D(object):
    def update(self, delta):
        if self.game_over:
            return

        o = self.map.remove(self.player_pos)
        o2 = self.map.peek(self.player_pos + 1)
        if not o2 is None:
            self.collision(o, o2)

        self.player_pos += 1

        if not self.map.add(o, self.player_pos):
            self.game_over = True

    # def draw(self):
    #     print(self.map.as_string())

    def collision(self, obj1, obj2):
        print("{} fights {}".format(obj1.name, obj2.name))

    def __init__(self, the_map):
        self.player_pos = 0
        self.map = the_map
        self.game_over = False
