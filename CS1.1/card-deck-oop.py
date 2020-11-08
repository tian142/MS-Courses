class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def show(self):
        print(f"{self.value} of {self.suit}")


class Deck:
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        for suit in suits:
            for val in range(1, 14):
                self.cards.append(Card(suit, val))

    def show_cards(self):
        for card in self.cards:
            card.show()


deck = Deck()
deck.show_cards()
