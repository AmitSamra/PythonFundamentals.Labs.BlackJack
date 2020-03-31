import unittest
from blackjack import Blackjack
from blackjack import Player


class TestCardGame(unittest.TestCase):
    bj = Blackjack(4)

    def test_choose_card(self):
        self.assertEqual(self.bj.choose_card(['A',1]),'A')
        self.assertEqual(self.bj.choose_card(['A', 1],1), 1)

    def test_return_card_val(self):
        self.assertEqual(self.bj.return_card_val('A'),11)
        self.assertEqual(self.bj.return_card_val(1), 1)

class TestPlayer(unittest.TestCase):
    pl = Player('Apple')

    def test_add_score(self):
        self.assertEqual(self.pl.add_score(['A']), 11)

if __name__ == '__main__':
    unittest.main()

