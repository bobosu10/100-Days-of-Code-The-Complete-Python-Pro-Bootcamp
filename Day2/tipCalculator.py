totalBill = float(input("Welcome to the tip calculator!\nWhat was the total bill? "))
tip = int(input("How much tip would you like to give? 10,12 or 15? "))
peopleCount = int(input("How many people to split the bill? "))

def billCalculator(totalBill, tip, peopleCount):
    if tip == 10:
        totalBill = (totalBill * 1.1)/peopleCount
    if tip == 12:
        totalBill = (totalBill * 1.12)/peopleCount
    if tip == 15:
        totalBill = (totalBill * 1.15)/peopleCount
    return round(totalBill, 2)

print(f"Each person should pay: {billCalculator(totalBill, tip, peopleCount)}")