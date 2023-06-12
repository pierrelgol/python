import random


Deck = []
Suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
Player = []
Dealer = []
Ranks = [
    {"rank": "A",  "value": 11},
    {"rank": "K",  "value": 10},
    {"rank": "Q",  "value": 10},
    {"rank": "J",  "value": 10},
    {"rank": "10", "value": 10},
    {"rank": "9",  "value":  9},
    {"rank": "8",  "value":  8},
    {"rank": "7",  "value":  7},
    {"rank": "6",  "value":  6},
    {"rank": "5",  "value":  5},
    {"rank": "4",  "value":  4},
    {"rank": "3",  "value":  3},
    {"rank": "2",  "value":  2},
]


def print_deck():
    for card in Deck:
        print(f"Your card is : {card}")


def print_cards_dealt():
    for card in Player:
        print(f"Your card is : {card}")
    for card in Dealer:
        print(f"Your card is : {card}")


def set_deck():
    for s in Suits:
        for r in Ranks:
            Deck.append([s, r])
    return Deck


def shuffle_deck():
    random.shuffle(Deck)


def get_random_cards(number):
    cards_dealt = []
    for x in range(number):
        card = Deck.pop()
        cards_dealt.append(card)
    return cards_dealt


set_deck()
shuffle_deck()
Player = get_random_cards(2)
Dealer = get_random_cards(2)
print_cards_dealt()
