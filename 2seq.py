user_list = input('Введите любые цифры через запятую, точку с запятой или слэш: ')
user_list = user_list.replace(';', ',')
user_list = user_list.replace('/', ',')
user_list = set(user_list.split(sep=','))
user_list = [int(i) for i in user_list]
print(user_list)