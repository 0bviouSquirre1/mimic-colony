# black box that does all combat-related calculations
#
# weapons have SPD and DMG
# fighters have HP and DEF
#
# HP is not used in calculations
# DEF determines chance of making contact
# DMG determines how many HP the enemy loses when hit
# SPD determines how quickly the next attack can occur
#
# if DEF = 0, then hit chance = 100%
# if DEF = 10, then hit chance = 0%
# hit chance = 100 - def(10)
#
# damage = dmg(10) // 10, 20, or 30 damage

from random import randint

def attack(self, attacker, defender):
    hit_chance = 100 - defender.defense(10)
    damage = attacker.weapon.damage(10)
    pass