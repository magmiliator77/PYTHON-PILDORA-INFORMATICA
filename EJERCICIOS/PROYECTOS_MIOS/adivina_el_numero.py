#GENERA UN NUMERO AL AZAR QUE EL USUARIO NO VE Y TIENES QUE INTENTAR ADIVINARLO

import random

numero_introducido = int(input("Introduce un número que este entre 0 y 10: "))

rango = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero_correcto = random.choice(rango)


def comprobacion_resultado(numero_introducido, numero_correto):

    if numero_introducido == numero_correcto:
        print("¡HAS GANADO!")
    else:
        print("¡HAS PERDIDO!")



print()






