import random
import unicodedata

# Define constants for card suits and rank.
SUIT = [
    "Spades",
    "Hearts",
    "Diamonds",
    "Clubs"
]
RANK = [
    "Ace",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King"
]

class Card:
    # Blank card by default
    def __init__(self):
        self.suit = SUIT[0]
        self.rank = RANK[0]
        self.face = unicodedata.lookup("Playing Card Back")
        self.isDiscarded = False
        self.isPlayed = False
        
    def setCard(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.face = unicodedata.lookup("Playing Card " + rank + " of " + suit)

    def draw(self):
        pass

    def discard(self):
        self.isDiscarded = True
    
    def print(self):
        print(self.face + " " + self.rank + " of " + self.suit)

# Initialize the deck to a standard 52 card deck.
def initializeDeck(deck):
    for i in range(52):
        deck.append(Card())

    # Variable for current card being updated, Loops update the entire deck.
    card = 0
    for i in SUIT:
        for j in RANK:
            deck[card].setCard(i, j)
            card += 1

# Explain how each poker hand works.
def explain():
    print(
"""
Poker is played with a standard 52 card deck.
Each hand is played with 5 different cards.

Cards consisnt of four different suits:

🂡 Spades, 🂱 Hearts, 🃁 Diamonds, 🃑 Clubs.

Cards are ranked as follows: (from worst to best)

🂢 Two, 🂣 Three, 🂤 Four, 🂥 Five, 🂦 Six, 🂧 Seven, 
🂨 Eight, 🂩 Nine, 🂪 Ten, 🂫 Jack, 🂭 Quuen, 🂮 King, 🂡 Ace.

There are 9 types of hand you can have in poker;
they are: (from best to worst)

Straight Flush: (Five cards of the same suit played in ascending order.)
🂱 Ace of Hearts
🂾 King of Hearts    NOTE: This specific hand is also known as a royal flush.
🂽 Queen of Hearts         it is the best hand playable in poker.
🂻 Jack of Hearts
🂺 Ten of Hearts

Four of a Kind: (Four cards of the same rank)
🂡 Ace of Spades
🂱 Ace of Hearts
🃁 Ace of Diamonds
🃑 Ace of Clubs
🃆 Six of Diamonds

Full House: (A pair of cards with matching rank
            plus three cards of another matching rank)
🃂 Two of Diamonds
🃒 Two of Clubs
🂢 Two of Spades
🂻 Jack of Hearts
🃋 Jack of Diamonds

Flush: (Five cards of the same suit)
🃕 Five of Clubs
🃓 Three of Clubs
🃝 Queen of Clubs
🃚 Ten of Clubs
🃒 Two of Clubs

Straight: (Five cards of ascending order)
🃃 Three of Diamonds
🃔 Four of Clubs     NOTE: An 🂡 Ace can either be played
🂥 Five of Spades          before a 🂢 Two, or after a 🂮 King.
🂦 Six of Spades
🂷 Seven of Hearts

Three of a Kind: (Three cards of matching rank)
🂮 King of Spades
🃞 King of Clubs
🃎 King of Diamonds
🂽 Queen of Hearts
🃒 Two of Clubs

Two Pair: (Two pairs of cards with matching ranks)
🂢 Two of Spades
🃒 Two of Clubs
🂵 Five of Hearts
🃕 Five of Clubs
🂩 Nine of Spades

Pair: (A pair of cards with matching ranks)
🃘 Eight of Clubs
🂨 Eight of Spades
🃞 King of Clubs
🂷 Seven of Hearts
🂢 Two of Spades

High Card: (No cards of matching rank or suit.
            The highest ranked card will be scored.)
🂡 Ace of Spades
🂳 Three of Hearts
🃅 Five of Diamonds
🂪 Ten of Spades
🂾 King of Hearts
"""
        )

# Declare deck as a list of 52 cards.
deck = []
initializeDeck(deck)

# TEST: Shuffle and print deck.
for i in deck:
    i.print()

print("\n\n")
random.shuffle(deck)
for i in deck:
    i.print()
