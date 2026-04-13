import random


def spin_row():
    symbols = ["🧑","👨🏻","🧑🏼","👨🏾","🧑🏿"]
    result =[]
    for symbol in range(3):
        result.append(random.choice(symbols))
    return result

def print_row(row):
    print(" | ".join(row))

def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=="🧑":
            return bet*5
        if row[0]=="👨🏻":
            return bet*4
        if row[0]=="🧑🏼":
            return bet*3
        if row[0]=="👨🏾":
            return bet*2
        if row[0]=="🧑🏿":
            return bet*1.75
    elif row[0]==row[1]or row[0]== row[2] or row[1]==row[2]:
        if row[0]=="🧑":
            return bet*1.5
        if row[0]=="👨🏻":
            return bet*1.4
        if row[0]=="🧑🏼":
            return bet*1.3
        if row[0]=="👨🏾":
            return bet*1.2
        if row[0]=="🧑🏿":
            return bet*1.1
    else:
        return 0

def main():
    balance =100.0

    print("************************")
    print("Slot Machine:🧑👨🏻🧑🏼👨🏾🧑🏿")
    print("************************")

    while balance >0 and not balance==0:
        print(f"Current balance is ${balance:.2f}")

        try:
            bet = float(input("How much you wanna bet?: "))
        except ValueError:
            print("Don't play with me, lil homies")
            continue
        if bet >balance:
            print("You can't do that, can you?")
            continue
        elif bet<0:
            print("istg")
            continue
        if bet<= balance:
            balance -=bet

        row = spin_row()
        print_row(row)

        payout= get_payout(row,bet)
        print(f"Ay, you got {payout:.2f}, g")
        balance +=payout


if __name__=="__main__":
    main()