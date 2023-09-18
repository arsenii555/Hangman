import pytest

from src.functions import get_random_word

words = []
with open('./tests/words.txt', 'r') as fd:
    for string in fd:
        words.append(string[:-1])
    fd.close()


def test_random_word_selection():
    # Perform random word selection multiple times
    for _ in range(50):
        random_word = get_random_word(words)
        assert random_word in words


def test_empty_list():
    # Test if an empty word list raises a ValueError
    with pytest.raises(ValueError):
        get_random_word([])
