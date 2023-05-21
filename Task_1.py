from pprint import pprint

with open('recipe.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        ingredient_count = int(f.readline())
        dish = []
        for _ in range(ingredient_count):
            core = f.readline()
            ing, count, unit, = core.strip().split(' | ')
            dishes = {
                'ingredient_name': ing,
                'quantity': count,
                'measure': unit
            }
            dish.append(dishes)
        f.readline()
        cook_book[dish_name] = dish

for dish in cook_book:
    pprint(f'{dish}: \n{cook_book.get(dish)}')


def get_shop_list_by_dishes(dis, person_count):
    shop_list = {}
    if isinstance(dis, list):
        for b in dis:
            if b in cook_book:
                for i in cook_book.get(b):
                    name, measure, quantity = i.get('ingredient_name'), i.get('measure'), \
                        int(i.get('quantity')) * person_count
                    shop_list_1 = {
                        'measure': measure,
                        'quantity': quantity
                    }
                    shop_list[name] = shop_list_1
        pprint(shop_list)
    else:
        if dis in cook_book:
            for i in cook_book.get(dis):
                name, measure, quantity = i.get('ingredient_name'), i.get('measure'), \
                    int(i.get('quantity')) * person_count
                shop_list_1 = {
                    'measure': measure,
                    'quantity': quantity
                }
                shop_list[name] = shop_list_1
            pprint(shop_list)

print('--------------------')
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 1)
print('--------------------')
get_shop_list_by_dishes('Омлет', 2)
