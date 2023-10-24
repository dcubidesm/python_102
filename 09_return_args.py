#Funciones y Argumentos:


def find_volumen(len=1, width=1, depth=1):
  #      #arg1              , arg2,  arg3 - Se convierte en una tupla
  return len * width * depth, width, 'hola'  #en el retorno puedes enviar múltiple argumentos


result, width, string = find_volumen(len=10, width=10)
#imprime los valores de la tupla
print(result)  #[0], Retorna un valor de 10 de la tupla
print(width)
print(string)
