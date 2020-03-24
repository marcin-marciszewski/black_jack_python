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


class Hand():
    """
    Creates new hand (player) object
    """

    def __init__(self):
        self.cards = []
        self.values = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.values += card.value
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        if self.aces != 0 and self.values > 21:
            self.values -= 10
            self.aces = 0

    def __str__(self):
        cards = ", ".join(str(x) for x in self.cards)
        return f'cards: {cards} value: {self.values}'


class Chips():
    """
    Creates new chips for the player
    """

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += (self.bet)*2

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    """
    Take a bet from the user and checks how many chips left
    """
    while True:
        try:
            players_bet = int(input('How much you want to bet:> '))
            if players_bet <= chips.total:
                chips.bet = players_bet
                remaining_chips = chips.total - players_bet
                print(
                    f'Your bet is: {players_bet}, you have {remaining_chips} remaining chips\n')
                break
            else:
                print('Not enough chips\n')
        except ValueError:
            print('Please put valid value\n')


def hit(hand, deck):
    """
    Chose random card from the deck and add it to the player's cards
    """
    card = deck.deal()
    hand.add_card(card)
    hand.adjust_for_ace()
    deck.deck.remove(card)


def check_win(chips, player, croupier):
    """
    Checks if there is a winner
    """
    if (player.values <= 21 and croupier.values > 21) or (player.values <= 21 and croupier.values <= 21 and player.values > croupier.values):
        chips.win_bet()
        print(f'Player wins.\nYour chips: {chips.total}\n')
    elif player.values == croupier.values:
        print(f"Draw\nYour chips: {chips.total}\n")
    else:
        chips.lose_bet()
        print(f'Croupier wins\nYour chips: {chips.total}\n')
