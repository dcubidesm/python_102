#Diccionario comprehension:
#structure: {key:value for var in interable}
print('Example 1')

print('Forma tradicional:')
dict = {}
for i in range(1,5):
  dict[i] = i*2

print(dict)

print('Forma Comprehension:')
#versión corta
dict_v2={i: i*2 for i in range(1,5) } 
print(dict_v2)
print('-'*10)

print('Example 2')

print('Forma Tradicional:')
import random 
countries = ['col','mex','bol','pe']
population = {}

for country in countries:
  population[country] = random.randint(1,100)

print(population)

print('Forma Comprehension:')
#iterador: # aleatorios random for recorre la lista y llena el diccionario
population_v2 = {country: random.randint(1,100) for country in countries}
print(population_v2)
print('-'*10)
print('Example 3')
print('Forma Tradicional:')
names = ['nico','zule','santi']
ages = [12,56,98]
#tenemos una lista con tuplas dentro
{
  'nico':12,
  'zule':56,
  'santi':98
}

#unir una lista con otra, se usa ZIP
print(list(zip(names, ages)))

print('Forma Comprehension:')
new_dict = {name: age for (name, age) in zip(names, ages) }
print(new_dict)
