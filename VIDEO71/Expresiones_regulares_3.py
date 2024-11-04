import re

lista_nombres=['Ma.1',
                'Sel'
                'Ma2',
                'Bal',
                'Ma:3',
                'Val',
                'Va2',
                'Ma4',
                'MaA',
                'Ma.5',
                'MaB',
                'Ma:C']

for elemento in lista_nombres:
    if re.findall('Ma[.:]', elemento):
        
        print(elemento)