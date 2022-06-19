
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# Importing necessary modules 
import random
from art import logo
from replit import clear

# Run the game
def playBlackjack():
  clear()
  print(logo)
  # Create necessary variables
  game_over = False
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  player_hand = []
  computer_hand = []
  player_hand.append(random.choice(cards))
  player_hand.append(random.choice(cards))
  computer_hand.append(random.choice(cards))
  computer_hand.append(random.choice(cards))

  # Determine if game continues after each turn
  while not game_over:
    player_score = calculate_score(player_hand)
    computer_score = calculate_score(computer_hand)
    if player_score == 0:
      print(f'\tYour cards: {player_hand}, current score: 21')
    else:
      print(f'\tYour cards: {player_hand}, current score: {player_score}')
    print(f"\tComputer's first card: {computer_hand[0]}")
    # Check if score is over 21
    if computer_score == 0 or player_score == 0 or player_score > 21:
      # End the game
      game_over = True
    # Ask for the next play
    else:
      deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if deal == 'y':
        player_hand.append(random.choice(cards))
      else:
        game_over = True

  # Determine final score
  while computer_score < 16 and computer_score != 0:
    computer_hand.append(random.choice(cards))
    computer_score = calculate_score(computer_hand)
  if player_score == 0:
    print(f'\tYour final hand: {player_hand}, final score: 21')
  else:
    print(f'\tYour final hand: {player_hand}, final score: {player_score}')
  if computer_score == 0:
    print(f"\tComputer's final hand: {computer_hand}, final score: 21")
  else: 
    print(f"\tComputer's final hand: {computer_hand}, final score: {computer_score}")
  print(compare(player_score, computer_score))

# Determine the score
def calculate_score(hand):
  score = sum(hand)
  if len(hand) == 2 and score == 21:
    return 0
  if 11 in hand and sum(hand) > 21:
      hand.remove(11)
      hand.append(1)
  return sum(hand)

# Determine who wins
def compare(player_score, computer_score):
  if computer_score == 0:
    return "Lose, opponent has Blackjack"
  elif player_score == 0:
    return "Win with a Blackjack"
  elif player_score > 21:
    return "You went over. You lose"
  elif computer_score > 21:
    return "Opponent went over. You win"
  elif player_score == computer_score:
    return "Draw"
  elif player_score > computer_score:
    return "You win"
  else:
    return "You lose"

# Ask if want to play again
while(input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y'):
  playBlackjack()


