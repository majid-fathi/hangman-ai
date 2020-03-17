import random
import string
import hangman_lib

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


# actually load the dictionary of words and point to it with
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word = words_dict[random.randrange(0, len(words_dict))]
    return word


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES
secret_word = 'claptrap'
letters_guessed = []
correctly_guessed = []  # The letters that were correctly guessed whit their index
possible_words = []


def check_word(word):
    # len(word) = len(correctly_guessed)
    result = True
    for index in range(len(correctly_guessed)):
        if not correctly_guessed[index] == '-':
            if not correctly_guessed[index] == word[index]:
                result = False

    return result


def word_guessed():
    """
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    """
    word = ''
    for a in correctly_guessed:
        word += a

    if word == secret_word:
        return True
    else:
        return False


def print_guessed():
    """
    Prints out the characters you have guessed in the secret word so far
    """
    print("guessed word", end=": ")
    for a in correctly_guessed:
        print(a, end=' ')
    print()


def random_letter():
    """
    generate random letter to guess word
    """
    global possible_words
    if len(letters_guessed) == 0:  # first turn
        for word in words_dict:
            if len(word) == len(secret_word):
                possible_words.append(word)

    else:  # other turns
        temp = []
        for word in possible_words:
            if check_word(word):
                temp.append(word)
        possible_words = temp

    possible_letters = []
    for word in possible_words:
        for letter in word:
            if letter not in possible_letters and letter not in letters_guessed:
                possible_letters.append(letter)

    print("possible letters: " + str(possible_letters))
    letter = random.choice(possible_letters)

    return letter


def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    global correctly_guessed
    global possible_words
    letters_guessed = []
    correctly_guessed = []
    possible_words = []
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word.
    secret_word = get_word()
    print("secret word: " + secret_word)
    for index in range(len(secret_word)):
        correctly_guessed.append('-')

    turn = 1
    while mistakes_made < MAX_GUESSES and not word_guessed():
        print("\nturn " + str(turn) + "  *******************************")
        print_guessed()
        print("mistakes = " + str(mistakes_made))
        letter = random_letter()
        print("possible words = " + str(len(possible_words)))
        print("guessed letter: " + letter, end=" ")
        letters_guessed.append(letter)

        contain = False
        for index in range(len(secret_word)):
            if secret_word[index] == letter:
                correctly_guessed[index] = letter
                contain = True

        if contain:
            print("✓")
        else:
            print("X")
            mistakes_made += 1

        hangman_lib.print_hangman_image(mistakes_made)
        turn += 1

    if word_guessed():
        print("\n\n*GG WP word guessed*")
        return True
    else:
        print("\n\nfailed")
        return False


failed = 0
success = 0
for i in range(100):
    if play_hangman():
        success += 1
    else:
        failed += 1

print(success / failed + success)
