#funciones: Son líneas de código que se utilizan repetidas veces y para optimizar código.

#salida de string
print('Hola')

#funcion nom_funcion(#parámetro)
def my_print(text):
  #se define el comportamiento de la funcion , imprime 1 vez, 2 veces..
  print(text * 2)  #toma el parámetro del texto y lo multiplca por 2.
  #Si recibe un int los multiplica * 2
  #Si recibe un texto lo duplica
my_print('Esto es una funcion')

#Funcion Suma
#tradicional
a = 10
b = 20

c = a + b
#con función.
#Además podemos utilizar una función dentro de otra
def suma(a, b):
  my_print(a + b)

suma(10, 3)  #13
