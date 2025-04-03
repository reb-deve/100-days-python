"""
For loop
"""

"""
Find High score and Low score
"""

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# print(max(student_scores))
# print(min(student_scores))

"""
Max
"""

max_score=student_scores[0]
for j in student_scores:
    if j > max_score:
        max_score = j
print("Max high score is " , max_score)

""" Min """

min_score =student_scores[0]
for i in student_scores:
    if i < min_score:
        min_score =i
print("Low score is " , min_score)


""" Password Generator Project """

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


choice_letter = random.choices(letters, k=nr_letters)
choice_number = random.choices(numbers, k=nr_numbers)
choice_symbol = random.choices(symbols,k=nr_symbols)

mix_pass_letter = choice_letter+choice_number+choice_symbol

print("Original selection:", mix_pass_letter)
for i in range(1,5):
    random.shuffle(mix_pass_letter)
    print("Password generated:", mix_pass_letter)
print("Shuffled",mix_pass_letter)
# Build the password string using a for loop
password = ""
for char in mix_pass_letter:
    password += char
print(f"Your generated password is: {password}")


