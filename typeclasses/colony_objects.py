from evennia.typeclasses.attributes import AttributeProperty

from .objects import Object

class Weapon(Object):

    speed = AttributeProperty(1, category="stats")
    damage = AttributeProperty(1, category="stats")
