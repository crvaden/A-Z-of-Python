

# List Comprehensions
# playing cards

card_color = ['red', 'black', 'red', 'red', 'black', 'black', 'black', 'red', 'red', 'black']
card_suit = ['hearts', 'spades', 'hearts', 'diamonds', 'clubs', 'clubs', 'spades', 'hearts', 'diamonds', 'spades']
card_value = ['2', '5', '7', 'J', 'A', '3', '6', 'K', 'A', '4']

hand = [x for x in zip(card_color, card_suit, card_value)]

print(hand)

for card in hand:
    print(card[2], 'of', card[1], 'is', card[0])