user_num = int(input('Введите число в диапазоне от -100 000 до 100 000: '))
UPPER_LIMIT = 100000
LOWER_LIMIT = -100000
counter = 0

while True:
    if user_num < LOWER_LIMIT or user_num > UPPER_LIMIT: 
        user_num = int(input('Некорректное число. Введите число в диапазоне от -100 000 до 100 000: '))
    else:
        break


for i in range(2, abs(user_num) // 2+1):
    if (user_num % i == 0):
        counter += 1

if counter <= 0:
    print(f"Число {user_num} является простым")
else:
    print(f"Число {user_num} является составным")
