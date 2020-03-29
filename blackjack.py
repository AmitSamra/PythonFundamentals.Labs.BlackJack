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

   def replay(self, input):
       return input("Do you want to play again? Y/N ").lower().startswith('y')

class Blackjack(CardGame):
    def __init__(self, deck_count):
        super().__init__(deck_count)

    def choose_card(self, deck):
        rand_num1 = randint(0, len(self.deck) - 1)
        a = self.deck[rand_num1]
        return a

    def hit_stay():
        hs_op = int(input('Enter 1 to hit or 0 to stay: '))
        return hs_op

    def return_card_val(card):
        if type(card) == int:
            card_val = card
        elif card == 'A':
            card_val = 11
        else:
            card_val = 10
        return card_val

    def win_check(score):
        return score == 21

    def first_deal():
        pass



bj1 = Blackjack(2)
a = bj1.create_deck()
print(a)

""""
deck1 = create_deck()






def simple_game(deck):

    play_game = input("Are you ready to play? Y/N ")
    print("-"*50)
    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        hand = []
        total = 0
        #show_deck(deck)
        acard1 = choose_card(deck)
        hand.append(acard1)
        aval1 = return_card_val(acard1)

        print("Initial Deal")
        print("-"*25)

        print(f"Card: {acard1} Value: {aval1}")
        acard2 = choose_card(deck)
        hand.append(acard2)
        aval2 = return_card_val(acard2)
        print(f"Card: {acard2} Value: {aval2}")
        total = aval1 + aval2
        print(f"Current hand {hand}")
        print(f"Total: {total}")
        print("-"*25)

        if win_check(total):
            print('You win!')
            game_on = False

        else:
            while total < 21:
                hs_choice = hit_stay()
                if hs_choice == 1:
                    acard3 = choose_card(deck)
                    hand.append(acard3)
                    if acard3 == 'A' and total > 21:
                        aval3 = 11
                    else:
                        aval3 = return_card_val(acard3)
                    print(f"Card: {acard3} Value: {aval3}")
                    total += aval3
                    print(f"Current hand {hand}")
                    print(f"Total: {total}")
                    print("-" * 25)
                    if win_check(total):
                        print('You win!')
                        game_on = False
                elif hs_choice == 0:
                    break
                else:
                    game_on = False
            else:
                print('You lose!')
                game_on = False
    else:
        print('Goodbye')

simple_game(deck1)
"""