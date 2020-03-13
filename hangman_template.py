# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *

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
    print('Enter play_hangman() to play a game of hangman!')
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
    word = words_dict[randrange(0, len(words_dict))]
    return word


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap'
letters_guessed = []


def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######


def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######


def random_letter():
    '''
    generate random letter to guess word
    '''

    ####### YOUR CODE HERE ######


def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word.
    # secret_word  = get_word()

    ####### YOUR CODE HERE ######
    return None
