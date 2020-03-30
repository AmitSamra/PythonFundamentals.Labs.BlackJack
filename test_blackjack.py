import unittest
from blackjack import Blackjack
from blackjack import Player


class TestCardGame(unittest.TestCase):
    bj = Blackjack()

    def choose_card(self):
        self.assertEqual(bj.choose_card(['A',1],'A'),'A')
        self.assertEqual(bj.choose_card(['A', 1], 1), 1)

if __name__ == '__main__':
    unittest.main()