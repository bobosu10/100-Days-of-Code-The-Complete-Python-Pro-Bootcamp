import art
import gameData
import random

def higher_lower():
    score = 0
    Aperson = random.choice(gameData.data)
    Bperson = random.choice(gameData.data)
    print(f"{art.logo}\nCompare A: {Aperson["name"]}, a {Aperson['description']}, from {Aperson['country']}.\n{art.vs}\nAgainst B: {Bperson["name"]}, a {Bperson['description']}, from {Bperson['country']}.")

    while True:

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        if guess in ("A", "B"):
            if Aperson["follower_count"] > Bperson["follower_count"]:
                correct = "A"
            else:
                correct = "B"
            if guess == correct:
                score += 1
                Aperson = Bperson
                Bperson = random.choice(gameData.data)
                while Aperson == Bperson:
                    Bperson = random.choice(gameData.data)
                print(
                    f"{art.logo}\nYou're right! Current score: {score}.\nCompare A: {Aperson["name"]}, a {Aperson['description']}, from {Aperson['country']}.\n{art.vs}\nAgainst B: {Bperson["name"]}, a {Bperson['description']}, from {Bperson['country']}.")
            else:
                print(f"Sorry, that's wrong. Final score: {score}.")
                break
        else:
            print("Sorry, you have to type 'A' or 'B': ")




higher_lower()
