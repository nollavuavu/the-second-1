import random

words = ("decision","conquer","nigga","nigger","destiny")

hangman_art ={0:("   ",
                 "   ",
                 "   "),
              1:(" o ",
                 "   ",
                 "   "),
              2:(" o ",
                 " | ",
                 "   "),
              3:(" o ",
                 "/| ",
                 "   "),
              4:(" o ",
                 "/|\\",
                 "   "),
              5:(" o ",
                 "/|\\",
                 "/  "),
              6:(" o ",
                 "/|\\",
                 "/ \\")}


def hangman_display(wrong_guesses):
    global is_running
    is_running=True
    if wrong_guesses==6:
        rematch = input("Nigga you lost, wanna retry?(Y or N): ").upper()
        if rematch == "Y":
            main()
        elif rematch == "N":
            is_running =False
        else:
            print("Nigga istg, stop playing")
            is_running=False
    for counter in hangman_art[wrong_guesses]:
        print(counter)

def hint_display(hint):
    print(" ".join(hint))

def answer_display(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"]*len(answer)
    wrong_guesses=0
    guessed_letter =set()
    is_running = True

    while is_running:
        hangman_display(wrong_guesses)
        hint_display(hint)
        guess = input("What's the letter: ").lower()

        if not len(guess)==1 or not guess.isalpha():
            print("Nigga stop playing")
            continue

        if guess in guessed_letter:
            print("Shi already been done g")
            continue

        guessed_letter.add(guess)

        if guess in answer:
            for index in range(len(answer)):
                if answer[index]==guess:
                    hint[index]=guess
        else:
            wrong_guesses+=1

        if "_" not in hint:
            rematch = input("Nigga congrats, want a rematch?(Y or N): ")
            if rematch == "Y":
                main()
            elif rematch == "N":
                is_running = False
            else:
                print("Nigga istg, stop playing")
                is_running=False

if __name__=="__main__":
    main()