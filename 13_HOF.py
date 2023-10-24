#Higher order function (HOF): Permite enviar un funcion dentro de otra funcion.
#funcion 1:
def increment(x):
  return x + 1


#funcion 2:
#Recibe 2 parametros x el valor que se envia y 2 el return de una funcion(increment).
#Con el fin de ser mas dinamico a la hora de enviar funciones lamda o definiarlas , puede ser directamente
def higher_ord_fun(x, func):
  return x + func(x)


# x , func
# 2 , (2 + 1)
result = higher_ord_fun(2, increment)
print(result)

#Ejemplo con LAMBDA y HOF
#funcion 1
increment_v2 = lambda x: x + 1

#funcion 2
higher_ord_fun_v2 = lambda x, func1: x + func1(x)
result = higher_ord_fun_v2(2, increment_v2)
print(result)

# x , func
# 2 , (2 + 2)
result = higher_ord_fun_v2(2, lambda x: x + 2)
print(result)
# x , func
# 2 , (2 * 3)
result = higher_ord_fun_v2(2, lambda x: x * 3)
print(result)
