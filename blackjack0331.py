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
       # [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J','Q','K', 'A']
       # [0, 1, 2, 3, 4, 5, 6, 7,  8,  9, 10, 11, 12,]

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

    def win_check_player(self, score):
        if score == 21:
            print('Player wins!')
            return True

    def lose_check_player(self, score):
        if score > 21:
            print("Player loses!")
            return True

    def win_check_dealer(self, score):
        if score == 21:
            print('Dealer wins!')
            return True

    def lose_check_dealer(self, score):
        if score > 21:
            print('Dealer loses!')
            return True

    def first_deal(self, ):
        pass

    def print_hand_total(self,player):
        print(f"Player Hand {player.hand}")
        print(f"Player Total: {player.add_score()}")

    def print_hand_total_dealer(self,dealer):
        print(f"Dealer Hand {dealer.hand}")
        print(f"Dealer Total: {dealer.add_score()}")

    def append_hand(self, player):
        player.hand.append(self.choose_card(self.deck))

    def compare(self, player, dealer):
        if player.total == dealer.total:
            print("Tie game!")
        elif player.total > dealer.total:
            print("Player wins!")
        else:
            print("Dealer wins!")


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



bj1 = Blackjack(1)
deck1 = bj1.create_deck()

player1 = Player('Apple')
dealer = Player('Dealer')

def main_fcn(deck, player, bj):
    print("")
    play_game = input("Are you ready to play? Y/N ")
    print("-"*50)
    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        print("Initial Deal")
        bj.append_hand(player)
        bj.append_hand(player)
        player.add_score()
        bj.print_hand_total(player)
        if bj.win_check_player(player.total):
            game_on = False
            break
        elif player.total < 21:
            while player.total < 21:
                hs_choice = bj.hit_stay()
                if hs_choice == 1:
                    bj.append_hand(player)
                    player.add_score()
                    bj.print_hand_total(player)
                    if bj.win_check_player(player.total):
                        game_on = False
                        #break
                    #elif bj.lose_check(player.total):
                     #   game_on = False
                        #break
                elif hs_choice == 0:
                    print("")
                    print("Dealer's Turn")
                    while dealer.total <= 16:
                        bj.append_hand(dealer)
                        dealer.add_score()
                        bj.print_hand_total_dealer(dealer)
                    else:
                        if not bj.win_check_dealer(dealer.total):
                            bj.compare(player, dealer)
                            game_on = False
                            break
                else:
                    hs_choice = bj.hit_stay()
            else:
                if bj.lose_check_player(player.total):
                    game_on = False
                    break
        else:
            if bj.lose_check_player(player.total):
                game_on = False
main_fcn(deck1, player1, bj1)

if __name__ == "__main__":
    bj1 = Blackjack(1)
    deck1 = bj1.create_deck()
    player1 = Player('Apple')
    dealer = Player('Dealer')
    main_fcn(deck1, player1, bj1)
