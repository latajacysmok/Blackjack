class Card(object):
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand(object):
    """ Ręka gracza  """
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<pusta>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

card1 = Card(rank = "A", suit = "c")
print("Wyświtlam obiekt kart (klasy Card): ")
print(card1)

card2 = Card(rank = "2", suit = "c")
card3 = Card(rank = "7", suit = "d")
card4 = Card(rank = "Q", suit = "h")
card5 = Card(rank = "J", suit = "s")
card6 = Card(rank = "A", suit = "c")

print("Wyświtlam resztę kart: ")
print(card2)
print(card3)
print(card4)
print(card5)
print(card6)

my_hand = Hand()
print("\nWyświetlam zawartość mojej ręki przed dodaniem jakichkolwiek kart:")
print(my_hand)

my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
my_hand.add(card6)
print("\nWyświetlam zawartość mojej ręki po dodaniu 6 kart:")
print(my_hand)

your_hand = Hand()
my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)
print("\nPrzekazuje pierwsze dwie karty z mojej ręki do Twojej.")
print("Twoja ręka: ")
print(your_hand)
print("Moja ręka: ")
print(my_hand)

my_hand.clear()
print("Moja ręka po usunięciu z niej kart: ")
print(my_hand)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")