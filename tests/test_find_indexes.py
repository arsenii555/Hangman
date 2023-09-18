from typing import Dict

from src.functions import find_indexes


def test_find_indexes_example():
    res = find_indexes('programming')
    expected = {
        'p': [0],
        'r': [1, 4],
        'o': [2],
        'g': [3, 10],
        'a': [5],
        'm': [6, 7],
        'i': [8],
        'n': [9],
    }
    assert res == expected


def test_find_indexes_empty_string():
    res = find_indexes('')
    expected: Dict[str, list] = {}
    assert res == expected


def test_find_indexes_single_letter():
    res = find_indexes('a')
    expected = {'a': [0]}
    assert res == expected


def test_find_indexes_repeating_letters():
    res = find_indexes('banana')
    expected = {
        'b': [0],
        'a': [1, 3, 5],
        'n': [2, 4],
    }
    assert res == expected


def test_find_indexes_case_insensitive():
    res = find_indexes('arRival')
    expected = {
        'a': [0, 5],
        'r': [1, 2],
        'i': [3],
        'v': [4],
        'l': [6],
    }
    assert res == expected


def test_find_indexes_mixed_case():
    res = find_indexes('enCyClopEdia')
    expected = {
        'e': [0, 8],
        'n': [1],
        'c': [2, 4],
        'y': [3],
        'l': [5],
        'o': [6],
        'p': [7],
        'd': [9],
        'i': [10],
        'a': [11],
    }
    assert res == expected
