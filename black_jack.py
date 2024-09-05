import random
import os
from blackjack_art import logo
def ran():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
def add_card(user_card,computer_card):
 os.system("cls")
 print(logo)
 user_card.append(ran())
 print(f"your card: {user_card}, current score: {sum(user_card)}")
 print(f"computer's first card: {computer_card[0]}")
 if sum(computer_card)<17:
  computer_card.append(ran())
 if 11 in user_card and sum(user_card) > 21:
  user_card.remove(11)
  user_card.append(1)
 if sum(user_card)>21:
  return
 if sum(user_card)==21:
  return
 keep_going=input("type y to get onether card and n to not: ")
 if keep_going=="n":
  return
 add_card(user_card,computer_card)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    user_card=[ran(),ran()]
    computer_card=[ran(),ran()]
    print(logo)
    print(f"your card: {user_card}, current score: {sum(user_card)}")
    print(f"computer's first card: {computer_card[0]}")
    keep_going=input("type y to get onether card and n to not: ")
    if keep_going=="y":
        add_card(user_card,computer_card)
    print(f"your card: {user_card}, current score: {sum(user_card)}")
    print(f"computer's first card: {computer_card}, current score: {sum(computer_card)}")
    if sum(user_card)>21 :
        print("You went over.you lose")
    elif sum(user_card)>sum(computer_card) or sum(computer_card)>21:
        print("you win")
    elif sum(user_card)==sum(computer_card):
        print("draw")
    else:
        print("you lose")
    