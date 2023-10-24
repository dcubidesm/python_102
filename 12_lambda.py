#lambda: Es una funcion gran versatilidad y de manejar sintaxis para las funciones, solo se debe crear en una sola linea ya que es entrada : salida
def increment(x):
  return x + 1


result = print(increment(10))

#lamda:
#parametros de entrada : parametros de salida (return)
increment_V2 = lambda x: x + 1
result = increment_V2(20)
print(result)

#ejercicio 2:
#title: Para poner la 1era letra en mayus
full_name = lambda name, last_name: f'Full name is :{name.title()} {last_name.title()}'

text = full_name('diana', 'cubides marin')
print(text)
