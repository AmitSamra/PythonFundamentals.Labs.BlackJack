import unittest
from blackjack import Blackjack
from blackjack import Player


class TestCardGame(unittest.TestCase):
    bj = Blackjack()

    def test_choose_card(self):
        self.assertEqual(bj.choose_card(['A',1],'A'),'A')
        self.assertEqual(bj.choose_card(['A', 1], 1), 1)

    def test_return_card_val(self):
        self.assertEqual(bj.return_card_val(['A',1],'A'),11)
        self.assertEqual(bj.return_card_val(['A',1], 1), 1)

class TestPlayer(unittest.TestCase):
    pl = Player()

    def test_add_score(self):
        self.assertEqual(pl.add_score('A'), 11)

if __name__ == '__main__':
    unittest.main()