from random import randint
# singles = []
# doubles = []
# triples = []
# throw_outs = []
#
# # fill up the lists with the possibilities
# for num in range(1, 22):
#     if num == 21:
#         singles.append(25)
#         doubles.append(50)
#     else:
#         singles.append(int(num))
#         doubles.append(2*int(num))
#         triples.append(3*int(num))
#
#
# def multi_nested_loop(matched_num, arr1, arr2, arr3=[]):
#     matches = []
#     for num1 in arr1:
#         for num2 in arr2:
#             # only when three arrays are given
#             if len(arr3) != 0:
#                 for num3 in arr3:
#                     total = num1 + num2 + num3
#                     if matched_num == total:
#                         order = f"{num1}, {num2}, {num3}"
#                         matches.append(order)
#             else:
#                 total = num1 + num2
#                 if matched_num == total:
#                     order = f"{num1}, {num2}"
#                     matches.append(order)
#     return matches
#
#
# def possible_outs():
#     points_left = int(input("How much point are left? "))
#     darts_remaining = int(input("How many darts are left? "))
#     possibilities = []
#     if points_left in doubles:
#         possibilities.append(points_left)
#     if darts_remaining == 2:
#         if points_left < 71 and len(possibilities) == 0:
#             possibilities = multi_nested_loop(points_left, singles, doubles)
#         if points_left < 111 and len(possibilities) == 0:
#             possibilities = multi_nested_loop(points_left, triples, doubles)
#             possibilities2 = multi_nested_loop(points_left, doubles, doubles)
#             for number in possibilities2:
#                 possibilities.append(number)
#     elif darts_remaining == 3:
#         if points_left < 91 and len(possibilities) == 0:
#             possibilities = multi_nested_loop(points_left, singles, singles, doubles)
#         if points_left < 136 and len(possibilities) == 0:
#             possibilities = multi_nested_loop(points_left, singles, triples, doubles)
#     print(possibilities)
#
#
# possible_outs()


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
