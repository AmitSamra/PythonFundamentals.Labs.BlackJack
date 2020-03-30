from random import randint
from random import shuffle

class CardGame():
   def __init__(self, deck_count):
       self.deck_count = deck_count

   def create_deck(self):
       self.deck = []
       for i in range(2, 11):
        self.deck.append(i)
       self.deck.append('J')
       self.deck.append('Q')
       self.deck.append('K')
       self.deck.append('A')
       return self.deck*self.deck_count

   def show_deck(self, deck):
       print(self.deck)

   def shuffle_deck(self, deck):
       shuffle(self.deck)
       print(self.deck)

   def replay(self):
       return input("Do you want to play again? Y/N ").lower().startswith('y')

class Blackjack(CardGame):
    def __init__(self, deck_count):
        super().__init__(deck_count)
        self.values = {
        2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10,
        'J':10, 'Q':10, 'K':10, 'A':11}

    def choose_card(self, deck):
        rand_num1 = randint(0, len(self.deck) - 1)
        a = self.deck[rand_num1]
        return a

    def hit_stay(self):
        hs_op = int(input('Enter 1 to hit or 0 to stay: '))
        return hs_op

    def return_card_val(self,card):
        if type(card) == int:
            card_val = card
        elif card == 'A':
            card_val = 11
        else:
            card_val = 10
        return card_val

    def win_check(self, score):
        return score == 21

    def first_deal(self):
        pass


class Player():
    def __init__(self, name, score = 0):
        super().__init__()
        self.name = name,
        self.score = score

        self.hand = []
        self.hand_val = []

    def add_score(self):
        self.score += 1



bj1 = Blackjack(1)
deck1 = bj1.create_deck()

player1 = Player('Apple')

dealer = Player('Dealer')


def main_fcn(deck, player, bj):

    play_game = input("Are you ready to play? Y/N ")
    print("-"*50)
    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        print("Initial Deal")
        print("-" * 25)

        player.hand = []
        player.hand_val = []

        acard1 = 'A'#bj.choose_card(deck)
        player.hand.append(acard1)
        aval1 = 11#bj.return_card_val(acard1)
        player.hand_val.append(aval1)

        acard2 = '9'#bj.choose_card(deck)
        player.hand.append(acard2)
        aval2 = 9#bj.return_card_val(acard2)
        player.hand_val.append(aval2)

        print(f"Current Hand {player.hand}")
        print(f"Player Total: {sum(player.hand_val)}")
        print("-"*25)
        game_on = False

        if bj.win_check(sum(player.hand_val)):
            player.add_score()
            print('You win!')
            if not bj.replay():
                print("-" * 25)
                game_on = False

        elif sum(player.hand_val) < 21:
            while sum(player.hand_val) < 21:
                hs_choice = bj.hit_stay()
                if hs_choice == 1:

                    acard3 = 5#bj.choose_card(deck)
                    player.hand.append(acard3)
                    aval3 = bj.return_card_val(acard3)
                    player.hand_val.append(aval3)
                    if 'A' in player.hand and sum(player.hand_val) >= 11:
                        player.hand_val.append(-10*player.hand.count('A'))


                    #elif #acard3 == 'A' and player.hand_val.count('A')>1:
                        #aval3 = bj.return_card_val(acard3)

                    #elif 'A' in player.hand:
                     #   aval3 = bj.return_card_val(acard3)

                    #player.hand.append(acard3)
                    #player.hand_val.append(aval3)
                    #aval3 = 11#bj.return_card_val(acard3)
                    #player.hand_val.append(aval3)

                    '''if sum(player.hand_val) > 21 and 'A' in player.hand:
                        while sum(player.hand_val) > 21:
                            for i in player.hand:
                                if i == 'A':
                                    sum(player.hand_val) -= 10
                                    if sum(player.hand_val) < 21:
                                        break'''

                    print(f"Current Hand {player.hand}")
                    print(f"Player Total: {sum(player.hand_val)}")
                    print("-" * 25)
                    if sum(player.hand_val) == 21:
                        print('You win!')
                        game_on = False

                elif hs_choice == 0:
                    dealer.hand = []
                    dealer.hand_val = 0
                    bcard1 = bj.choose_card(deck)
                    dealer.hand.append(bcard1)
                    bval1 = bj.return_card_val(bcard1)
                    print(f"Card: {bcard1} Value: {bval1}")
                    acard2 = bj.choose_card(deck)
                    dealer.hand.append(acard2)
                    bval2 = bj.return_card_val(acard2)
                    print(f"Card: {acard2} Value: {bval2}")
                    dealer.hand_val = bval1 + bval2
                    print(f"Current hand {dealer.hand}")
                    print(f"Dealer Total: {dealer.hand_val}")

                    while dealer.hand_val <= 17:
                        bcard3 = bj.choose_card(deck)
                        player.hand.append(bcard3)
                        if bcard3 == 'A' and dealer.hand_val > 21:
                            bval3 = 11
                        else:
                            bval3 = bj.return_card_val(bcard3)

                        if bj.win_check(dealer.hand_val):
                            dealer.add_score()
                            print('You win!')
                            game_on = False
                            break
                        elif (dealer.hand_val > sum(player.hand_val)) and (dealer.hand_val <= 21):
                            dealer.add_score()
                            print('Dealer wins!')
                            game_on = False
                        else:
                            print('Player wins!')
                            game_on = False
                            break
                    else:
                        game_on = False
            else:
                print('You lose Line 194!')
                print(' ')
                if not bj.replay():
                    print("-" * 25)
                    game_on = False
    else:
        print('Goodbye')

main_fcn(deck1, player1, bj1)
