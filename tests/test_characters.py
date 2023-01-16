from evennia.utils.test_resources import EvenniaTest


class TestCharacter(EvenniaTest):
    def test_new_character(self):
        char1 = self.char1

        self.assertEqual(char1.carried_gold, 0)
        self.assertEqual(char1.stored_gold, 0)
        self.assertEqual(char1.carried_gems, 0)
        self.assertEqual(char1.stored_gems, 0)

        self.assertEqual(char1.hit_points, 100)
        self.assertEqual(char1.defense, 0)
        self.assertEqual(char1.charisma, 0)

        self.assertEqual(char1.boost_hit_points, 0)
        self.assertEqual(char1.boost_defense, 0)
        self.assertEqual(char1.boost_charisma, 0)

        self.assertEqual(char1.deaths, 0)
        self.assertEqual(char1.kills, 0)
        self.assertEqual(char1.victories, 0)
