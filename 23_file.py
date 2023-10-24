#Permite leer archivos, en este caso será uno txt.
file = open('./text.txt')
#Forma 1: #me permite leer todo el archivo
#print(file.read())
#Forma 2: #me permite leer linea a linea del archivo, como un iterador
"""
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
"""

for line in file:
  print(line)

file.close()  #Sirve como método para cerrar el archivo y liberar memoria.

#Se puede utilizar with para cerrar el archivo y liberar espacio en memoria de forma aotomática.
#No es necesario colocar el close()

with open('./text.txt') as file:
  for line in file:
    print(line)
