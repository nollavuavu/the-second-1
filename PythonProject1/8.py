import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()
random.shuffle(key)

desired_text = input("Enter what you desire to encrypt: ")
undesired_text = ""

for letter in desired_text:
    index = chars.index(letter)
    undesired_text += key[index]
print(undesired_text)

undesired_text = input("Enter what you desire to encrypt: ")
desired_text = ""

for letter in undesired_text:
    index = key.index(letter)
    desired_text += chars[index]
print(desired_text)