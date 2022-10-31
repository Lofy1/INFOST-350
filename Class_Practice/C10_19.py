import random

#varables
initCard = 1
valDeck =[]
for card in range(0,52):
	valDeck.append(1)

#order of cards in the array is Spades A to K then Clubs, Diamonds, Hearts
# rank = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# suit = ["Spades","Clubs","Diamonds","Hearts"]

deck = ["Spades A", "Spades 2", "Spades 3", "Spades 4", "Spades 5", "Spades 6", "Spades 7", "Spades 8", "Spades 9", "Spades 10", "Spades J", "Spades Q", "Spades K","Clubs A", "Clubs 2", "Clubs 3", "Clubs 4", "Clubs 5", "Clubs 6", "Clubs 7", "Clubs 8", "Clubs 9", "Clubs 10", "Clubs J", "Clubs Q", "Clubs K","Diamonds A", "Diamonds 2", "Diamonds 3", "Diamonds 4", "Diamonds 5", "Diamonds 6", "Diamonds 7", "Diamonds 8", "Diamonds 9", "Diamonds 10", "Diamonds J", "Diamonds Q", "Diamonds K","Hearts A", "Hearts 2", "Hearts 3", "Hearts 4", "Hearts 5", "Hearts 6", "Hearts 7", "Hearts 8", "Hearts 9", "Hearts 10", "Hearts J", "Hearts Q", "Hearts K"]

#this gets removed where done
index = random.randint(0,52)


dealer = []
player = []

class getCard():
  print("hi")
  if (valDeck[index] == 0):
    index = random.randint(0,52)
  else:
    print("Your card is", deck[index])
    valDeck[card] = 0

getCard()

