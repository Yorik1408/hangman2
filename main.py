import random
from words import words


def get_valid_word(s: str) -> bool:
    return ' ' in s or '-' in s


def hangman_game():
    """ Hangman game"""
    print("Упс, ты попал на виселицу, но ничего, в нашем государстве действует правило, "
          "угадай слово которое мы тебе загадаем или будешь болтаться на дереве!")
    secret = random.choice(words)
    guesses = "aeiouy"
    turns = 6
    while turns > 0:
        missed = 0
        for letter in secret:
            if letter in guesses:
                print(letter, end='')
            else:
                print('_', end='')
                missed += 1
        if missed == 0:
            print('\nНа этот раз победа за тобой, не попадайся больше на глаза нашему палачу')
            break
        guess = input('\nНазови букву или умри: ')
        guesses += guess
        if guess not in secret:
            turns -= 1
            print('\nТы ошибся!')
            print('\n', 'Осталось попыток: ', turns)
            if turns < 6:
                print('\n  | ')
            if turns < 5:
                print('  | ')
            if turns < 4:
                print('  0 ')
            if turns < 3:
                print(' /|\ ')
            if turns < 2:
                print('  | ')
            if turns < 1:
                print(' / \ ')
            if turns == 0:
                print('\n\nЭто слово: ', secret)


if __name__ == '__main__':
    ans = 'да'
    while ans == 'да':
        hangman_game()
        print('Хотите снова попасть на плаху?')
        ans = input()
