def average(numlist):
    sum = 0
    for num in numlist:
        sum += num
    return sum/len(numlist)

print(average([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(average([0, 1, 2]))
print(average([80, 34, 234, 3, 3985, 235]))
