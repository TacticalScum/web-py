from random import randint

UPPER_LIMIT = 1000
LOWER_LIMIT = 0
random_num = randint(LOWER_LIMIT, UPPER_LIMIT) 
counter = 10

print("У вас есть 10 попыток чтобы отгадать загаданное число.")

while counter > 0:
    user_num = int(input('\nВведите число в диапазоне от 0 до 1000: '))
    while True:
        if user_num < LOWER_LIMIT or user_num > UPPER_LIMIT: 
            user_num = int(input('Некорректное число. Введите число в диапазоне от 0 до 1000: '))
        else:
            break
    if user_num > random_num:
        print(f"Число {user_num} больше загаданного")
    elif user_num < random_num:
        print(f"Число {user_num} меньше загаданного")
    elif user_num == random_num:
        print(f"Вы угадали! Загаданное число - {user_num}!")
        break
    counter -=1
    print(f"Попыток осталось - {counter}!")
else:
    print("Попытки закончились, вы проиграли!")
