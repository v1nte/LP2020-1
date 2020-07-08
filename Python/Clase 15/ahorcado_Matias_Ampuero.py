import msvcrt
import random
import os

IMAGES =['''

        +-----+
        |     |
              |
              |
              |
              |
              |
              |
    ====================''','''


        +-----+
        |     |
        O     |
              |
              |
              |
              |
    ====================''','''

        +-----+
        |     |
        O     |
        |     |
              |
              |
              |
              |
    ====================''','''


        +-----+
        |     |
        O     |
       /|     |
              |
              |
              |
              |
    ====================''','''

        +-----+
        |     |
        O     |
       /|\    |
              |
              |
              |
              |
    ====================''','''

        +-----+
        |     |
        O     |
       /|\    |
        |     |
              |
              |
              |
    ====================''','''

        +-----+
        |     |
        O     |
       /|\    |
        |     |
       /      |
              |
              |
    ====================''','''

        +-----+
        |     |
        O     |
       /|\    |
        |     |
       / \    |
              |
              |
    ====================''']

WORDS=['LAVADORA',
'SECADORA',
'COMPUTADOR',
'TECLADO',
'PALOMA',
'BARTOK',
'SOFA',
'MESA',
'GATO',
'LEON',
'MATIAS',
'CELULAR']

def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]



def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print("")
    print(hidden_word)
    print('* ----------* ----------* ----------* ----------* ----------* ----------*')




def run():
    print("BIENVENIDO AL JUEGO DEL AHORCADO! JEJE")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    os.system("cls")
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)

        current_letter = str(input('Escoge una letra: ')).upper()
        os.system("cls")

        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('Â¡Perdiste! La palabra correcta era {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []

        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('¡Felicidades! Ganaste. La palabra es: {}'.format(word))
            break




run()
