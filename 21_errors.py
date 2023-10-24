#manejo de errores
#levantar nuestros propios errores
#Por ejemplo:
#1.SintaxError: Errores de sintaxis
#2.ZeroDivisorError: Operaciones matematicas diviendo en 0
#3. Name error: error en el llamado de una variable y si exite mas codigo no lo ejecuta.
#4.AssertionError: Verifica que tdo este bien en la función.
#
print("Hola")

#ASSERT : Coincide el resultado y continua las demás líneas de ejecución.
#Si no arroja un error de 4.
suma = lambda x, y: x + y
assert suma(2, 2) == 4

print("Hola 2")

#Ejer1:
#raise, me permite crear mis "propios" errores dentro de las funciones.
age = 16

if age < 18:
  raise Exception("No se aceptan menores de edad")
