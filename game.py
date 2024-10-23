import random as rd
import hangman
words = ["Physics", "Mathematics", "Chemistry", "Science", "Computer",
         "Urdu", "Punjabi", "English", "Islamiyat", "Education"]
word =  rd.choice(words)
print(word)
guessed_letters = []
correct_guess = ['_'] * len(word)
attempts = 7
index = 0
while True:

    print("Welcome to Hangman!!")


    while attempts > 0:

        print("\nCurrent Word: ", ' '.join(correct_guess))
        print(f"Attempts remaining: {attempts}")

        guess = input("Enter a letter: ").lower()


        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)


        if guess in word:
            print(f"Correct! The letter '{guess}' is in the word.")


            for i in range(len(word)):
                if word[i] == guess:
                    correct_guess[i] = guess
        else:

            print(f"Sorry! The letter '{guess}' is not in the word.")
            attempts -= 1
            
            print(hangman.stages[index])
            index += 1

        if '_' not in correct_guess:
            print(f"\nCongratulations! You've guessed the word '{word}'!")
           


    if attempts == 0:
        print(f"\nGame Over! The correct word was '{word}'.")


    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break
