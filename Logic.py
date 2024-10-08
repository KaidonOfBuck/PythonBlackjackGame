# Game logic planning and stuff

# I need a player and a dealer and a each needs a hand of cards
# player options are to hit or stand

# Face cards are value 10
# Ace is 1 if 21 - playerhand < 11
# soft 17 = dealers hand is 17 with an Ace = 11 (must hit)
# blackjack is 21 in first two cards (Ace plus a 10/face card)

"""

1. create deck of cards
2. shuffle deck
3. deal cards to each "player" (player, dealer, player, dealer's face down card)
4. check if either player or dealer has a blackjack
5. player can choose to hit or stand.
6. if player hits, deal card and calculate the total, or check if they bust
7. if player doesn't bust, get 21 or stand, player can again choose to hit or stand
8. once player stands, dealer gets dealt cards until he must stand, or bust
9. once dealer is finished winner is calculated and win/lose screen is displayed
10. new game screen is then displayed with options to play again or exit

"""

from Player import *
from Dealer import *
from Card import *
from CardSprite import *
from Deck import *
from TableSprite import *
from LauncherButton import *
from WelcomeSprite import *

def calculateAceValue(playerHandTotal):
    if 21 - playerHandTotal < 11:
        # Ace value should be 1
        return 1
    elif 21 - playerHandTotal >= 11:
        # Ace value should be 11
        return 11
        
# Game loop

# Create Deck
deck = Deck(True)

# print(deck.getData()[12].getName() + ' Value: ' + str(deck.getData()[12].getValue()))

# Shuffle Deck
deck.shuffleDeck()

#create player and dealer
player = Player()
dealer = Dealer()

# Deal two cards to each player and dealer in order
# And calculate the HandValue after each card is dealt
for i in range(2):
    player.addCardToHand(deck.dealCard())
    
    if player.getHand()[i].getName() == 'Ace':
        player.getHand()[i].setValue(calculateAceValue(player.getHandValue()))
    
    player.setHandValue(player.getHand()[i].getValue() + player.getHandValue())

    dealer.addCardToHand(deck.dealCard())

    if dealer.getHand()[i].getName() == 'Ace':
        dealer.getHand()[i].setValue(calculateAceValue(dealer.getHandValue()))

    dealer.setHandValue(dealer.getHand()[i].getValue() + dealer.getHandValue())

print('Player Hand Value: ' + str(player.getHandValue()), end = ', ')
print('Cards:', end = (' '))
for card in player.getHand():
    print(card.getName(), end = ', ')
print('\n')

print('Dealer Hand Value: ' + str(dealer.getHandValue()), end = ', ')
print('Cards:', end = (' '))
for card in dealer.getHand():
    print(card.getName(), end = ', ')
print('\n')

if dealer.getHandValue() == 21:
    print('Blackjack! The Dealer Won!')
    # This is where you end the game loop and display the new game screen
elif player.getHandValue() == 21:
    print('Blackjack! You Won!')
    # This is where you end the game loop and display the new game screen
else:
    # No one has blackjack, game continues
    pass

playerHits = True

while playerHits:

    print("type \"hit\" or \"stand\" to choose.")
    choice = input('Hit or Stand: ')

    if choice == 'hit' or choice == 'Hit':
        playerHits = True
    elif choice == 'stand' or choice == 'Stand':
        playerHits = False
    else:
        print('Input not recognized, please try again.')

    player.addCardToHand(deck.dealCard())
    
    if player.getHand()[-1].getName() == 'Ace':
        player.getHand()[-1].setValue(calculateAceValue(player.getHandValue()))
    
    player.setHandValue(player.getHand()[-1].getValue() + player.getHandValue())

dealerHits = True

while dealerHits:
    if dealer.getHandValue() >= 17:
        dealerHits = False
    else:
        dealer.addCardToHand(deck.dealCard())

        if dealer.getHand()[i].getName() == 'Ace':
            dealer.getHand()[i].setValue(calculateAceValue(dealer.getHandValue()))

        dealer.setHandValue(dealer.getHand()[i].getValue() + dealer.getHandValue())


print('Player Hand Value: ' + str(player.getHandValue()), end = ', ')
print('Cards:', end = (' '))
for card in player.getHand():
    print(card.getName(), end = ', ')
print('\n')

print('Dealer Hand Value: ' + str(dealer.getHandValue()), end = ', ')
print('Cards:', end = (' '))
for card in dealer.getHand():
    print(card.getName(), end = ', ')
print('\n')

playerValue = player.getHandValue()
dealerValue = dealer.getHandValue()

if playerValue > 21:
    print('Player Busted! You Lost!')
elif dealerValue > 21:
    print('Dealer Busted! You Won!')
elif playerValue > dealerValue:
        print('You Won!')
else:
    print('You Lost!')
    
