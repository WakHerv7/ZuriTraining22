import random
from random import choice
# t = ["Rock", "Paper", "Scissors"]
rps = ["R", "P", "S"]

def get_choice(choice):
    if choice == "R":
        return "Rock"
    elif choice == "S":
        return "Scissors"
    elif choice == "P":
        return "Paper"

#set player to False
player = False

while player == False:
    
    player = input("Pick between 'R' (rock), 'P' (paper), 'S' (scissors) ? ")
    computer = random.choice(rps)

    if player in ('R', 'P', 'S'):

        print("Player(", get_choice(player), ") : CPU(", get_choice(computer),")")

        if player == computer:
            print("Tie!")
            player = False

        elif player == "R":
            if computer == "P":                
                print("You lose!")
            else:
                print("You win!")

        elif player == "P":
            if computer == "S":
                print("You lose!")
            else:
                print("You win!")

        elif player == "S":
            if computer == "R":
                print("You lose...")
            else:
                print("You win!")        
        
    else:
        print("Invalid Input. Try again.")
        player = False