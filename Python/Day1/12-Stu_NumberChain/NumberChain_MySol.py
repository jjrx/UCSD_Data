wants_to_play = 'y'

while wants_to_play == 'y':
    nums = int(input("How  many numbers? "))

    for x in range(nums):
        print(x)
    
    wants_to_play = input("Would you like to continue? y/n? ")
