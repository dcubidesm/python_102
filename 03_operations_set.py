#Operaciones entre conjuntos:
#UNION: unifica +2 sets
set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

print('-'*10)
print('--Operadores de Conjunto--')
print('-'*10)
#Forma 1: Metodo Union
set_union = set_a.union(set_b)
print('Forma 1 con union: ', set_union)
#Forma 2: con un operador (|)
print('Forma 2 con |: ', set_a | set_b)
print('-' * 10)
#INTERSECTION: Elementos en común
set_intersection = set_a.intersection(set_b)
#Forma 1: Metodo Intersection
print('Forma 1 con intersection: ', set_intersection)
#Forma 2: con un operador (&)
print('Forma 2 con &: ', set_a & set_b)
print('-'*10)

#DIFFERENCE: Muestra los elementos del 1er conjunto removiendo la interseccion y set_b
set_difference = set_a.difference(set_b)
#Forma 1: Metodo difference
print('Forma 1 con difference: ', set_difference)
#Forma 2: con un operador (-)
print('Forma 2 con -: ', set_a - set_b)
print('-'*10)

#SYMMETRIC DIFFERENCE: Muestra los elementos externos removiendo los datos en común.
set_sym_difference = set_a.symmetric_difference(set_b) 
#Forma 1: Metodo difference
print('Forma 1 con symmetric difference: ', set_sym_difference)
#Forma 2: con un operador (^) intercalacion
print('Forma 2 con ^: ', set_a ^ set_b)
