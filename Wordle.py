# Игра Wordle в консоли 

import random    # Импортируем библиотеку random

words_list = [     #Список слов
    'багаж',
    'рамка',
    'шайба',
    'белка',
    'бочка',
    'мужик',
    'спина',
    'буфет',
    'бонус',
    'конус',
]

word = random.choice(words_list)   # Случайный выбор слова 
symbol_word = list(str(word))  # # Слово по буквам  

def start_game(answer):     # Функция приветсвия
    
    if answer == 'да':
        print('Давайте начнём играть. У тебя есть 5 попыток чтобы угадать слово, загаданное мной. Буквы которые стоят на нужных местах подсвечиваются зеленым, если буквы есть в слове, но они не на своих местах, они подсвечиваются желтым.')
        game_logic(input('Введите слово: '))
    else:
        print('Пока')
        

def game_logic(your_word):
    words = list(str(your_word))   # рАзбиваем слово пользователя на буквы
    for i in range(len(your_word)):
        if symbol_word[i] == word[i]:
            print('Буква на своем месте: ')
        elif word[i] in symbol_word:
            print('Буква есть в слове, но не на своем месте')
        else:
            continue

print(symbol_word)
start_game(input('Готовы ли Вы начать играть?: '))
