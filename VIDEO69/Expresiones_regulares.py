import re

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

textoBuscar="Python"

print(len(re.findall(textoBuscar, cadena)))