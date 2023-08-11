# Игра Wordle в консоли 

import random    # Импортируем библиотеку random
from colorama import Fore

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
final_word = []  

def start_game(answer):     # Функция приветсвия
    
    

    if answer == 'да':
        print('Давайте начнём играть. У тебя есть 5 попыток чтобы угадать слово, загаданное мной. Буквы которые стоят на нужных местах подсвечиваются зеленым, если буквы есть в слове, но они не на своих местах, они подсвечиваются желтым.')
        print('Введите слово: ')
        
        game_logic(input())
            
    else:
        print('Пока')
        
def game_logic(your_word):

    count = 0

    while count != 5 and your_word != word:

        words = list(str(your_word))   # разбиваем слово пользователя на буквы
        
        for i in range(len(your_word)):
            if symbol_word[i] == words[i]:
                color(symbol=words[i], color='Green')
            elif words[i] in symbol_word:
                color(symbol=words[i], color="Yellow")
            else:
                color(symbol=words[i], color='White')
        print(''.join(final_word))
        print(Fore.WHITE)
        final_word.clear()
    
        count += 1

        if count == 5:
            print('У вас кончились попытки. Попробуйте еще раз')
            break
        elif word == your_word:
            print(f'Поздравляем, вы выиграли. Это слово {your_word}')
            break

        your_word = input()
        
    


def color(symbol, color):
    if color == 'Green':
        final_word.append(Fore.GREEN +symbol)
    elif color == "Yellow":
        final_word.append(Fore.YELLOW + symbol)
    elif color == 'White':
        final_word.append(Fore.WHITE + symbol)
    


print(symbol_word)
start_game(input('Готовы ли Вы начать играть?: '))
