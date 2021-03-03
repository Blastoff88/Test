__author__ = 'Zac Keepers and Caleb Durda'


class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for fighting.",
                         value=0,
                         damage=5)


class Blaster(Weapon):
    def __init__(self):
        super().__init__(name="Blaster",
                         description="A small blaster with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=10)


class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin made out of gold".format(str(self.amt)),
                         value=self.amt)