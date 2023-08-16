# word = 'o n o m a t o p e e'
"""
If first and last letter appear inside the word, it should be visible
word  = "o _ o _ _ _ o _ e e"
7 attempts
"""

from nltk.corpus import words
from colorama import Fore, Style

import random

# Get the list of English words
english_words = words.words()
while True:
    answer = input(Fore.GREEN + "\n> Do you want to play another round ? (Y/N): " + Style.RESET_ALL)
    if answer.lower() == 'n':
        break
    elif answer.lower() == 'y':
        # Generate a random word
        # Hide the inside letters
        random_word = random.choice(english_words).lower()

        word_to_be_guessed = random_word.lower()
        word = list(word_to_be_guessed)

        for index, letter in enumerate(word):
            if word[0] != letter and word[-1] != letter:
                word[index] = '_'

        word_to_be_printed = ' '.join(word)
        print(Fore.BLUE + f"Word to be guessed is: {word_to_be_printed}" + Style.RESET_ALL)

        """
         The user should enter only 1 character => len(string) > 1
         not digit => string.isdigit()
         not space 
        """
        tried_letters_or_words = set()
        number_of_attempts = 0
        has_won = False
        gave_up = False

        while number_of_attempts < 7:
            if has_won:
                break

            if gave_up:
                break
            while True:
                if number_of_attempts == 6:
                    print(Fore.YELLOW + f"You have only one more attempt left! Choose wisely! :)" + Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + f"You have {7 - number_of_attempts} attempts left" + Style.RESET_ALL)

                print("> Enter the command:\n\t1.Choose a letter\n\t2.Give the word\n\t3.Give up")
                print(Fore.LIGHTBLUE_EX + "!! If you want to cancel a command press '#' !!" + Style.RESET_ALL)
                if len(list(tried_letters_or_words)) > 0:
                    print(
                        Fore.BLUE + f'-> Tried letters and/or words are: {",".join(tried_letters_or_words)}'
                        + Style.RESET_ALL)
                command = input(Fore.LIGHTYELLOW_EX + "\n> Command " + Style.RESET_ALL)
                if command == '1':
                    letter_to_try = input("> Add a letter: ").lower()
                    if letter_to_try == '#':
                        break

                    while letter_to_try.isalpha() is False or len(letter_to_try) > 1 or letter_to_try in ["", " "]:
                        if letter_to_try.isalpha() is False:
                            print(Fore.LIGHTMAGENTA_EX + "Please enter a letter." + Style.RESET_ALL)
                        if len(letter_to_try) > 1:
                            print(
                                Fore.LIGHTMAGENTA_EX + "You have entered more characters. Please enter a letter"
                                + Style.RESET_ALL)
                        if letter_to_try == ["", " "]:
                            print(
                                Fore.LIGHTMAGENTA_EX + "You have entered a space. Please enter a letter."
                                + Style.RESET_ALL)
                        letter_to_try = input("> Add a letter: ").lower()

                    if letter_to_try not in word_to_be_guessed:
                        number_of_attempts += 1
                        tried_letters_or_words.add(letter_to_try)
                    elif letter_to_try in word_to_be_guessed and (word_to_be_guessed[0] != letter_to_try and
                                                                  word_to_be_guessed[-1] != letter_to_try):
                        for index, value in enumerate(word_to_be_guessed):
                            if value == letter_to_try:
                                word[index] = letter_to_try

                    if number_of_attempts == 7:
                        print(Fore.RED + "You lost! :(\nThe initial word was ")
                        print(Fore.CYAN + f"\t{' '.join(word_to_be_guessed)}")
                        break
                    elif '_' not in word:
                        print(Fore.GREEN + "Congratulations! You won!! :)\nThe word is" + Style.RESET_ALL)
                        print(Fore.CYAN + f"\t{' '.join(word_to_be_guessed)}" + Style.RESET_ALL)
                        has_won = True
                        break

                elif command == '2':
                    word_to_guess = input("\n> Give the word: ")
                    if word_to_guess == '#':
                        break
                    if word_to_guess.lower() == word_to_be_guessed.lower():
                        print(Fore.GREEN + "Congratulations! You won!! :)\nThe word is" + Style.RESET_ALL)
                        print(Fore.CYAN + f"\t{' '.join(word_to_be_guessed)}" + Style.RESET_ALL)
                        has_won = True
                        break
                    else:
                        number_of_attempts += 1
                        tried_letters_or_words.add(word_to_be_guessed)
                        if number_of_attempts == 7:
                            print(Fore.RED + "You lost! :(\nThe initial word was ")
                            print(Fore.CYAN + f"\t{' '.join(word_to_guess)}")
                            break

                elif command == '3':
                    print(Fore.CYAN + f"\tThe word was: {' '.join(word_to_be_guessed)}" + Style.RESET_ALL)
                    gave_up = True
                    break
                else:
                    print(Fore.RED + "Please enter a valid command!" + Style.RESET_ALL)

                word_to_be_printed = ' '.join(word)
                print(Fore.BLUE + word_to_be_printed + Style.RESET_ALL)

    else:
        print(Fore.RED + "Please enter a valid answer!\n" + Style.RESET_ALL)
