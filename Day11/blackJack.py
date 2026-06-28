import art
import random

cards = {
    2: [2], 3: [3], 4: [4], 5: [5], 6: [6], 7: [7],
    8: [8], 9: [9], 10: [10], "A": [1, 11], "Q": [10], "K": [10], "J": [10],
}


def calcular_score(mao):
    total = sum(max(cards[carta]) for carta in mao)
    quantidade_ases = mao.count("A")
    while total > 21 and quantidade_ases > 0:
        total -= 10
        quantidade_ases -= 1
    return total


choise = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if choise == "y":
    print(art.logo)
    playerCard = [random.choice(list(cards.keys())), random.choice(list(cards.keys()))]
    computerCard = [random.choice(list(cards.keys()))]

    userTotal = calcular_score(playerCard)
    computerTotal = calcular_score(computerCard)

    print(f"Your cards: {playerCard}, current score: {userTotal}")
    print(f"Computer's first card: {computerCard}")

elif choise == "n":
    print(art.lose)
    choise = ""
else:
    print("Invalid input")
    choise = ""

while choise == "y":
    choise = input("'y' to get another card, type 'n' to pass: ")

    if choise == "y":
        playerCard.append(random.choice(list(cards.keys())))
        userTotal = calcular_score(playerCard)
        if computerTotal > 17:
            computerCard.append(random.choice(list(cards.keys())))
            computerTotal = calcular_score(computerCard)


        if userTotal > 21:
            print(f"Your cards: {playerCard}, Score: {userTotal}\nYou lose! (Bust)")
            break

        print(f"\nYour cards: {playerCard}, current score: {userTotal}")
        print(f"Computer's cards: {computerCard}")

    elif choise == "n":
        while computerTotal < 17:
            computerCard.append(random.choice(list(cards.keys())))
            computerTotal = calcular_score(computerCard)
            print(f"Computer draws a card. New hand: {computerCard} (Score: {computerTotal})")

        print(f"\n=== Final Hands ===")
        print(f"Your cards: {playerCard}, final score: {userTotal}")
        print(f"Computer cards: {computerCard}, final score: {computerTotal}\n")

        if computerTotal > 21:
            print("You win! Computer busted.")
        elif userTotal > computerTotal:
            print("You win! You have a higher score.")
        elif userTotal < computerTotal:
            print("You lose! Computer has a higher score.")
        else:
            print("It's a draw (Push)!")

        break