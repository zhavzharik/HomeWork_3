elements = int(input('Введите количество элементов: '))
list_of_elements =[]
for i in range(1, elements+1):
    element = int(input('Введите {} элемент '.format(i)))
    list_of_elements.append(element)
list_of_elements.sort()
print(list_of_elements)
