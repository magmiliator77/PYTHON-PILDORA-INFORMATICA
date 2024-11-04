#Solicitar el Valor del Radio de un Círculo para Calcular su Área
import math

radio = float(input("Introduce el radio del circulo: "))

pi = 3.141592 

piRedondeado = round(pi, 2)

area = piRedondeado * (radio ** 2)


print(f"El area del ciculo con radio {radio} es: {area}")

#MEJORAS
#EN LA ENTRADA DE DATOS ANADIR UN ESPACIO
#REDENDEAR EL RESULTADO A DOS DECIMALES
