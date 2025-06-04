import random

#set
words = "apple","orange","banana","coconut","pineapple";
#dictionary{key:tuple}
hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" O ",
                  "   ",
                  "   "),
               2:("  O  ",
                  "  | ",
                  "   "),
               3:("  O ",
                  " /| ",
                  "   "),
               4:("  O ",
                  " /|\\ ",
                  "   "),
               5:("  O ",
                  " /|\\",
                  " /" ),
               6:("  O ",
                  " /|\\",
                  " / \\")}





def display_hangman(wrong_guess):
    print("****************")
    for line in hangman_art[wrong_guess]:
        print(line)
    print("*****************")

def display_hint(hint):
    print("  ".join(hint))

def display_answer(answer):
    print("  ".join(answer))


def main():
    answer = random.choice(words)
    hint=["_"]*len(answer)
    wrong_guess=0;
    guessed_letters= set() # empty set
    is_running = True


    while is_running:
        display_hangman(wrong_guess)
        display_hint(hint)
        guess = (input("Enter a letter: ").lower())

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input!")
            continue
        
        if guess in guessed_letters:
            print(f"Our guess is already guesses!")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guess+=1

        if not "_" in hint:
            display_hangman(wrong_guess)
            display_answer(answer)
            print("YOU WIN!")
            is_running=False
        elif wrong_guess >= len(hangman_art)-1:
            display_hangman(wrong_guess)
            display_answer(answer)
            print("YOU LOSE!")
            is_running=False



if __name__ == "__main__":
    main()