class Card(object):
    SUITS = [
        'Spades',
        'Hearts',
        'Diamonds',
        'Clubs',
    ]

    VALUES = {
        'Ace': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5,
        'Six': 6,
        'Seven': 7,
        'Eight': 8,
        'Nine': 9,
        'Ten': 10,
        'Jack': 11,
        'Queen': 12,
        'King': 13,
    }

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
