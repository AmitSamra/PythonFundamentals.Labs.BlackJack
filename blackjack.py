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

#show_deck(deck1)

def shuffle_deck(deck):
    shuffle(deck)
    print(deck)

card_values = {
    'J':10, 'Q':10, 'K':10, 'A':11
}

#shuffle_deck(deck1)

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

def simple_game(deck):
    show_deck(deck)
    a = choose_card(deck)
    print(f"Card: {a}")
    b = return_card_val(a)
    print(f"Value: {b}")



simple_game(deck1)
