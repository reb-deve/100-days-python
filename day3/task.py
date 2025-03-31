"""
Your goal today is to build a "Chose your own adventure game".
Using what you have learnt in the lessons today you will be building a very simple version of this type of text game.
"""

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choose_f = input("Choose a side: Left (L) or Right (R)? ").strip().lower()

if choose_f == "r":
    print("Fall into a hole.\nGame Over.")
elif choose_f == "l":
    choose_s = input("Choose: Swim (S) or Wait (W)? ").strip().lower()
    if choose_s == "s":
        print("Attacked by trout.\nGame Over.")
    elif choose_s == "w":
        choose_d = input("Which door? Blue (B), Red (R), or Yellow (Y)? ").strip().lower()
        if choose_d == "r":
            print("Burned by fire.\nGame Over.")
        elif choose_d == "b":
            print("Eaten by beasts.\nGame Over.")
        elif choose_d == "y":
            print("You win!")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")
