import time

from DungeonGame.control.dungeon_1d import Dungeon1D
from DungeonGame.model.game_space import GameSpace
from DungeonGame.model.game_room import GameRoom
from DungeonGame.model.game_entity import GameEntity

from DungeonGame.view.renderer_1d import *

# LEDs = 20


def main():
    # test objects
    obj1 = GameEntity("X", 25, 10, 10, 10, 10, 10)
    obj1.print_stats()

    obj2 = GameEntity("O", 10, 10, 10, 10, 10, 10)
    obj2.print_stats()

    # test world
    rooms = [GameRoom(5, "overworld"), GameRoom(3, "cave"), GameRoom(8, "lava"), GameRoom(5, "overworld"), GameRoom(3, "cave")]
    world = GameSpace(rooms)
    world.add(obj1, 0)
    world.add(obj2, 2)

    dungeon_1d = Dungeon1D(world)
    renderer_1d = TextRenderer(world)

    fps = 2
    last_frame_time = 0
    while not dungeon_1d.game_over:
        current_time = time.time()
        dt = current_time - last_frame_time
        last_frame_time = current_time

        dungeon_1d.update(dt)   # <-- Update ------------
        renderer_1d.draw()      # <-- Draw --------------

        sleep_time = 1 / fps - (current_time - last_frame_time)
        if sleep_time > 0:
            time.sleep(sleep_time)

main()
