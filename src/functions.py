import random


def find_indexes(word: str) -> dict:
    """
    Find the indexes of each letter in a word and return them as dictionaries.

    :param word: The string in which to find letter indexes.
    :return: A dictionary letter_indexes (dict): dictionary where keys are
            letters from the input string, and values are lists of indexes at which
            these letters appear in the word.
    :rtype: dict

    :example:
        >>> find_indexes('hangman')
        {'h': [0], 'a': [1, 5], 'n': [2, 6], 'g': [3], 'm': [4]}
    """
    word = word.lower()
    letter_indexes = {}
    for index, curr_letter in enumerate(word):
        if curr_letter not in letter_indexes:
            letter_indexes[curr_letter] = [index]
        else:
            letter_indexes[curr_letter].append(index)
    return letter_indexes


def get_random_word(word_list: list):
    """
    Select a random word from a list of words.

    :param word_list: A list of words from which to choose a random word.
    :return: A randomly selected word from the input list.
    :rtype: str

    :raises ValueError: If the input word list is empty.

    :example:
        >>> word_list = ['apple', 'banana', 'cherry', 'date', 'fig']
        >>> get_random_word(word_list)
        'banana'
    """
    if not word_list:
        raise ValueError('The input word list is empty.')
    return random.choice(word_list)
