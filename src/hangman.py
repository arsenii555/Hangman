import random

words = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape",
    "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "pear",
    "quince", "raspberry", "strawberry", "tangerine", "watermelon", "apricot",
    "blueberry", "cranberry", "dragonfruit", "guava", "kiwifruit", "lime",
    "mulberry", "pomegranate", "pineapple", "blackberry", "boysenberry",
    "coconut", "grapefruit", "papaya", "persimmon", "blackcurrant", "lychee",
    "cantaloupe", "cucumber", "tomato", "carrot", "zucchini", "potato",
    "broccoli", "cauliflower", "lettuce", "spinach", "kale", "radish", "beet",
    "turnip", "eggplant", "pepper", "asparagus", "corn", "onion", "garlic",
    "ginger", "basil", "oregano", "parsley", "thyme", "rosemary", "coriander",
    "cumin", "sage", "mint", "vanilla", "cinnamon", "nutmeg", "cloves",
    "paprika", "mustard", "turmeric", "cardamom", "cayenne", "peppermint",
    "lavender", "chocolate", "vanilla", "caramel", "hazelnut", "almond",
    "pecan", "cashew", "walnut", "macadamia", "pistachio", "toffee",
    "marshmallow", "caramel", "honey", "maple", "peanut"
]


def find_indexes(word: str) -> dict:
    """
    Finds the indexes of each letter in a word and return them as dictionaries.
    :param str word: The string in which to find letter indexes.

    :return: A dictionary letter_indexes (dict): dictionary where keys are
    letters from the input string, and values are lists of indexes at which
    these letters appear in the word.

    :rtype: dict

    :example:
    >>> find_indexes("hangman")
    {'h': [0], 'a': [1, 5], 'n': [2, 6], 'g': [3], 'm': [4]}
    """
    word = word.lower()
    letter_indexes = dict()
    for i in range(len(word)):
        curr_letter = word[i]
        if curr_letter not in letter_indexes:
            letter_indexes[curr_letter] = [i]
        else:
            letter_indexes[curr_letter].append(i)
    return letter_indexes


def get_random_word(word_list: list):
    """
    Selects a random word from a list of words.

    :param list word_list: A list of words from which to choose a random word.

    :return: A randomly selected word from the input list.
    :rtype: str

    :example:

    >>> word_list = ["apple", "banana", "cherry", "date", "fig"]
    >>> get_random_word(word_list)
    'banana'
    """
    if not word_list:
        raise ValueError("The input word list is empty.")

    return random.choice(word_list)


word = get_random_word(words)
length = len(word)
attempts = length * 2 // 3 + 1
current = ['_'] * length
closed = length
dict_of_indexes = find_indexes(word)
guessed_letters = set()
while attempts > 0:
    character = input(f"{''.join(current)} guess a character: ")
    if character in dict_of_indexes.keys():
        if character.lower() not in guessed_letters:
            for i in dict_of_indexes[character]:
                current[i] = word[i]
                closed -= 1
                guessed_letters.add(character.lower())
        else:
            print("You have already tried this letter")
    else:
        attempts -= 1
        print(f"Wrong. You have {attempts} more guesses")

    if closed == 0:
        print(f"{word} Congratulations! You won!")
        break
if attempts == 0:
    print(f"I am really sorry. You lose :(\nThe right answer was {word}")
