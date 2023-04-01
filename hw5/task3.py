def fib_num(user_num):
    a, b = 0, 1
    for _ in range(user_num):
        yield a
        a, b = b, a + b


user_num = int(input('Введите число: '))
print(list(fib_num(user_num)))
