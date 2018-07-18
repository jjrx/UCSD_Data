import random
player_choice = input("(r)ock, (p)aper, or (s)cissors? ")
comp_options = ['r', 'p', 's']
comp_choice = random.choice(comp_options)

if (player_choice == 'r' and comp_choice == 'p'):
    print("You chose rock, the computer chose paper.")
    print("You lose.")
elif (player_choice == 'r' and comp_choice == 's'):
    print("You chose rock, the computer chose scissors.")
    print("You win!")
elif (player_choice == 'r' and comp_choice == 'r'):
    print("You chose rock, the computer chose rock.")
    print("You tied.")
elif (player_choice == 'p' and comp_choice == 's'):
    print("You chose rock, the computer chose scissors.")
    print("You win!")
elif (player_choice == 'p' and comp_choice == 'p'):
    print("You chose paper, the computer chose paper.")
    print("You tied.")
elif (player_choice == 'p' and comp_choice == 's'):
    print("You chose paper, the computer chose scissors.")
    print("You lose.")
elif (player_choice == 'p' and comp_choice == 'r'):
    print("You chose paper, the computer chose rock.")
    print("You win!")
elif (player_choice == 's' and comp_choice == 'p'):
    print("You chose scissors, the computer chose paper.")
    print("You win!")
elif (player_choice == 's' and comp_choice == 'r'):
    print("You chose scissors, the computer chose rock.")
    print("You lose.")
