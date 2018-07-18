wants_to_play = 'y'
starting_num = 0

while wants_to_play == 'y':
    
    nums = int(input("How  many numbers? "))
    
    for x in range(starting_num,starting_num + nums):
        print(x)
    
    starting_num = starting_num + nums
    wants_to_play = input("Would you like to continue? y/n? ")
