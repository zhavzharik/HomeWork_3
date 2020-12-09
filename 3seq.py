user_list_one = (input('Введите элементы 1-го списка: '))
user_list_one = user_list_one.replace(';', ',')
user_list_one = user_list_one.replace('/', ',')
user_list_one = user_list_one.split(sep=',')
user_list_one = [int(i) for i in user_list_one]

user_list_two = (input('Введите элементы 2-го списка: '))
user_list_two = user_list_two.replace(';', ',')
user_list_two = user_list_two.replace('/', ',')
user_list_two = user_list_two.split(sep=',')
user_list_two = [int(i) for i in user_list_two]

print(user_list_one)
print(user_list_two)
result_list =[]
for element in user_list_one:
    if element not in user_list_two:
        result_list.append(element)
print(result_list)