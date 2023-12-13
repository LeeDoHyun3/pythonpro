class Card:
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        replay = self.rank + self.suit
        return replay

class Positionable_Card(Card):
    def __init__(self, rank, suit, face_up = False):
        super().__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            reply = super().__str__()
        else:
            reply = "XX"
        return reply

    def flip(self):
        self.is_face_up = not self.is_face_up



class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            replay = ""
            for card in self.cards:
                replay += str(card) + "\t"        
        else:
            replay = "<empty>"
        return replay

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
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
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Out of cards!")

class Player(Hand):
    def __init__(self, name):
        self.name = name
        self.cards = []
        
class Dealer(Hand):
    def c_print(self):
        print("")
        
if __name__ == "__main__" :
    print("\t\tWelcome to Blackjack!\n")
    playerNum = int(input("How many player? (2-5): "))
    playerList = ['player1', 'player2', 'player3', 'player4', 'player5']
    hands = []
    dealer = Dealer()
    hands.append(dealer)
    for i in range(playerNum):
        name = input("Enter plaer name: ")
        playerList[i] = Player(name)
        hands.append(playerList[i])
        
    print(hands)
    deck = Deck()
    deck.populate()
    deck.shuffle()
    deck.deal(hands, 2)
    for hand in hands:
        print(hand)

