from random import randint
t=("Rock","Paper","Scissors ")
computer = t[randint(0,2)]
player = False
while player == False:
    print("Enter Your Opinion")
    player = input(t)
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lost",computer,"covers",player)
        else:
            print("You won!",player,"beats",computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lost",computer,"cut",player)
        else:
            print("Yay! You won",player,"beats",computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("Oops! You lost",computer, "covers",player)
        else:
            print("Yay! You Won",player,"cuts",computer)
    else:
        print("Please Enter Correct option")

