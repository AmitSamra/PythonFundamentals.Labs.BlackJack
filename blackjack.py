from random import randint
from random import shuffle

def create_deck():
    deck = []
    for i in range(2,11):
        deck.append(i)
    deck.append('J')
    deck.append('Q')
    deck.append('K')
    deck.append('A')
    return deck

deck1 = create_deck()

def show_deck(deck):
    print(deck)

def shuffle_deck(deck):
    shuffle(deck)
    print(deck)

def choose_card(deck):
    rand_num1 = randint(0,len(deck)-1)
    a = deck[rand_num1]
    return a

def return_card_val(card):
    if type(card) == int:
        card_val = card
    elif card == 'A':
        card_val = 11
    else:
        card_val = 10
    return card_val

def hit_stay():
    hs_op = int(input('Enter 1 to hit or 0 to stay: '))
    return hs_op

def first_deal():
    pass

def win_check(score):
    return score == 21

def replay(input):
    return input("Do you want to play again? Y/N ").lower().startswith('y')

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
