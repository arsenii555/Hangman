import pytest

from src.hangman import get_random_word

word_list = [
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


def test_random_word_selection():
    # Perform random word selection multiple times
    for _ in range(50):
        random_word = get_random_word(word_list)
        assert random_word in word_list


def test_empty_list():
    # Test if an empty word list raises a ValueError
    with pytest.raises(ValueError):
        get_random_word([])
