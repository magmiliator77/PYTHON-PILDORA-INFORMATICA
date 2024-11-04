# Ejercicio 14: Calcular la Diferencia en Días de Dos Fechas Dadas

from datetime import date

hoy = date(2019, 9, 16)
otra_fecha = date(2023, 2, 13)

delta = otra_fecha - hoy

print(delta)
print(delta.days)






