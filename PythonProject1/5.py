import random

dice_arts = {1:"⚀",
        2:"⚁",
        3:"⚂",
        4:"⚃",
        5:"⚄",
        6:"⚅"}
dice =[]
total =0
num_of_dice=int(input("How many times yo?: "))

for counter in range(num_of_dice):
    dice.append(random.randint(1,6))
    for counter2 in dice_arts.get(dice[counter]):
        print(f"{dice[counter]}: {counter2}")
for counter in dice:
    total+=counter
print(total)