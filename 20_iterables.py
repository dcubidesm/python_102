#Es una función que sirve para realizar iteraciones como los for
#

for i in range(1, 11):
  print(i)

my_iter = iter(range(1, 11))
print(my_iter)
#sirve para ejecutar el iterador manualmemte con next()
print(next(my_iter))

#Tener en cuenta el iterador manual porque si se pasa del rango limite envia un error de StopTIteration
