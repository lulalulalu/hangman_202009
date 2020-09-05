__date__ = "09/2020"
__author__ == "lulu"
# # Write your code here
import random
import string
import sys

print("H A N G M A N")


# def menu():
#     player_choice = input("Type 'play' to play the game, 'exit' to quit: ")
#     return player_choice

flag = True

while flag:
    word_list = ['python', 'java', 'kotlin', 'javascript']
    chosen_word = random.choice(word_list)
    word_letters = set(chosen_word)
    used_letters = set()
    alphabet = set(string.ascii_lowercase)  # set lowercase
    lives = 8

    player_choice = input("Type 'play' to play the game, 'exit' to quit: ")
    if player_choice == "exit":
        sys.exit(0)
        flag = False
    else:
        while len(word_letters) > 0 and lives > 0:
            # letters used --- extra information
            # " ".join(["a", "b", "c"]) --> "a b c"
            # print("you have used these letters: ", " ".join(used_letters))
            try:
                print()
                # what current word is --> (w-rd)
                letter_list = [letter if letter in used_letters else "-" for letter in chosen_word]
                print("".join(letter_list))

                user_letter = input("Input a letter: ")

                if user_letter not in alphabet:
                    if len(user_letter) > 1 or len(user_letter) == 0:
                        print("You should input a single letter")
                    else:
                        print("It is not an ASCII lowercase letter")

                elif user_letter not in used_letters:
                    used_letters.add(user_letter)
                    if user_letter in word_letters:
                        word_letters.remove(user_letter)
                        if letter_list == chosen_word:
                            lives -= 1

                    else:
                        lives -= 1
                        print("No such letter in the word")

                elif user_letter in letter_list:
                    print("You already typed this letter")

                elif user_letter in used_letters:
                    print("You already typed this letter")
            except Exception:
                continue

        # gets here when len(word_letters) == 0 or when lives == 0
        if lives == 0:
            print("You are hanged!")
        else:
            print("You guessed the word!")
            print("You survived!")
    print()
    lives = 8
    # flag = False


# version - 3 (stage 7/8)
# print("H A N G M A N")
# # print("The game will be available soon.")
#
# word_list = ['python', 'java', 'kotlin', 'javascript']
# chosen_word = random.choice(word_list)
# word_letters = set(chosen_word)
# alphabet = set(string.ascii_lowercase)  # set lowercase
# # print(alphabet)
# used_letters = set()
# lives = 8
#
# while len(word_letters) > 0 and lives > 0:
#     # letters used --- extra information
#     # " ".join(["a", "b", "c"]) --> "a b c"
#     # print("you have used these letters: ", " ".join(used_letters))
#     print()
#     # what current word is --> (w-rd)
#     letter_list = [letter if letter in used_letters else "-" for letter in chosen_word]
#     print("".join(letter_list))
#
#     user_letter = input("Input a letter: ")
#
#     if user_letter not in alphabet:
#         if len(user_letter) > 1 or len(user_letter) == 0:
#             print("You should input a single letter")
#         else:
#             print("It is not an ASCII lowercase letter")
#
#     elif user_letter not in used_letters:
#         used_letters.add(user_letter)
#         if user_letter in word_letters:
#             word_letters.remove(user_letter)
#             if letter_list == chosen_word:
#                 lives -= 1
#
#         else:
#             lives -= 1
#             print("No such letter in the word")
#
#     elif user_letter in letter_list:
#         print("You already typed this letter")
#
#     elif user_letter in used_letters:
#         print("You already typed this letter")
#
#
# # gets here when len(word_letters) == 0 or when lives == 0
# if lives == 0:
#     print("You are hanged!")
# else:
#     print("You guessed the word!")
#     print("You survived!")


# version - 2 (stage 6/8)
# print("H A N G M A N")
# # print("The game will be available soon.")
#
# word_list = ['python', 'java', 'kotlin', 'javascript']
# chosen_word = random.choice(word_list)
# word_letters = set(chosen_word)
# alphabet = set(string.ascii_lowercase)  # set lowercase
# used_letters = set()
# lives = 8
#
# while len(word_letters) > 0 and lives > 0:
#     # letters used --- extra information
#     # " ".join(["a", "b", "c"]) --> "a b c"
#     # print("you have used these letters: ", " ".join(used_letters))
#     print()
#     # what current word is --> (w-rd)
#     letter_list = [letter if letter in used_letters else "-" for letter in chosen_word]
#     print("".join(letter_list))
#
#     user_letter = input("Input a letter: ")
#
#     if user_letter not in used_letters:
#         used_letters.add(user_letter)
#         if user_letter in word_letters:
#             word_letters.remove(user_letter)
#             if letter_list == chosen_word:
#                 lives -= 1
#
#         else:
#             lives -= 1
#             print("No such letter in the word")
#
#     elif user_letter in used_letters:
#         lives -= 1
#         if user_letter in chosen_word:
#             print("No improvements")
#         else:
#             print("No such letter in the word")
#
#
# # gets here when len(word_letters) == 0 or when lives == 0
# if lives == 0:
#     print("You are hanged!")
# else:
#     print("You guessed the word!")
#     print("You survived!")


# version -1
# word_letters = set(chosen_word)  # letters in the word
# display = "-" * len(chosen_word)

# guessed_letters = []  # what the user has guessed
#
#
# print("H A N G M A N")
# # word = input("Guess the word: > " + chosen_word[0:3] + "-" * (len(chosen_word) - 3))
# # print()
# # print(display)
# # guess = input("Input a letter: ")
#
# while len(chosen_word) > 0 and lives > 0 \
#         :
#     guessed_letters.append(guess)
#     # print(guessed_letters)
#     letter_list = [guess if guess in guessed_letters else "-" for guess in chosen_word]
#     print()
#     print(display)
#     guess = input("Input a letter: ")
#     if guess in chosen_word:
#         k = chosen_word.count(guess)
#         for _ in range(k):
#             # guessed_letters += guess
#             lives -= 1
#             index = chosen_word.find(guess)
#             display = display[:index] + guess + display[index + 1:]
#             print(display)
#
#     else:
#         print("No such letter in the word")
#         print()
#         print(display)
#         guess = input("Input a letter: ")
#         lives -= 1
#
#     if guess in guessed_letters and guessed_letters.count(guess) > 1:
#         lives -= 1
#         print("No improvements")
#         continue
#     elif guess not in guessed_letters and guessed_letters.count(guess) > 1:
#         lives -= 1
#         print("No improvements")
#         continue
#
# if guess == chosen_word:
#     print("You guessed the word!")
#     print("You survived!")
# else:
#     print("You are hanged!")
#
# # print("Thanks for playing!")
# # print("We'll see how well you did in the next stage")
