# Ejercicio 10: Solicitar al Usuario un Número n y Calcular n + nn + nnn

#n = 3 => 3 + 33 + 333 = 369

n=input("Escriba el valor de n: ")

nn=int('{}{}'.format(n, n))

nnn=int('{}{}{}'.format(n, n, n))

n=int(n) #Convierte a entero

suma=n + nn + nnn

print(suma)



