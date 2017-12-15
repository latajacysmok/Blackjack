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

class Deck(Hand):
    """ Talia kart do gry"""
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self. cards[0]
                    self.give(top_card, hand)
                else:
                    print("Nie mogę dalej rozdawać. Zabrakło kart!")

class Positionable_Card(Card):
    """ Karta, która może być odkryta lub zakryta. """
    def __init__(self, rank, suit, face_up = True):
        super(Positionable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up

class Unprintable_Card(Card):
    """ Karta, której ranga i kolor nie są ujawnione przy jej wyświetleniu. """
    def __str__(self):
        return "<utajniona>"




card1 = Card("A", "c")
card2 = Unprintable_Card("A", "h")
card3 = Positionable_Card("A", "s")

print("Wyświetlenie obiektu klasy Card: ")
print(card1)

print("\nWyświetlanie obiektu klasy Unprintable_Card: ")
print(card2)

print("\nWyświetlanie obiektu klasy positionable_Card: ")
print(card3)

print("Odwracanie stanu obiektu klasy positionable_Card (odkrycie-zakrycie karty).")
card3.flip()

print("\nWyświetlanie obiektu klasy positionable_Card: ")
print(card3)

# deck1 = Deck()
# print("Utworzyłem nową talię.")
# print("Talia: ")
# print(deck1)
#
# deck1.populate()
#
# print("\nDodałem do talii komplet kart.")
# print("Talia: ")
# print(deck1)
#
# deck1.shuffle()
#
# print("\nPotasowałem talię kart.")
# print("Talia: ")
# print(deck1)
#
# my_hand = Hand()
# your_hand = Hand()
# hands=[my_hand, your_hand]
#
# deck1.deal(hands, per_hand = 5)
#
# print("\nRozdałem Tobie i sobie po 5 kart.")
# print("Moja ręka: ")
# print(my_hand )
# print("\nTwoja ręka.")
# print(your_hand)
# print("\nTalia: ")
# print(deck1)
#
# deck1.clear()
# print("\nUsunąłem zawartość talii.")
# print("Talia: ", deck1)

# card1 = Card(rank = "A", suit = "c")
# print("Wyświtlam obiekt kart (klasy Card): ")
# print(card1)
#
# card2 = Card(rank = "2", suit = "c")
# card3 = Card(rank = "7", suit = "d")
# card4 = Card(rank = "Q", suit = "h")
# card5 = Card(rank = "J", suit = "s")
# card6 = Card(rank = "A", suit = "c")
#
# print("Wyświtlam resztę kart: ")
# print(card2)
# print(card3)
# print(card4)
# print(card5)
# print(card6)
#
# my_hand = Hand()
# print("\nWyświetlam zawartość mojej ręki przed dodaniem jakichkolwiek kart:")
# print(my_hand)
#
# my_hand.add(card1)
# my_hand.add(card2)
# my_hand.add(card3)
# my_hand.add(card4)
# my_hand.add(card5)
# my_hand.add(card6)
# print("\nWyświetlam zawartość mojej ręki po dodaniu 6 kart:")
# print(my_hand)
#
# your_hand = Hand()
# my_hand.give(card1, your_hand)
# my_hand.give(card2, your_hand)
# print("\nPrzekazuje pierwsze dwie karty z mojej ręki do Twojej.")
# print("Twoja ręka: ")
# print(your_hand)
# print("Moja ręka: ")
# print(my_hand)
#
# my_hand.clear()
# print("Moja ręka po usunięciu z niej kart: ")
# print(my_hand)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")