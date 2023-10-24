#Escribir dentro del archivo
#r, permisos de lectura
#w, permisos de escritura
#r+, permmisos de lectura y escritura
#w+, permisos de lectura y escritura pero sobreescribe el archivo
with open('./text.txt', 'w+') as file:
  for line in file:
    print(line)
  file.write('Hola soy Diana\n')
  file.write('Se agrego el registro\n')
  file.write('Salto de linea\n')
  file.write('Otro mas\n')
