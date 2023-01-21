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

def attack(attacker, defender):
    string = ""
    hit_difficulty = defender.defense * 10
    does_hit = randint(0, 100) > hit_difficulty

    if does_hit:
        if not attacker.weapon:
            damage = 1
            string += f"{attacker} punches {defender} for {damage} points of damage."
        else:
            damage = attacker.weapon.damage * 10
            string += f"{attacker} hits {defender} with their {attacker.weapon} for {damage} points of damage."

        defender.hit_points -= damage
        if defender.hit_points <= 0:
            string += f"\n{defender} dies, {attacker} wins!"
            defender.hit_points = 0
            attacker.kills += 1
            defender.deaths += 1
    else:
        string += f"{attacker} swings at {defender} and misses!"
    
    return string