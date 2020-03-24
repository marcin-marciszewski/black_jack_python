import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


player_playing = True
croupier_playing = False


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
        """
        Shuffles the deck
        """
        random.shuffle(self.deck)

    def deal(self):
        """
        Deals a random card to a player
        """
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
        """
        Adds dealt card to player's cards
        """
        self.cards.append(card)
        self.values += card.value
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        """
        Check if ace should give 1 or 11
        """
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
        """
        Add chips to the account after winning
        """
        self.total += (self.bet)*2

    def lose_bet(self):
        """
        Deduct chips after
        """
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


def game():
    print("Welcome to Black Jack game")
    chips = Chips()
    while True:
        if chips.total == 0:
            repeat()
        new_deck = Deck()
        new_deck.shuffle()
        player = Hand()
        croupier = Hand()
        print("Please put your bet.")
        take_bet(chips)
        hit(player, new_deck)
        hit(player, new_deck)
        hit(croupier, new_deck)

        print(f'Player:> {player}')
        print(f'Croupier:> {croupier}\n')

        while player_playing:
            user_choice = input("Hit or stand, press h or s:> ")
            if user_choice == 'h':
                hit(player, new_deck)
                print(f'Player:> {player}')
                print(f'Croupier:> {croupier}\n')
                if player.values > 21:
                    chips.lose_bet()
                    print(f'Croupier wins\nYour chips: {chips.total}\n')
                    croupier_playing = False
                    break
            elif user_choice == 's':
                croupier_playing = True
                break

        if croupier_playing:
            while croupier.values <= 17:
                hit(croupier, new_deck)
                print(f'Player:> {player}')
                print(f'Croupier:> {croupier}\n')
                if croupier.values > 17:
                    check_win(chips, player, croupier)
                    break


def repeat():
    """
    Asks the player if he wants to play again when chips = 0
    """
    answer = "x"
    while answer.lower() != "yes" or answer.lower() != "no":
        answer = input(
            "No more chips. Do you want to play again? Yes or No:> ")
        if answer.lower() == "yes" or answer.lower() == "no":
            break
    if answer.lower() == "yes":
        game()
    else:
        print("Good bye.")
        exit()


game()
