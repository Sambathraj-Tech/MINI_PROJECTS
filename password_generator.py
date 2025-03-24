import string
import random
from random import shuffle
from string import digits

letters = int(input("How many letters Do you want ? :"))
Digits = int(input("How many Numbers Do you want ? :"))
Special = int(input("How many Special_characters Do you want ? :"))

characters = string.ascii_letters
numbers = string.digits
special_chars = string.punctuation

password = ""

for i in range(0,letters+1):
    char = random.choice(characters)
    password = password + char

for i in range(0,Digits+1):
    char = random.choice(numbers)
    password = password + char

for i in range(0,Special+1):
    char = random.choice(special_chars)
    password = password + char

print(password)

shuffled = "".join(random.sample(password,len(password)))

#.join makes the list into a single string with the use of empty string
#random.sample(str_name,len(str_name))

print(shuffled)