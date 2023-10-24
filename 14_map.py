#MAP: Es una función HOF que puede llamar a otra función ó lambda directamente, sirve para transformar los datos de una lista(array) dada de elementos.
#Se obtiene el mismo número de elementos del array o elementos iterables

#ejemplo:
numbers = [1, 2, 3, 4]
numbers_v2 = []

for i in numbers:
  numbers_v2.append(i * 2)

print(numbers)
print(numbers_v2)

#ejemplo 2: lamda
#Nom_var   = (lambda PE : PS, lista a modificar)
#Si no se convierte a lista , envia una referencia que es un map
numbers_v3 = list(map(lambda i: i * 2, numbers))
print(numbers_v3)

#ejemplo 3: Se puede transformar 2 listas, pero el limite siempre será la lista mas pequeña
numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]
print('*' * 10)
print(numbers_1)

print(numbers_2)

result = list(map(lambda x, y: x + y, numbers_1, numbers_2))

print(result)


def multiply_numbers(numbers):
  return list(map(lambda x: x * 2, numbers))


numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)
