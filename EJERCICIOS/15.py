#Ejercicio 15: Calcular el Volumen de una Esfera a partir del Radio Dado

from math import pi

r = float(input("Escribe el radio de la esfera: "))

volumen = 4/3 * pi * r ** 3

volumen_rounded = round(volumen, 2)

print("El volumen de la esfera es {} unidades cubicas".format(volumen_rounded))