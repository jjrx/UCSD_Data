candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

candyCart = []

for candy in candyList:
    print("[" + str(candyList.index(candy)) + "] " + candy)

allowance = int(input("What is the allowance? "))

for x in range(allowance):
    userChoice = int(input("Which candy would you like? "))
    candyCart.append(candyList[userChoice])

for candy in candyCart:
    print("You bought " + candy)
