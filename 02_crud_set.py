#CRUD de sets.
set_countries = {'col', 'mex', 'bol'}

print('--M E T O D O S - C R U D--')
size = len(set_countries)
print('Tamaño del conjunto:', size, 'elementos')

#validar la existencia de un valor, retorna booleno
print('col' in set_countries)
print('pe' in set_countries)

#add: Adicionar un elemento al set
set_countries.add('pe')
print(set_countries)

#update: actualiza un elemento del set
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

#remove : eliminar
set_countries.remove('col')
print(set_countries)
#cuando no encuentra un valor del conjunto arroja un error
set_countries.remove('ar')
print(set_countries)

#,solo si no existe, imprime el set y para esto existe otro metodo:
set_countries.discard('arg')
print(set_countries)
set_countries.add('arg')
print(set_countries)

#limpia TODO el conjunto
set_countries.clear()
print(set_countries) 
print(len(set_countries))
