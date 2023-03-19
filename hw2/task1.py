user_num = int(input('Введите число: '))
TEMP = user_num

final_num = ''
alphabet = '0123456789ABCDEF'
 
while user_num > 0:
    final_num = alphabet[user_num % 16] + final_num
    user_num = user_num // 16
 
print(f'Число {TEMP} в шестнадцатиричной системе = {final_num}')
