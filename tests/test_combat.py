from evennia.utils.test_resources import EvenniaTest
from evennia import create_object
from world import combat_system
from typeclasses import colony_objects

class TestWeapons(EvenniaTest):
    def test_create_weapon(self):
        item = create_object('typeclasses.colony_objects.Weapon', "dagger")

        self.assertEquals(item.speed, 1)
        self.assertEquals(item.damage, 1)

class TestCombat(EvenniaTest):
    def setUp(self):
        
        return super().setUp()
    def test_attack(self):
        combat_system.attack(self.char1, self.char2)

        self.assertEquals(self.char2.hit_points, 90)