import random


dict = {'Сменная обувь и одежда' : 5, 'Туристический коврик' : 2, 'Дождевик' : 1, 'Компас' : 1, 'Фонарик' : 1,
'Спрей от насекомых' : 1, 'Посуда и продукты для приготовления обеда' : 7, 'Термос с теплым напитком' : 2,
'Крем с солнцезащитным фактором' : 1, 'Аптечка' : 2, 'Туалетная бумага' : 1, 'Палатка' : 3, 'Спальный мешок' : 1}

user_bag = int(input('Введите грузоподъёмность рюкзака: '))

same_items_list = []

print(f'В рюкзак грузоподъёмностью {user_bag} кг можно взять следующие предметы:')

while user_bag >= 0 :
    
    if user_bag == 0:
        break

    hike_item = round(random.randint(0, len(dict)-1))
    
    if hike_item in same_items_list:
        continue
    else:
        same_items_list.append(hike_item)

    if user_bag - list(dict.values())[hike_item] < 0:
        continue
    else:
        print(f'- {list(dict)[hike_item]} весом {list(dict.values())[hike_item]} кг')
        user_bag = user_bag - list(dict.values())[hike_item]
