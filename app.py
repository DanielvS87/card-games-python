from random import randint


class Deck:
    def __init__(self):
        self.cards = []
        self.current_index = 1
        self.last_card = None
        self.next_card = None

    def get_next_card(self):
        if self.current_index != 0:
            next_card = self.cards[self.current_index]
            self.current_index = self.current_index + 1
            self.next_card = next_card

    def first_card(self):
        if self.current_index == 1:
            self.last_card = self.cards[self.current_index-1]

    def deck_empty(self):
        if len(self.cards) == self.current_index:
            return True
        else:
            return False

    def shuffle_deck(self):
        list_range = range(0, len(self.cards))
        for card in list_range:
            random_card = randint(list_range[0], list_range[-1])
            self.cards[card], self.cards[random_card] = self.cards[random_card], self.cards[card]
        return self.cards

    def initialize(self):
        self.shuffle_deck()
        self.first_card()
        self.get_next_card()


class Card:
    def __init__(self, suit, card, amount, color):
        self.suit = suit
        self.card = card
        self.amount = amount
        self.color = color

    def get_card(self):
        return f"{self.card} of {self.suit}"


# lists to create the deck of cards
suits = ["clubs", "spades", "diamonds", "hearts"]
cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
amounts = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
color = ["red", "black"]
deck = Deck()


# Create deck of cards
for i in range(len(cards)):
    for j in range(len(suits)):
        if suits[j] == "clubs" or suits[j] == "spades":
            color = "black"
        else:
            color = "red"
        deck.cards.append(Card(suits[j],
                               cards[i],
                               amounts[i],
                               color))


# guessing game if next card is higher or lower than the previous one
def higher_lower():
    deck.initialize()
    score = 0
    total_guesses = 0
    end_game = False
    while not deck.deck_empty() or not end_game:
        print(deck.last_card.get_card())
        guess = input("is the next card higher(h) or lower(l)? Or want to Quit (q)").upper()
        print("next card is: " + deck.next_card.get_card())
        if guess == "Q":
            break
        elif deck.last_card.amount > deck.next_card.amount and guess == "L":
            score = score + 1
            print("You guessed correct")
        elif deck.last_card.amount < deck.next_card.amount and guess == "H":
            score = score + 1
            print("You guessed correct")
        else:
            print("You guessed incorrect")
        total_guesses = total_guesses + 1
        deck.last_card = deck.next_card
        deck.get_next_card()
    print("Your score is: " + str(score) + " out of " + str(total_guesses))


higher_lower()
