from random import randint
choice = ["rock","paper","scissor"]



win = 0
lose = 0
draw = 0
for i in range(5):
    computer = choice[randint(0,2)]
    player = input("Enter rock, paper, scissor: ")
    while player != "rock" and player != "paper" and player !="scissor":
        print("Your input is wrong, enter again")
        player = input("Enter rock, paper, scissor: ")
    print("Your choice:",player)
    print("Computer choice:",computer)

    if player == computer:
        print("Draw")
        draw+=1
    elif player == "rock" and computer == "paper":
        print("Computer wins")
        lose += 1
    elif player == "rock" and computer == "scissor":
        print("You win")
        win += 1
    elif player == "paper" and computer == "rock":
        print("you win")
        win += 1
    elif player =="paper" and computer == "scissor":
        print("You lose")
        lose += 1
    elif player == "scissor" and computer == "rock":
        print("You lose")
        lose += 1
    elif player == "scissor" and computer == "paper":
        print("You win")
        win += 1
    print("----------------------------------------------")

if win > lose:
    print("Final result-",win,":",lose,", You win")
elif win < lose:
    print("Final result-",win,":",lose,", You lose")
else:
    print("Final result-",win,":",lose,", Draw")

