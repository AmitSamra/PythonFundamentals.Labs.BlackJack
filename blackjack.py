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

show_deck(deck1)

def shuffle_deck(deck):
    shuffle(deck)
    print(deck)

#shuffle_deck(deck1)

def choose_two(deck):
    rand_num1 = randint(0,len(deck)-1)
    a = deck[rand_num1]
    rand_num2 = randint(0, len(deck)-1)
    b = deck[rand_num2]
    print(a,b)

choose_two(deck1)

def simple_game(deck):
    choose_two(deck)

simple_game(deck1)









