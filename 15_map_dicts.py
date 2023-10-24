#Map con diccionarios: podemos trasformar una lista de diccinarios a una lista de números.
#Ejemplo: Una lista de diccionarios de una orden de compra:
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

prices = list(map(lambda item: item['price'], items))
print(items)
print('*' * 10)
print(prices)


#Vamos a transformar una lista de diccionarios en solo una lista de numeros.
#              *
def add_taxes(item):
  item['taxes'] = item['price'] * .19
  return item


new_items = list(map(add_taxes, items))
print('*' * 10)
print(new_items)
print('*' * 10)
print(items)


