# word = 'o n o m a t o p e e'
"""
If first and last letter appear inside the word, it should be visible
word  = "o _ o _ _ _ o _ e e"
7 attempts
"""

import random

from nltk.corpus import words
from colorama import Fore, Style


# If we want to use a predefined list of words for hangman game
# from now on we use as hangman_list_of_words
# from hangman_words import words_to_be_guessed as hangman_list_of_words
# print(random.choice(hangman_list_of_words))


def go_through_word(given_word: str, symbol_to_replace: str, hidden_word: list) -> list:
    """
    :param given_word: word to be guessed
    :param symbol_to_replace: the symbol used to replace
    :param hidden_word: the modified hidden word after each character insertion
    :return: modified word
    """
    for index, letter in enumerate(given_word):
        if symbol_to_replace == '_' and given_word[0] != letter and given_word[-1] != letter:
            hidden_word[index] = symbol_to_replace
        elif given_word[0] != letter and given_word[-1] != letter and letter == symbol_to_replace:
            hidden_word[index] = symbol_to_replace
    return hidden_word


def display_info(character_to_be_checked):
    if character_to_be_checked.isalpha() is False:
        print(Fore.LIGHTMAGENTA_EX + "Please enter a letter." + Style.RESET_ALL)
    if len(character_to_be_checked) > 1:
        print(
            Fore.LIGHTMAGENTA_EX + "You have entered more characters. Please enter a letter"
            + Style.RESET_ALL)
    if character_to_be_checked == ["", " "]:
        print(
            Fore.LIGHTMAGENTA_EX + "You have entered a space. Please enter a letter."
            + Style.RESET_ALL)


def display_no_of_attempts_and_return_game_result(remained_attempts: int, word_to_be_guessed: list, word: list,
                                                  has_won: bool = False) -> bool:
    if remained_attempts == 7:
        print(Fore.RED + "You lost! :(\nThe initial word was ")
        print(Fore.CYAN + f"\t{' '.join(word_to_be_guessed)}")
        return True
    elif '_' not in word:
        display_congratulations_message(word_to_be_guessed, has_won)
        return True
    elif remained_attempts == 6:
        print(Fore.YELLOW + f"You have only one more attempt left! Choose wisely! :)" + Style.RESET_ALL)
    elif (remained_attempts := 7 - remained_attempts) and remained_attempts > 0:
        print(Fore.YELLOW + f"You have {remained_attempts} attempts left" + Style.RESET_ALL)
    return False


def display_congratulations_message(word_to_be_guessed: list, has_won: bool = False):
    print(Fore.GREEN + "Congratulations! You won!! :)\nThe word is" + Style.RESET_ALL)
    print(Fore.CYAN + f"\t{' '.join(word_to_be_guessed)}" + Style.RESET_ALL)
    has_won = True


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

        # Use a word from the predefined list of words
        # random_word = random.choice(hangman_list_of_words)

        word_to_be_guessed = random_word.lower()
        word = list(word_to_be_guessed)

        word = go_through_word(word_to_be_guessed, '_', word)
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
                        display_info(letter_to_try)
                        letter_to_try = input("> Add a letter: ").lower()

                    if letter_to_try not in word_to_be_guessed:
                        number_of_attempts += 1
                        tried_letters_or_words.add(letter_to_try)
                    elif letter_to_try in word_to_be_guessed and (word_to_be_guessed[0] != letter_to_try and
                                                                  word_to_be_guessed[-1] != letter_to_try):
                        word = go_through_word(word_to_be_guessed, letter_to_try, word)

                    if display_no_of_attempts_and_return_game_result(number_of_attempts, word_to_be_guessed, word,
                                                                     has_won) or has_won:
                        break

                elif command == '2':
                    word_to_guess = input("> Give the word: ")
                    if word_to_guess == '#':
                        break
                    if word_to_guess.lower() == word_to_be_guessed.lower():
                        display_congratulations_message(word_to_be_guessed, has_won)
                        break
                    else:c
                        number_of_attempts += 1
                        tried_letters_or_words.add(word_to_guess)
                        if display_no_of_attempts_and_return_game_result(number_of_attempts, word_to_be_guessed, word,
                                                                         has_won) or has_won:
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
