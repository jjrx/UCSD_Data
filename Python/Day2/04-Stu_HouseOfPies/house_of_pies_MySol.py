pies = ["Pecan", "Apple Crisp", "Bean", "Banoffee",  "Black Bun", "Blueberry", "Buko", "Burek",  "Tamale", "Steak"]

print("Welcome to the House of Pies! Here are our pies:")
print("---------------------------------------------------------------------")
for pie in pies:
    print("(" + str(pies.index(pie)+1) + ") " + pie) 

piesOrdered = []

anotherOrder = "yes"
while anotherOrder == "yes":  
    pieNum = int(input("Please enter the pie number you would like to order: "))
    print("Great! We'll have that " + pies[pieNum-1] + " pie right out for you.")
    piesOrdered.append(pies[pieNum-1])
    anotherOrder = input("Would you like to make another order? ")

print("You ordered " + str(len(piesOrdered)) + " pies: ")
for pie in pies:
    print(str(piesOrdered.count(pie)) + " " + pie)
