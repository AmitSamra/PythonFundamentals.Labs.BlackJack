from random import randint

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

    def first_deal(self, ):
        pass


class Player():
    def __init__(self, name):
        super().__init__()
        self.name = name,

        self.hand = []
        self.total = 0

    def add_score(self):
        self.total = 0
        for card in self.hand:
            if type(card) == int:
                self.total += card
            elif card == 'A':
                self.total += 11
            else:
                self.total += 10
        if self.total >= 22 and 'A' in self.hand:
            self.total -= 10*self.hand.count('A')
        return self.total

    def player_first_deal(self):
        pass

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
        player.total = 0

        acard1 = bj.choose_card(deck)
        player.hand.append(acard1)
        acard2 = bj.choose_card(deck)
        player.hand.append(acard2)
        total = player.add_score()

        print(f"Current Hand {player.hand}")
        print(f"Player Total: {total}")
        print("-"*25)

        if bj.win_check(player.total):
            player.add_score()
            print('You win!')
            if not bj.replay():
                print("-" * 25)
                game_on = False

        elif player.total < 21:
            while player.total < 21:
                hs_choice = bj.hit_stay()
                print(' ')
                if hs_choice == 1:

                    acard3 = bj.choose_card(deck)
                    player.hand.append(acard3)
                    total = player.add_score()

                    print(f"Current hand {player.hand}")
                    print(f"Player Total: {total}")
                    print("-" * 25)
                    if bj.win_check(player.total):
                        player.add_score()
                        print('You win!')
                        game_on = False
                        break

                elif hs_choice == 0:

                    dealer.hand = []
                    dealer.total = 0

                    while dealer.total <= 17:
                        bcard3 = bj.choose_card(deck)
                        dealer.hand.append(bcard3)
                        total = dealer.add_score()
                        print(f"Dealer Hand {dealer.hand}")
                        print(f"Dealer Total: {total}")

                    else:
                        if bj.win_check(dealer.total):
                            print('Dealer wins!')
                            game_on = False
                            break

                        elif (dealer.total > player.total) and (dealer.total <= 21):
                            print('Dealer wins!')
                            game_on = False
                            break

                        elif dealer.total == player.total:
                            print("Tie Game!")
                            game_on = False
                            break

                        else:
                            print('Player wins!')
                            game_on = False
                            break

                    #else:
                     #   game_on = False
                else:
                    game_on = False
            else:
                print('You lose!')
                print(' ')
                game_on = False
    else:
        print('Goodbye')

main_fcn(deck1, player1, bj1)
