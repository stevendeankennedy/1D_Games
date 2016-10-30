class Renderer1D(object):
    """
        Basic 1D Renderer.
        Renders to serial output, connected to Arduino w/ ws2812b LED Strip
    """

    def __init__(self, game_space):
        self.world = game_space

    def draw(self):
        """Render output."""
        pass

class TextRenderer(Renderer1D):
    """
        Text version.
    """

    space_text = {  # spaces defines how text output looks
        "overworld": '-',
        "cave": '_',
        "lava": '~'
    }

    def draw(self):
        line = ''  # The line that will be printed

        rooms = self.world.rooms
        for r in rooms:
            line += '|'  # room output beginning wall
            space = self.space_text[r.type]  # what to draw
            spaces = r.spaces

            for i in range(len(spaces)):
                if spaces[i] is None:
                    line += space
                else: # something here
                    line += spaces[i].name
                i += 1
        line += '|'  # end of room
        print(line)
