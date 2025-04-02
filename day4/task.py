from new import choice


"""
PAUSE 1 - Heads or Tails
Create a coin flip program using what you have learnt about randomisation in Python.
It should randomly print "Heads" or "Tails" everytime it is run.
"""
a="Head"
b="Tail"
rad=choice(a,b)
if rad == "Head":
    print("You are head!")
else:
    print("You are tail!")

"""
List

You can create a simple collection of ordered items using a Python list. e.g.

fruits = ["Cherry", "Apple", "Pear"]
Accessing Items in Lists
You can provide the name of the list then a square bracket and then the item index that you want. e.g.

fruits[0]

Negative Indices
You can access items in the list counting from the end of the list by using negative whole numbers. e.g.
fruits = ["Cherry", "Apple", "Pear"]
fruits[-1] #this will be "Pear"
"""
fruits = ["Cherry", "Apple", "Pear"]
print(fruits[-1])

"""
Modifying Items
You can use the same syntax to get hold of items in a List to modify it.
"""
fruits = ["Cherry", "Apple", "Pear"]
fruits[0]="bnana"
print(fruits)

"""
Adding items

you can add items to the end of a list using append()
function
"""
fruits.append("Cherry")
print(fruits)
print(fruits.sort(reverse=False))
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

states_of_america_sort = sorted(states_of_america,reverse=False)
print(states_of_america_sort)

states_of_america.sort(reverse=True)
coun=states_of_america.count("Delaware")
print(coun)
states_of_america_sort.pop()
print(states_of_america_sort)
""" from collections import deque
fruit = deque(["apple", "banana", "cherry"])
print(fruit.popleft()) """

""" Merge to List """

vegan=["Gemose","obst",""]

combined_list=[fruits,vegan]
print(combined_list)

"""
Rock Paper Scissor
"""

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

# Get user's choice
choice_type = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

# Validate input
if choice_type not in ["0", "1", "2"]:
    print("Invalid choice! Please enter 0, 1, or 2.")
else:
    player_choice = int(choice_type)
    computer_choice = random.randint(0, 2)

    print("\nYou chose:")
    print(choices[player_choice])

    print("\nComputer chose:")
    print(choices[computer_choice])

    # Determine the winner
    if player_choice == computer_choice:
        print("It's a draw!")
    elif (player_choice == 0 and computer_choice == 2) or \
         (player_choice == 1 and computer_choice == 0) or \
         (player_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("Computer wins!")

