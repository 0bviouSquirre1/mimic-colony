"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia.objects.objects import DefaultCharacter
from evennia.typeclasses.attributes import AttributeProperty

from .objects import ObjectParent


class Character(ObjectParent, DefaultCharacter):

    carried_gold = AttributeProperty(0, category="wealth")
    stored_gold = AttributeProperty(0, category="wealth")
    carried_gems = AttributeProperty(0, category="wealth")
    stored_gems = AttributeProperty(0, category="wealth")

    hit_points = AttributeProperty(100, category="stats")
    defense = AttributeProperty(0, category="stats")
    charisma = AttributeProperty(0, category="stats")

    boost_hit_points = AttributeProperty(0, category="stats")
    boost_defense = AttributeProperty(0, category="stats")
    boost_charisma = AttributeProperty(0, category="stats")

    deaths = AttributeProperty(0, category="tallies")
    kills = AttributeProperty(0, category="tallies")
    victories = AttributeProperty(0, category="tallies")
