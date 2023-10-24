#El filter puede recibir de igual manera los HOF una función o una lambda function
#Filter con una lista de diccionarios:
matches = [
    {
        'home_team': 'Bolivia',  #E.local
        'away_team': 'Uruguay',  #E. visitante
        'home_team_score': 3,  #Goles
        'away_team_score': 1,
        'home_team_result': 'Win'
    },
    {
        'home_team': 'Brazil',
        'away_team': 'Mexico',
        'home_team_score': 1,
        'away_team_score': 1,
        'home_team_result': 'Draw'
    },
    {
        'home_team': 'Ecuador',
        'away_team': 'Venezuela',
        'home_team_score': 5,
        'away_team_score': 0,
        'home_team_result': 'Win'
    },
]

print(matches)
print(len(matches))
#Vamos a filtrar por los equipos de futbol ganadores Win.

list_win = list(filter(lambda item: item['home_team_result'] == 'Win',
                       matches))

print(list_win)
print(len(list_win))


#RETO
def filter_by_length(words):
  # Escribe tu solución 👇
  return list(filter(lambda item: len(item) >= 4, words))


words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)
