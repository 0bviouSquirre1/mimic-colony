from evennia.utils.test_resources import EvenniaTest
from evennia import prototypes
from world import combat_system
from typeclasses import colony_objects

class TestWeapons(EvenniaTest):
    def test_create_weapon(self):
        item = prototypes.spawner.spawn("dagger")[0]

        self.assertEquals(item.speed, 3)
        self.assertEquals(item.damage, 1)

class TestCombat(EvenniaTest):
    def setUp(self):
        super().setUp()
        dagger = prototypes.spawner.spawn("dagger")[0]
        self.char1.weapon = dagger

    def test_attack_hit(self):
        attacker = self.char1
        defender = self.char2
        defender.defense = 0

        string = combat_system.attack(attacker, defender)
        test_string = f"{attacker} hits {defender} for 10 points of damage."

        self.assertEquals(string, test_string)
        self.assertEquals(defender.hit_points, 90)
    
    def test_attack_miss(self):
        attacker = self.char1
        defender = self.char2
        defender.defense = 10

        string = combat_system.attack(attacker, defender)
        test_string = f"{attacker} swings at {defender} and misses!"

        self.assertEquals(string, test_string)
        self.assertEquals(defender.hit_points, 100)
    
    def test_attack_kill(self):
        attacker = self.char1
        defender = self.char2
        defender.hit_points = 10

        string = combat_system.attack(attacker, defender)
        test_string = f"{attacker} hits {defender} for 10 points of damage.\n{defender} dies, {attacker} wins!"
        
        self.assertEquals(string, test_string)
        self.assertEquals(defender.hit_points, 0)