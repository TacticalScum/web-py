numerator_1, denominator_1 = input('Введите первую дробь в формате "1/2": ').split('/')
numerator_2, denominator_2 = input('Введите вторую дробь в формате "1/2": ').split('/')

numerator_1 = int(numerator_1)
numerator_2 = int(numerator_2)
denominator_1 = int(denominator_1)
denominator_2 = int(denominator_2)

sum_result = round((numerator_1 * denominator_2 + numerator_2 * denominator_1) / (denominator_1 * denominator_2), 3)

multiplication_result = round((numerator_1 * numerator_2) / (denominator_1 * denominator_2),3)

print(f'Сумма дробей {numerator_1}/{denominator_1} и {numerator_2}/{denominator_2} = {sum_result}')
print(f'Произведение дробей {numerator_1}/{denominator_1} и {numerator_2}/{denominator_2} = {multiplication_result}')
