class Card:
	RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
	SUITS = ["c", "d", "h", "s"]

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def __str__(self):
		replay = self.rank + self.suit
		return replay

class Hand:
	def __init__(self):
		self.cards = []
	def __str__(self):
		if self.cards:
			replay = ""
			for card in self.cards:
				replay += str(card) + " "
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


if __name__ == '__main__':
	card1 = Card(rank = "A", suit = "c")
	card2 = Card(rank = "2", suit = "c")
	card3 = Card(rank = "3", suit = "c")
	card4 = Card(rank = "4", suit = "c")
	card5 = Card(rank = "5", suit = "c")
	print(card1)
	print("\nPrinting the rest of the objects individualy:")
	print(card2)
	print(card3)
	print(card4)
	print(card5)
	my_hand = Hand()
	print("\nPrinting my hand before I add any cards:")
	print(my_hand)
	my_hand.add(card1)
	my_hand.add(card2)
	my_hand.add(card3)
	my_hand.add(card4)
	my_hand.add(card5)
	print("\nPrinting my hand afeter adding 5 cards:")
	print(my_hand)

	your_hand = Hand()
	my_hand.give(card1, your_hand)
	my_hand.give(card2, your_hand)
	print("\nGave the first two cards form my hand to your hand.")
	print("Your hand:")
	print(your_hand)
	print("My hand:")
	print(my_hand)
	my_hand.clear()
	print("\nMy hand after clearing it:")
	print(my_hand)

