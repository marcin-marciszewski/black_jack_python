import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card():
    """
    Creates new card object
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        for k, v in values.items():
            if self.rank == k:
                self.value = v

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck():
    """
    Creates new deck object
    """

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.deck.append(new_card)

    def __str__(self):
        return ", ".join(str(x) for x in self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        card = random.choice(self.deck)
        return card
