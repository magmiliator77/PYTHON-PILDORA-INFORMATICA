def funcion_decoradora(funcion_parametro):
    
    def funcion_interior():
        # Acciones adicionales que decoran
        print("vamos a realizar un cálculo: ")
        funcion_parametro()
        # Acciones adicionales que decoran
        print("Hemos terminado el cáclulo")
    return funcion_interior


@funcion_decoradora
def suma():
    
    print(15+28)

@funcion_decoradora
def resta():
    print (30-10)

suma()
resta()