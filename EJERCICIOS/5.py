#Ejercicio 5: Obtener la Representación Inversa de una Cadena de Caracteres

#Python => nohtyP

cadena = 'Python'

#METODO 1

for i in range(len(cadena) -1, -1, -1):
    print(cadena[i], end='')

print()

#METODO 2 SLICING
print(cadena[::-1])