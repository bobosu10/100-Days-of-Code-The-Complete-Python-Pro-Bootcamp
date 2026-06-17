import art

print(art.logo+"\nWelcome to the secret auction program")

def theBig(persons):
    biggestName =""
    biggestValue = 0
    for key in persons:
        if persons[key] > biggestValue:
            biggestValue = persons[key]
            biggestName = key
    print(f"The winner is {biggestName} and his/her value is {biggestValue}")


persons = {}

otherBidders = True
while otherBidders:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    persons[name] = bid
    continuar = input("Are there any other bidders? Type 'yes or 'no'. ")
    if continuar == "no":
        theBig(persons)
        otherBidders = False
    else:
        print("\n"*10)


#maior_pessoa = max(persons, key=persons.get)

#print(f"{maior_pessoa}: {persons[maior_pessoa]}")
