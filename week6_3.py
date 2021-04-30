# MIS 132 - April 30
# Simple War Game Preparation
# Card, deck, player classes

import random
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}

# Card Class

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

two_hearts = Card(suits[0], ranks[0])
#print(two_hearts)
#print(two_hearts.value)

# Deck Class

class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
        print("A deck has been created.")

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


my_deck = Deck()
my_deck.shuffle()

#print(len(my_deck.all_cards))
#for card in my_deck.all_cards:
#    print(card)

#new_card = my_deck.deal_one()
#print(new_card)
#print(len(my_deck.all_cards))


# Player Class

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []
        print(f"Player '{self.name}' has joined the game.")

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"


player_a = Player("a")
print(player_a)

#player_a.add_cards(my_deck.deal_one())
#print(player_a.all_cards[0])
#print(player_a)
