#Reduce: Reducir algo en un solo valor , es decir, tomar una lista y sacar una conclusión de eso.
import functools
##hermientas python


def accum(counter, item):
  print('Counter', counter)
  print('Item', item)
  return counter + item


numbers = [1, 2, 3, 4]
result = functools.reduce(accum, numbers)
print(result)
