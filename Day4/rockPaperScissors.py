import random

#friends = ["alice", "david", "bob", "charlie","robert"]

#escolha = random.choice(friends)

#print(f"O escolhido da vez foi {escolha}")

#fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
#vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

#print(dirty_dozen[1][1])

userChoise = int(input("******************************************************************\nWelcome to the rock paper scissors game !\nWhat do you choose?Type 0 for Rock, 1 for Paper or 2 for Scissors.\nCHOISE: "))

rockPaperScissors = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""" , """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

pcChoice = random.randint(0,2)

pcHand = rockPaperScissors[pcChoice]
userHand = rockPaperScissors[userChoise]

if userHand == pcHand:
    print(f"******************************************************************\nDRAW!!!{userHand}\n{pcHand}\nDRAW!!!\n******************************************************************")
elif (userChoise == 0 and pcChoice == 2) or (userChoise == 1 and pcChoice == 0) or (userChoise == 2 and pcChoice == 1):
    print(f"******************************************************************\nUSER WIN!!!{userHand}\n{pcHand}\nUSER WIN!!!\n******************************************************************")
elif (userChoise == 0 and pcChoice == 1) or (userChoise == 1 and pcChoice == 2) or (userChoise == 2 and pcChoice == 0):
    print(f"******************************************************************\nPC WIN!!!{userHand}\n{pcHand}\nPC WIN!!!\n******************************************************************")



