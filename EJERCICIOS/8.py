#Ejercicio 8: Obtener el Primer y Último Elemento de una Lista

lenguajes = ['Python', 'C#', 'PHP', 'JAVA', 'JS']

#PRIMER ELEMENTO: PYTHON
#ULTIMO ELEMENTO: JS

#----------HECHO POR MI ANTES DE VER LA SOLUCIÓN -----------

primerElemento = lenguajes[0]

ultimoElemento = lenguajes[4]

print(f"El primer elemento de la lista es {primerElemento} y el ultimo es {ultimoElemento}")


#----------HECHO POR EL PROFE -----------

primer_elemento = lenguajes[0]

#Esto calcula el numero de posiciones que hay en la lista de lenguajes (5) y le resta una posicion, ya que el ultimo elemento esta en la posicon 4
#ultimo_elemento = lenguajes[len(lenguajes) -1]
ultimo_elemento = lenguajes[-1] # ---> ES LO MISMO PERA MAS FACIL (SE LLAMA NOTACION DE INDICES NEGATIVAS)

print(primer_elemento)

print(ultimo_elemento)






