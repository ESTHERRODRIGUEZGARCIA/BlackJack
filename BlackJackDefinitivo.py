from random import choice, sample

#valor de la carta,  lista de cartas para poder escoger una carta.

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
print("Cartas: {}".format(" ".join(cartas.keys())))
print("Puntos: {}".format(list(cartas.values())))

print("Iteración ordenada del diccionario: ")
for carta, valor in cartas.items():
    print("La carta {} vale {}".format(carta, valor))

print("Ahora juguemos al BlackJack: \nPodrás escoger dos cartas, una a continuación de la otra. \nSus valores serán sumados")
lista = list(cartas)
#ahora, en qué consiste el juego