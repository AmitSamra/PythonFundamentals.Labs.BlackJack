from random import randint

rand_num = randint(1,11)
#print(rand_num)

def create_deck():
    deck = []
    for i in ['Diamonds', 'Clubs', 'Hearts', 'Spades']:
        for j in range(2,11):
            deck.append( {i:j} )
            deck.append({'Diamonds': 'J'})
            deck.append({'Diamonds': 'Q'})
            deck.append({'Diamonds': 'K'})
            deck.append({'Diamonds': 'A'})
    return deck

a = create_deck()

def show_deck(deck):
    print(deck)

show_deck(a)

