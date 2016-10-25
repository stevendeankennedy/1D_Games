import time

from control.dungeon_1d import Dungeon1D
from model.game_entity import GameEntity
from model.game_space import GameSpace

from DungeonGame.view.renderer_1d import *

LEDs = 20


def main():
    # test objects
    obj1 = GameEntity("X", 25, 10, 10, 10, 10, 10)
    obj1.print_stats()

    obj2 = GameEntity("O", 10, 10, 10, 10, 10, 10)
    obj2.print_stats()

    # test world
    rooms = [5, 3, 8]
    print(rooms)
    world = GameSpace(LEDs, rooms)
    world.add(obj1, 0)
    world.add(obj2, 12)

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