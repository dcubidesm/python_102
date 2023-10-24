#List comprehension
#Example 1: list de 10 numeros
#estructura: [element for element in iterable]
'''
numbers = [] 
for element in range(1,11):
  numbers.append(element *2 )

print(numbers)
print('-'*10)
#Example 2: list de 10 numeros en una sola linea
#element = iterador lo que hace dentro del for 
numbers_v2 = [element *2 for element in range(1,11)]
print(numbers_v2)
'''
print('-' * 10)

#estructura con condicion: [element for element in iterable if condition]
#Forma tradicional:
print('Forma Tradicional:')
numbers = []
for i in range(1, 11):
  if i % 2 == 0:
    numbers.append(i * 2)

print(numbers)
print('-' * 10)
#Forma de list comprehension: tiene legibilidad
print('Forma con list comprehension:')
#[operacion del iterador-primera parte del for-la primera parte del if]
numbers_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_v2)
print('-' * 10)
