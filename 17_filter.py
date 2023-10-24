#Función Filter: Sirve para filtrar dentro de una lista y crear una nueva.

numbers = [1, 2, 3, 4, 5]
new_list = list(filter(lambda x: x % 2 == 0, numbers))
print(numbers)
print(new_list)
