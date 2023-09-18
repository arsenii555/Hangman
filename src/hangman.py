from functions import find_indexes, get_random_word

words = []
with open('words.txt', 'r') as fd:
    for string in fd:
        words.append(string[:-1])
    fd.close()
word = get_random_word(words)
length = len(word)
attempts = length * 2 // 3 + 1
current = ['_' for _ in range(length)]
closed = length
dict_of_indexes = find_indexes(word)
guessed_letters = set()
print('Start guessing...')  # noqa: WPS421 not secure issue
while attempts > 0:
    current_word = ''.join(current)
    character = input(f'{current_word} guess a character: ')  # noqa: WPS421, WPS305,  not secure issue
    if character in dict_of_indexes.keys():
        if character.lower() not in guessed_letters:
            for ind in dict_of_indexes[character]:
                current[ind] = word[ind]
                closed -= 1
                guessed_letters.add(character.lower())
        else:
            print('You have already tried this letter')  # noqa: WPS421 not secure issue
    else:
        attempts -= 1
        print(f'Wrong. You have {attempts} more guesses')  # noqa: WPS421, WPS305 not secure issue

    if closed == 0:
        print(f'{word} Congratulations! You won!')  # noqa: WPS421, WPS305 not secure issue
        break
if attempts == 0:
    print(f'I am really sorry. You lose :(\nThe right answer was {word}')  # noqa: WPS421, WPS305 not secure issue
