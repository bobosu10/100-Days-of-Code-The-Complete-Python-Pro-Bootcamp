import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '?']

lettersCount = int(input("Welcome to the PyPassword Generator!\nHow many letters would you like in your password?"))
symbolsCount = int(input("How many symbols would you like in your password?"))
numbersCount = int(input("How many numbers would you like in your password?"))

possibleList = []

for i in range(numbersCount):
    possibleList.append(random.choice(numbers))
for j in range(symbolsCount):
    possibleList.append(random.choice(symbols))
for k in range(lettersCount):
    possibleList.append(random.choice(letters))

print(possibleList)
random.shuffle(possibleList)
print(possibleList)

password = ""

for char in possibleList:
    password += char
print(password)