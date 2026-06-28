import art

print(art.logo)

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mult(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operations = {"+":add,"-":sub,"*":mult,"/":div}

userOn = True
firstNumberExist = False

while userOn:
    if firstNumberExist == False:
        n1 = int(input("what is your first number:\n"))
        choice = input("What do you want to do(+,-,*,/):\n")
        n2 = int(input("what is your seconde number:\n"))
    else:
        choice = input("What do you want to do(+,-,*,/):\n")
        n2 = int(input("what is your seconde number:\n"))

    if choice in operations:
        result = operations[choice](n1,n2)
        print(f"\nThe result is: {result}")
    elif continar == "quit":
        userOn = False
    else:
        print("\nInvalid choice. Try again.\n")

    continar = input("Would you like to continue with the previus result(y/n)?\n")

    if continar == "n":
        firstNumberExist = False
        print("result delete as first number.")

    elif continar == "y":
        n1 = result
        firstNumberExist = True
    elif continar == "quit":
        userOn = False
    else:
        print("Invalid choice. Try again.\n")