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
    """

    def __init__(self, name, maxhp, attack, defense, sp_atk, sp_def, speed):
        self.name = name
        self.maxhp = maxhp
        self.attack = attack
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed

    def print_stats(self):
        stats = "!{:<10s}-----\n ATK:{:>8}\n DEF:{:>8}\n SPA:{:>8}\n SPD:{:>8}\n SPEED:{:>6}\n HP:{:>9}"\
            .format(self.name, self.attack, self.defense, self.sp_atk, self.sp_def, self.speed, self.maxhp)
        print(stats)