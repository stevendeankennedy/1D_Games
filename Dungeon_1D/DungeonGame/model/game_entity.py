class GameEntity(object):
    """The superclass for all objects that exist in the game world.

    Attributes:
        name: - name of the object
        HP - HP and max HP
        attack - attack
        defense - defense
        sp_atk - special attack
        sp_def - special defense
        speed - speed
        move:  # of spaces this entity wants to move.  +1 means right 1, -3 means left 3
    """

    def __init__(self, name, maxhp, attack, defense, sp_atk, sp_def, speed):
        self.name = name
        self.maxhp = maxhp
        self.attack = attack
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed

        self.move = 0
        self.needs_update = True

    def print_stats(self):
        stats = "!{:<10s}-----\n ATK:{:>8}\n DEF:{:>8}\n SPA:{:>8}\n SPD:{:>8}\n SPEED:{:>6}\n HP:{:>9}"\
            .format(self.name, self.attack, self.defense, self.sp_atk, self.sp_def, self.speed, self.maxhp)
        print(stats)

    def update(self, dt):
        if self.needs_update:
            self.update_behavior(dt)

    def update_behavior(self, dt):
        self.move = 1  # just move up 1

    def updated(self):
        """
        Has just been updated.
        """
        self.move = 0
        self.needs_update = False

    def update_ready(self):
        """
        Ready for next update.
        """
        self.needs_update = True
