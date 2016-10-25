from DungeonGame.model import game_space

class Renderer1D(object):
    """
        Basic 1D Renderer.
        Renders to serial output, connected to Arduino w/ ws2812b LED Strip
    """

    def __init__(self, game_space):
        self.world = game_space

    def draw(self):
        """Doesn't do anything."""
        pass

class TextRenderer(Renderer1D):
    """
        Text version.
    """

    def draw(self):
        # game_world = self.world.as_string()
        # print(game_world)
        i = 0 # index
        line = ''
        # game_world = self.world.get_array()
        game_world = self.world.world
        rooms = self.world.rooms
        for r in rooms:
            line += '['
            while r > 0:
                r -= 1
                if game_world[i] is None:
                    line += '-'
                else: # something here
                    line += game_world[i].name
                i += 1
            line += ']'  # end of room
        line += '['  # final space... undefined room
        for j in range(i, len(game_world)):
            if game_world[j] is None:
                line += '-'
            else:  # something here
                line += game_world[j].name
        line += ']'  # end undefined room
        print(line)