#scope: (alcance:) que alcance tiene una variable- bloque scope, enclosing scope, globla scope y Built - in

price = 100  #es una variable global scope, no tiene nada que ver con la var:price dentro de la función.
#tener en cuenta los contextos de las variables, tener cuidado como utilizarlas.
result = 500  # es una variable global scope


def increment():
  price = 200  #variable local scope
  result = price = price + 10
  print(result)
  return result


print(price)

price2 = increment()
print(price2 + 10)
print(
    result
)  #sale un error porque esta fuera del contexto de la función. #Al tener la variable inicializada fuera de la función el error se iria.
