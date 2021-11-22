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

print("\n\nRecordemos las normas: ")
print("Al inicio de cada partida el jugador debe apostar.")
print("El crupier repartirá dos cartas descubiertas a cada jugador y una a sí mismo, también visible a los jugadores.")
print("Cada jugador decidirá si pide más cartas o se planta con las dos ya repartidas.")
print("Luego el crupier jugará su mano.")
print("Los jugadores que se queden más lejos de 21 que el crupier o que hayan sobrepasado este valor, pierden.")
print("Quienes tengan el mismo valor del crupier recuperan su apuesta pero no pierden ni ganan.")
print("Los jugadores que saquen BlackJack (as más 10 o figura) se les paga 3×2 y aquellos que superen al crupier se les paga 1×1 según la apuesta que hayan hecho.")
print("\nAhora, juguemos:")

lista = list(cartas)
print("Ha seleccionado:", end=" ")
carta = choice(lista)
score = cartas[carta]
print(carta, end=" ")
#aquí el programa nos enseña la carta que ha seleccionado
carta = choice(lista)
score += cartas[carta]
print(carta, end=" ")
print("\n >>> su puntuación es de", score)
#juego hecho
