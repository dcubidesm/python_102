#Se hará un ejemplo de un array con map y agregando otro key:value a un array nuevo y que no modifique el original.

#REFERENCIA EN MEMORIA: es un lugar reservado con ese diccionario
items = [{
    'product': 'camisa',
    'price': 100,
}, {
    'product': 'pantalones',
    'price': 300
}, {
    'product': 'pantalones 2',
    'price': 200
}]


def add_taxes(item):
  #Se debe crear una copa de la lista de diccionario
  new_items = item.copy()
  #Acá en cada iteracion guarda en memoria
  new_items['taxes'] = new_items['price'] * .19
  return new_items


new_items = list(map(add_taxes, items))
print('*' * 10)
print(new_items)
print('*' * 10)
print(items)
