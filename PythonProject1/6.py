def main():
    balance =0
    is_running = True

    def show_balance():
        print(f"Your balance is ${balance:2.f}")
    def deposit():
        money_deposit = float(input("How much you wanna deposit twin?:$"))
        if money_deposit<0:
            print("Nigga stop trolling")
            return 0
        else:
            print(f"You have deposited ${money_deposit:2.f}")
            return  money_deposit
    def withdraw():
        money_withdraw = float(input("How much you gon take, homie?:$"))
        if money_withdraw > balance:
            print("You cant do that shi")
            return 0
        else:
            print(f"You have withdrawn ${money_withdraw:2.f}")
            return  money_withdraw

    while is_running:
        print("************************")
        print("Banking fast and furious")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")
        print("************************")
        try:
            choice = int(input("Enter what you wish to achieve(1-4): "))
            match choice:
                case 1:
                    show_balance()
                case 2:
                    balance +=deposit()
                case 3:
                    balance -=withdraw()
                case 4:
                    is_running =False
                case _:
                    print("Nigga sybau")
        except ValueError:
            print("Don't mess with me!")

if __name__=="__main__":
    main()