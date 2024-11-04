#Ejercicio 18: Calcular la Suma de Tres Números e Incluir una Condición de Igualdad

def suma_numeros(a, b, c):
    """
    Calcula la suma de tres numeros. Si los tres numeros son iguales, la suma se multiplica por 3.
    
    """
    
    suma = a + b + c

    if a == b and a == c:
        suma *= 3

    return suma


print(suma_numeros(2, 2, 7))
print(suma_numeros(2, 2, 2))






