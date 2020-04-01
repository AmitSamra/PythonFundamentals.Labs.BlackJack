import unittest
from blackjack0331 import Blackjack
from blackjack0331 import Player
from unittest import mock


class TestCardGame(unittest.TestCase):

    bj = Blackjack(1)

    def test_choose_card(self):
        self.bj.deck = ['A',1]
        with mock.patch("blackjack0331.randint", return_value = 0):
            self.assertEqual(self.bj.choose_card(),'A')   

    def test_choose_card(self):
        self.bj.deck = ['A',1]
        with mock.patch("blackjack0331.randint", return_value = 1):
            self.assertEqual(self.bj.choose_card(),1)

    ''' 
    Can also do above using following:
    def test_choose_card(self):
        self.bj.deck = ['A',1]
        with mock.patch("blackjack0331.randint", side_effect = [0,1]):
            self.assertEqual(self.bj.choose_card(),'A')
            self.assertEqual(self.bj.choose_card(), 1)
    '''

    def test_return_card_val(self):
        self.assertEqual(self.bj.return_card_val('A'),11)
        self.assertEqual(self.bj.return_card_val(1), 1)

    def test_win_check_player(self):
        self.assertEqual(self.bj.win_check_player(21),True)

    def lose_check_player(self):
        self.assertEqual(self.bj.lose_check_player(22), True)



class TestPlayer(unittest.TestCase):

    pl = Player('Apple')
    pl.hand = ['A']

    def test_add_score(self):
        self.assertEqual(self.pl.add_score(), 11)











if __name__ == '__main__':
    unittest.main()

