purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]


'''
item — название товара,
category — категория товара,
price — цена за единицу товара,
quantity — количество единиц, купленных за один раз.
'''


def total_revenue(purchases):
    '''
    Рассчитайте и верните общую выручку (цена * количество).
    '''
    revenue = 0
    for i in purchases:
        revenue += i['price'] * i['quantity']
    return revenue


def items_by_category(purchases):
    '''
    Верните словарь, где ключ — категория, а значение — список уникальных товаров в этой категории.
    '''
    category_dict = {}
    for i in purchases:
        category = i['category']
        item = i['item']
        if category not in category_dict:
            category_dict[category] = []
        if item not in category_dict[category]:
            category_dict[category].append(item)
    return category_dict


min_price = 1.0 # минимальная цена для expensive_purchases

def expensive_purchases(purchases, min_price):
    '''
    Выведите все покупки, где цена товара больше или равна min_price.
    '''
    expensive_purchases_list = []
    for i in purchases:
        if i['price'] >= min_price:
            expensive_purchases_list.append(i)
    return expensive_purchases_list


def average_price_by_category(purchases):
    '''
    Рассчитайте среднюю цену товаров по каждой категории.
    '''
    category_price_dict = {}
    category_avg_dict = {}
    for i in purchases:
        category = i['category']
        price = i['price']
        if category not in category_price_dict:
            category_price_dict[category] = []
        category_price_dict[category].append(price)
    for category  in category_price_dict:
        prices = category_price_dict[category]
        category_avg_dict[category] = sum(prices) / len(prices)
    return category_avg_dict


def most_frequent_category(purchases):
    '''
    Найдите и верните категорию, в которой куплено больше всего единиц товаров (учитывайте поле quantity).
    '''
    category_quantity_dict = {}
    for i in purchases:
        category = i['category']
        quantity = i['quantity']
        if category not in category_quantity_dict:
            category_quantity_dict[category] = 0
        category_quantity_dict[category] = category_quantity_dict.get(category) + quantity
    return max(category_quantity_dict, key=category_quantity_dict.get)

#вывод результатов
print(f'Общая выручка: {total_revenue(purchases)}')
print(f'Товары по категориям: {items_by_category(purchases)}')
print(f'Покупки дороже {min_price}: {expensive_purchases(purchases, min_price)}')
print(f'Средняя цена по категориям: {average_price_by_category(purchases)}')
print(f'Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}')