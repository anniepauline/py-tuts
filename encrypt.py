import string
import random

chars = " " + string.punctuation + string.digits + string.ascii_letters
print(chars)

chars = list(chars)
print(chars)
key = chars.copy()

random.shuffle(key)
print(f"key: {key}")
print(f"chars: {chars}")

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cypher_text =""

for letter in plain_text:
    index = chars.index(letter)
    cypher_text+=(key[index])

print(cypher_text)

print(f"Original messgae: {plain_text}")
print(f"Encrypted message: {cypher_text}")


#DECRYPT
cipher_text = input("Enter your cipher test: ")
plain_text=""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Cipher messgae: {cypher_text}")
print(f"Plain message: {plain_text}")
