#Sets: Estructura de datos, agrupa elementos que tienen algo en común,
#se pueden modificar, no tiene un orden y no se pueden duplicar
set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 45, 6, 7, 7}
print(set_numbers)

set_types = {'hola', 7, 36.25, False}
print(set_types)

#crea un set apartir de un string con la funcion set.
#lo que hace es dividir el texto en 4 elementos
set_from_string = set('hola')
print(set_from_string)

#crea un set apartir de una tupla con la funcion set.
set_from_tuples = set(('abc', 'as', 'def', 'abc'))
print(set_from_tuples)

#crea un set apartir de una lista con la funcion set.
numbers = [1, 2, 3, 1, 2, 3, 4]
set_from_list = set(numbers)
print(''set_from_list)
#pasar el conjunto de datos unicos a una lista o tupla
unique_numbers = list(set_from_list)
print(unique_numbers)
unique_numbers = tuple(set_from_list)
print(unique_numbers)
