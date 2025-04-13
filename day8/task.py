""" alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()



# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(plain_text, shift_amount):
    result = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % len(alphabet)
            result += alphabet[new_position]
        else:
            result += letter
    print(f"Encrypted message: {result}")

def decrypt(cipher_text, shift_amount):
	result = ""
	for letter in cipher_text:
		if letter in alphabet:
			position = alphabet.index(letter)
			new_position = (position - shift_amount) % len(alphabet)
			result += alphabet[new_position]
		else:
			result += letter
	print(f"Decrypted message: {result}")
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
if direction == "encode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text, shift)
elif direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decrypt(text, shift)
else:
    print(f"Wrong direction entered: {direction}")
# TODO-5: Create a function called 'decrypt()' that takes 'cipher_text' and 'shift_amount' as inputs.
# TODO-6: Inside the 'decrypt()' function, shift the letters back to their original positions.

 """

 #alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
def caesar(original_text, shift_amount, encode_or_decode):
    alphabet = [chr(i)for i in range(97,123)]
    result = ""
    if encode_or_decode == "decode":
        shift_amount*=-1
    for char in original_text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index=(index+shift_amount) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += char
    print(f"Here is the {encode_or_decode} result: {result}")

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)







