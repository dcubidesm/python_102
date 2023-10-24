#Para seguir con el manejo de errores , se hablará de las excepciones para precisamente manejar esos errores.
#Se puede unir todos los errores en un solo bloque de try y otro bloque de except
#ejemplo 1:
try:
  print(0 / 0)
except ZeroDivisionError as zerror:
  print(zerror)

#ejemplo 2:
try:
  assert 1 != 1, "Uno no es igual a uno"
except AssertionError as aerror:
  print(aerror)

#ejemplo 3:
age = 16
try:
  if age < 18:
    raise Exception("No se aceptan menores de edad")
except Exception as e:
  print(e)

print("hola")

print("Hola")


#Ejercicio:
def my_divide(a, b):
  try:
    result = a / b
  except ZeroDivisionError:
    result = "No se puede dividir por 0"
  return result


print('*' * 10)
response = my_divide(10, 2)
print(response)  # 5

response = my_divide(10, 0)
print(response)  # No se puede dividir por 0
