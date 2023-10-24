#Modules: permite usar estas herramientas disponibles en python como por ejemplo functools.
#las expresuones regulares son transversales son iguales en javascript, python , c.

#permite validar informacion de la ruta
#donde estamos ejecutando este archivo.
import sys

print(sys.path)

import re  #Se utiliza para xpresiones regulares

text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte 3'
result = re.findall('[0-9]+', text)
print(result)

import time  #manejo de fechas y hora

timestamp = time.time()  #fecha y hora en formato unix
print(timestamp)

local = time.localtime()

result = time.asctime(local)
print(result)

#sirve para manejar listas
import collections

numbers = [1, 1, 2, 1, 2, 1, 4, 5, 3, 3, 21]
counter = collections.Counter(numbers)  #se obtiene una lista de un diccionario
print(counter)
