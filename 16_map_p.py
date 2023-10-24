items = [
    #1
    {
        'product': 'pantalones',
        'price': 500
    },
    #2
    {
        'product': 'camisa',
        'price': 100
    },
    #3
    {
        'product': 'pantalones 2',
        'price': 300
    }
]

#Ejemplo 2: Tenemos que agregar una nuevo item a cada uno de los diccionarios con los impuestos(taxes), para poder hacerlo en una lambda funciona toca crear otra funcion(def).


#               *
def add_taxes(item):
  item['taxes']: item['price'] * .19
  return item


new_list = list(map(add_taxes, items))
print(new_list)
