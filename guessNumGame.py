import random

computer = random.randint(1,100)
guessTime = 0
player = int(input("Guess number from 1-100: "))

for i in range(100):
    guessTime+=1
    if player==computer:
        print("You get the right number by ",guessTime,"times")
        break
    elif player > computer:
        print("The number is too high")
        player = int(input("Guess number from 1-100: "))
    else:    
        print("The number is too low")
        player = int(input("Guess number from 1-100: "))


    
