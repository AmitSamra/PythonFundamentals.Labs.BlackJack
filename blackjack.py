from random import randint

rand_num = randint(1,11)
#print(rand_num

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

'''
def create_deck():
    deck = []
    for i in ['Diamonds', 'Clubs', 'Hearts', 'Spades']:
        for j in range(2,11):
            deck.append( {i:j} )
    deck.append({'Diamonds': 'J'})
    deck.append({'Diamonds': 'Q'})
    deck.append({'Diamonds': 'K'})
    deck.append({'Diamonds': 'A'})
    deck.append({'Clubs': 'J'})
    deck.append({'Clubs': 'Q'})
    deck.append({'Clubs': 'K'})
    deck.append({'Clubs': 'A'})
    deck.append({'Hearts': 'J'})
    deck.append({'Hearts': 'Q'})
    deck.append({'Hearts': 'K'})
    deck.append({'Hearts': 'A'})
    return deck

a = create_deck()

def show_deck(deck):
    for item in deck:
        print(item)

show_deck(a)
'''
