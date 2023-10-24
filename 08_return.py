#Return: Me retorna el resultado de una función y lo guarda en dos resultados utilizando parámetros
'''

def sum_with_range(min, max):  #parametros a recibir
  print(min, max)
  sum = 0
  for x in range(min, max):  #parametros a recibir
    sum += x  #suma lo recibido en los paramtros
    return sum  # retorna el resultado de esa operacion


result = sum_with_range(2, 5)  #parametros
print(result)
result_v2 = sum_with_range(result, result + 10)
print(result_v2)
'''


def sum_with_range(min, max):
  print(min, max)
  sum = 0
  for x in range(min, max):
    sum += x
  return sum


result = sum_with_range(1, 10)
print(result)
result_2 = sum_with_range(result, result + 10)
print(result_2)
