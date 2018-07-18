candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

candyCart = []

for candy in candyList:
    print("[" + str(candyList.index(candy)) + "] " + candy)

wantCandy = "y"
while wantCandy == 'y':
    userChoice = int(input("Which candy would you like? "))
    candyCart.append(candyList[userChoice])
    wantCandy = input("Do you still want candy? y/n? ")

for candy in candyCart:
    print("You bought " + candy)
