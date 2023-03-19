triangle_side_A = int(input('Введите значения стороны треугольника "А": '))
triangle_side_B = int(input('Введите значения стороны треугольника "B": '))
triangle_side_C = int(input('Введите значения стороны треугольника "C": '))

if triangle_side_A + triangle_side_B < triangle_side_C:
    print ('Такого треугольника не существует')
elif triangle_side_A + triangle_side_C < triangle_side_B:
    print ('Такого треугольника не существует')
elif triangle_side_B + triangle_side_C < triangle_side_A:
    print ('Такого треугольника не существует')
else:
    if triangle_side_A != triangle_side_B and triangle_side_A != triangle_side_C and triangle_side_B != triangle_side_C:
        print (f'Трегольник со сторонами: {triangle_side_A}, {triangle_side_B}, {triangle_side_C} - Разносторонний')
    elif triangle_side_A == triangle_side_B and triangle_side_A == triangle_side_C and triangle_side_B == triangle_side_C:
        print (f'Трегольник со сторонами: {triangle_side_A}, {triangle_side_B}, {triangle_side_C} - Равносторонний')
    elif triangle_side_A == triangle_side_B or triangle_side_A == triangle_side_C or triangle_side_B == triangle_side_C:
        print (f'Трегольник со сторонами: {triangle_side_A}, {triangle_side_B}, {triangle_side_C} - Равнобедренный')
