#card class
class Card:
	def __init__(self, rank, suit):
			self.rank = rank
			self.suit = suit

#hand class, aka player or dealer
class Hand:
	def __init__(self, name, cards, value, size):
		self.name = name
		self.cards = cards
		self.value = value
		self.size = size

#initialize deck
def build_deck():
	rank = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
	suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
	for value in rank:
		for suit in suits:
			new_card = Card(value, suit)
			deck.append(new_card)
			#print(f"{new_card.rank} of {new_card.suit}")
	return deck

#deal initial hand
def deal_hand(player):
	while (player.size < 2):
		deal_card(player)

#get card's int value
def card_value(card, hand_value):
	card_value = card.rank
	if (card.rank == "A"):
		if (hand_value <= 10):
			card_value = 11
		else:
			card_value = 1
	elif ((card.rank == "J") or (card.rank == "Q") or (card.rank == "K")):
		card_value = 10
	
	return card_value

#deal a single card if card is in deck, otherwise do nothing
def deal_card(player):
	index = random.randint(0,51) #NOTE: RANDOM IS NOT EXCLUSIVE FOR END - (0,52) will create 'OutOfBounds' Exception
	#print(f"index =  {index}")
	card = deck[index]
	if (valDeck[index] == 1):
		player.cards.append(card)
		valDeck[index] = 0;
		player.value = player.value + card_value(card, player.value)
		player.size += 1

#print player hand
def show_hand(player):
	print(f"{player.name.title()} has: ", end="")
	for card in player.cards:
		print(f"{card.rank} of {card.suit}", end=", ")
	print(f"Total Hand Value = {player.value}")

#special print for dealer hand when one card hidden
def show_dealer(dealer):
	print(f"Dealer showing: {dealer.cards[0].rank} of {dealer.cards[0].suit}")

#############################MAIN###########################################
import random
#varables
chips=100
valDeck =[]
for card in range(0,52):
	valDeck.append(1)
deck = []
build_deck()
player = Hand("player", [], 0, 0)
dealer = Hand("dealer", [], 0, 0)
deal_hand(player)
deal_hand(dealer)
show_hand(player)
show_dealer(dealer)

if(dealer.value < 17):
		deal_card(dealer)
		show_hand(dealer)
		pStatus=dealer.value



#outer while loop: checks if player has chips to play, or choses to quit game - exit condition(s): chips = 0, player doesnt continue
	#if player has 21, check dealer hand - unless dealer has 21 then player wins
	#OPTIONAL: if player not 21, check dealer hand for faceup 'A' @ dealer.cards[0], and ask for insurance
	#players inner while loop - exit condition(s): player doesn't hit, player busts
	#dealers inner while loop - exit condition(s): dealer busts, dealer doesn't hit (dealer stands on 17(?))
	#check hand totals and decide winner, allocate winnings/losses
 	#if chips > 0, ask player to play again
