#diccionary comprenhension con condicional
#structure: {key:value for var in iterable if condition}

print('Forma Tradicional:')
import random

countries = ['col', 'mex', 'bol', 'pe']
population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)

print('Forma Comprehension:')
#key:value for (key:value) in dict ya creado de los items y la condicion
#Me trae los paises donde su poblacion es > 50 y llena el diccionario con el resultante
##ejercicio 1
result = {
    country: population
    for (country, population) in population_v2.items() if population > 50
}
print(result)

text = 'Hola, soy Diana'
unique = {c: c.upper() for c in text if c in 'aeiou'}
print(unique)
