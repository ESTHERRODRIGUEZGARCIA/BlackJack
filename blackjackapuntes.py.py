from random import choice, sample


cartas = { 
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10, 
} 
#un dicc por si mismo tiene dos valores, el key y el valor. 

print("Cartas: {}".format(" ".join(cartas.keys()))) 

# hay que rellenarlo con la key, definido por python. El .format, todo lo que hay dentro del paréntesis, lo pone entre las llaves
#ahora quiero que me de el valor; se hace de forma similar pero con los datos que queremos

print("Puntos: {}".format(list(cartas.values())))

#necesitamos un item para que () sea valor * valor
#for lo que hace es que recorra todo. Si solo necesitamos un valor es sin el for, items(4)

print("1\ Iteración estándar sobre un diccionario")
for carta, valor in cartas.items():
    print("la carta {} vale {}".format(carta, valor))

#ahora para que quede ordenado, utilizo el sorted, me ordena de menor valor a mayor por defecto
#Quiero ordenar para que lo coja de forma random

print("2\ Iteración ordenada sobre un diccionario")
for carta in sorted(cartas.keys()):
    print("la carta {} vale {}".format(carta, cartas[carta]))

#ahora jugamos al blackjack. Me crea una lista de esas cartas, del diccionario

print("3\ Black Jack")
lista_cartas = list(cartas)


#solo se puede elegir una carta
print("Ha seleccionado:", end=" ")

carta = choice(lista_cartas)

score = cartas[carta]

print(carta, end=" ")
#eliges otra
carta = choice(lista_cartas)
#sumas los valores de ambas cartas(+=). Solo quiero sacar 2 cartas 
score += cartas[carta]

print(carta, end=" ")

print(" >>> su puntuación es de", score)

#sample sirve para barajar, parte de la banca
main_banca = sample(lista_cartas, 2)
score_banca = sum(cartas[carta] for carta in main_banca)
print("La banca tiene: {} {}  >> su score es {}".format(main_banca[0],
                                                          main_banca[1],
                                                          score_banca))
