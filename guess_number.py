from random import randint


#The great beginning

WELCOME_MESSAGE = 'Угадайте число от 1 до 100:'
print(WELCOME_MESSAGE)
number = randint(1, 100)
print('Угадайте число от 1 до 100')

def main():
    while True:
        guess = int(input('Введите число: '))
        if guess < number:
            print('Ваше число меньше того, что загадано.')
        elif guess > number:
            print('Ваше число больше того, что загадано.')
        elif guess == number:
            break

main()
print('Отличная интуиция! Вы угадали число :)')