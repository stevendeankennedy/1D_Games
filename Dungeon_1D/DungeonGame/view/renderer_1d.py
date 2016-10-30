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
        line = ''  # The line that will be printed
        space_text = {  # spaces defines how text output looks
            "overworld": '-',
            "cave": '_',
            "lava": '~'
        }
        rooms = self.world.rooms
        for r in rooms:
            line += '|'  # room output beginning wall
            space = space_text[r.type]  # what to draw
            spaces = r.spaces
            # if space is None:
            #     space = ' '
            for i in range(len(spaces)):
                if spaces[i] is None:
                    line += space
                else: # something here
                    line += spaces[i].name
                i += 1
        line += '|'  # end of room
        print(line)
