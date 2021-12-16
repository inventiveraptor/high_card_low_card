#!/usr/bin/env python3

import random
import time

player_score = 0
computer_score = 0

print("This game is played against a computer opponent where cards are selected randomly from two decks of traditional playing cards.")
time.sleep(2)
print("Are you ready to play? (Y/N)")
cont = input()
while cont[0] == "y" or cont[0] == "Y":
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    computer_suit = random.choice(suits)
    player_suit = random.choice(suits)
    computer_card = random.choice(cards)
    player_card = random.choice(cards)

    if player_card > computer_card:
        win = 1
    elif player_card == computer_card: 
        win = 2
    else:
        win = 3

    #convert player card: 
    if player_card == 2:
        player_card = "Two"
    elif player_card == 3:
        player_card = "Three"
    elif player_card == 4: 
        player_card = "Four"
    elif player_card == 5:
        player_card = "Five"
    elif player_card == 6:
        player_card = "Six"
    elif player_card == 7:
        player_card = "Seven"
    elif player_card == 8:
        player_card = "Eight"
    elif player_card == 9:
        player_card = "Nine"
    elif player_card == 10:
        player_card = "Ten"
    elif player_card == 11:
        player_card = "Jack"
    elif player_card == 12:
        player_card = "Queen"
    elif player_card == 13:
        player_card = "King"
    elif player_card == 14:
        player_card = "Ace"

    #convert computer card value 
    if computer_card == 2:
        computer_card = "Two of "
    elif computer_card == 3:
        computer_card = "Three of "
    elif computer_card == 4: 
        computer_card = "Four of "
    elif computer_card == 5:
        computer_card = "Five of "
    elif computer_card == 6:
        computer_card = "Six of "
    elif computer_card == 7:
        computer_card = "Seven of "
    elif computer_card == 8:
        computer_card = "Eight of "
    elif computer_card == 9:
        computer_card = "Nine of "
    elif computer_card == 10:
        computer_card = "Ten of "
    elif computer_card == 11:
        computer_card = "Jack of "
    elif computer_card == 12:
        computer_card = "Queen of "
    elif computer_card == 13:
        computer_card = "King of "
    elif computer_card == 14:
        computer_card = "Ace of "

    print(f"Computer drew the {computer_card} {computer_suit}...")
    time.sleep(2)
    print("Get ready to draw in\n3.....")
    time.sleep(1)
    print("2.....")
    time.sleep(1)
    print("1.....")
    time.sleep(1)
    print("Draw!!!")
    time.sleep(0.5)
    print(f"You drew the {player_card} {player_suit}!")
    time.sleep(2)
    if win == 1: 
        print("You win!")
        player_score += 1
    elif win == 3:
        print("Computer wins...")
        computer_score += 1
    else:
        print("Tie!!!")
    time.sleep(2)
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")
    print("Play again? (Y/N)")
    cont = input()
    
print("")    
print("")
print("Final score:")
print(f"Player: {player_score}\nComputer: {computer_score}")