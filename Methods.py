# 5 методов list (список)

my_list = [5, 15, 25, 35, 598, 25, 56, 598, -5, 25]
print('Мой список: ', my_list)

# медод .append(x)-  добавляет элемент x в конец списка
my_list.append(366)
print('В мой список добавлен элемент "366": ', my_list)

# метод .count(x) - возвращает количество элементов со значением x
number = my_list.count(25)
print('Количество элекетнов "25" в моем списке: ', number)

# метод  .sort(key=..., reverse=...) - сортирует список по возрастанию (по умолчанию),
# можно сортировать на основе функции или по убыванию, метод sort заменяет исходный список
my_list.sort()
print('Мой список, отсортированный по возрастанию: ', my_list)
my_list.sort(reverse=True)
print('Мой список, отсортированный по убыванию: ', my_list)

# метод .index(x, start , end) - возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
print('Индекс элемента "56": ', my_list.index(56))
print('Индекс элемента "25", начиная с 6-го и до конца: ', my_list.index(25, 6))

# метод .pop - удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
my_list.pop(0)
print('Из моего списка удален 0-ой элемент: ', my_list)
print('-'*100)

# 5 методов dict (словарь)
# создадим словарь из двух списков
food = ['zucchini', 'spinach', 'grapes', 'shrimp', 'gouda cheese']
calories = ['16', '23', '38', '99', '356']
my_dict = {f:c for f, c in zip(food,calories)}  # использование цикла for
print('Мой словарь: ', my_dict)

# метод len() - определяет длину (в конкретном примере - словаря)
print('Длина моего словаря: ', len(my_dict))

# метод .items() - этот метод возвращает итерируемый объект.
# Такой объект содержит пары ключ-значение для словаря по аналогии с кортежами в списке.
# Метод используется, когда нужно перебрать значения словаря.
for f,c in my_dict.items():  # использование цикла for
    print(f, c)

# метод .keys() - получаем все ключи из словаря
my_keys = my_dict.keys()
print('Ключи моего словаря: ', my_keys)

# метод .values() - получаем все значения из словаря
my_values = my_dict.values()
print('Значения моего словаря: ', my_values)

# метод .fromkeys() - возвращает словарь с указанными ключами и значениями
weight_food = dict.fromkeys(food, 100)
print('Вес продуктов: ', weight_food)

# некоторые операции со словарем:
# заменяем значение по ключу
weight_food['grapes'] = 200
print('Заменили вес винограда: ', weight_food)

# удаляем последний элемент словаря
weight_food.popitem()
print('Удалили из словаря последний элемент: ', weight_food)

# добавляем элемент в словарь
weight_food['mango'] = 150
print('Добавили в словарь манго: ', weight_food)

# получаем значение по ключу
spinach = weight_food['spinach']
print('Вес шпината: ', spinach)
print('-'*100)

# 5 методов set (множество)
# создадим два множества из списков. в множестве только уникальные зачения
food = ['zucchini', 'spinach', 'grapes', 'shrimp', 'gouda cheese', 'grapes', 'shrimp', 'gouda cheese']
mix = ['16', '23', '38', '99', '99', '356', 'spinach', 'grapes', 'shrimp']
my_set_food = set(food)
my_set_mix = set(mix)
print('Первое множество: ', my_set_food)
print('Второе множество: ', my_set_mix)

print('Одинаковые элементы в обоих множествах (пересечение): ', my_set_food.intersection(my_set_mix))
print('Уникальные элементы в первом множестве (их нет во втором): ', my_set_food.difference(my_set_mix))
print('Объединение первого и второго множеств: ', my_set_food.union(my_set_mix))
print('Все ли элементы первого множества есть во втором: ', my_set_food.issubset(my_set_mix))
print('Является ли первое множество надмножеством второго: ', my_set_food.issuperset(my_set_mix))
print('-'*100)

# 5 методов str (строк)
my_line = ('How are you?')
print('Моя строка: ', my_line)

# метод .split() - разбиение строки по разделителю
my_split = my_line.split()
print('Разбиение строки на элементы: ', my_split)

# метод join() - объединение элементов в строку (разделитель s -  пробел)
s = ' '
new_line = s.join(my_split)
print('Соединение элементов в строку: ', new_line)

# метод .lower() - преобразование строки к нижнему регистру
print('Строка в нижнем регистре: ', new_line.lower())

# метод .format() - форматирование строки
# метод .upper() - преобразование строки к верхнему регистру
print('{:*^45}'.format(new_line.upper())) # форматирование по центру (^)  с заполнением (*), всего 45 символов
print('Как дела? Перевод на английский: {}'.format(new_line))
print('-'*100)


# Неизменяемый список - tuple (кортеж)
my_tuple = tuple('How are you?')
my_tuple_number = tuple(calories)
print('Мой кортеж: ', my_tuple)
print('Мой кортеж из цифр: ', my_tuple_number)
print('Соединение кортежей: ', my_tuple + my_tuple_number)
print('Повторение кортежа: ', my_tuple * 2)
print('Количество "о": ', my_tuple.count('o'))
print('-'*100)


# использование цикла for
# перечисление элементов в списке food
for i in range(len(food)):
    print(i, food[i])

# перечисление букв в строке my_line
for letter in my_line:
    print(letter)

# перечисление ключей и значений словаря
for key in my_dict:
    print(key) # ключ словаря
    print(my_dict[key]) # значение словаря по ключу