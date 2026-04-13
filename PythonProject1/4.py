import random

options =("R","P","S")
computer = random.choice(options)
win_times = 0
while True:
    computer = random.choice(options)
    player = input("Rock, paper, scissors! What you choose?(R, P, S): ").upper()
    if player == computer:
        replay =input("It's a draw! You wanna play again?(Y or N): ").upper()
        if replay == "N":
            print("Aight")
            break
        else:
            print("Aight brodie, continue")
    elif player == "P" and computer =="S" or player =="S" and computer =="R" or player=="R"and computer =="P":
        replay=input("Yo you lose asl! Wanna play again?(Y or N): ").upper()
        if replay == "N":
            print("Aight")
            break
        else:
            print("Aight brodie, continue")
    elif player =="P"and computer=="R" or player =="S" and computer =="P" or player =="R" and computer =="S":
        win_times +=1
        replay =input(f"Yo congrats, you won {win_times} times! Want a rematch?(Y or N): ")
        if replay == "N":
            print("Aight")
            break
        else:
            print("Aight brodie, continue")

