# CALCULADORA by MIGUEL TORRES MARTÍNEZ

from tkinter import *  # Asegúrate de que tkinter esté importado correctamente

# Inicialización de la ventana principal
raiz = Tk()
miFrame = Frame(raiz)
miFrame.pack()

operacion = ""
resultado = 0
reset_pantalla = False
numeroPantalla = StringVar()

# -----------------pantalla----------------------
pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="black", fg="green", justify="right")

# ----------------Pulsaciones teclado --------------------------
def numeroPulsado(num):
    global operacion
    global reset_pantalla
    if reset_pantalla:
        numeroPantalla.set(num)
        reset_pantalla = False
    else:
        numeroPantalla.set(numeroPantalla.get() + num)

# ---------------funcion suma -----------------
def suma(num):
    global operacion
    global resultado
    global reset_pantalla
    resultado = int(numeroPantalla.get())
    operacion = "suma"
    reset_pantalla = True

# ---------------funcion resta -----------------
def resta(num):
    global operacion
    global resultado
    global reset_pantalla
    resultado = int(numeroPantalla.get())
    operacion = "resta"
    reset_pantalla = True

# ---------------funcion multiplicacion -----------------
def multiplicacion(num):
    global operacion
    global resultado
    global reset_pantalla
    resultado = int(numeroPantalla.get())
    operacion = "multiplicacion"
    reset_pantalla = True

# ---------------funcion division -----------------
def division(num):
    global operacion
    global resultado
    global reset_pantalla
    resultado = int(numeroPantalla.get())
    operacion = "division"
    reset_pantalla = True

# ----------------TECLA DE BORRAR C --------------------------
def teclaBorrar(botonC):
    global resultado
    global operacion
    global reset_pantalla
    pantalla.delete(0, END)
    resultado = 0
    operacion = ""
    reset_pantalla = False

# -------------funcion el_resultado-------------------
def el_resultado():
    global resultado
    global operacion
    global reset_pantalla
    if operacion == "suma":
        resultado += int(numeroPantalla.get())
    elif operacion == "resta":
        resultado -= int(numeroPantalla.get())
    elif operacion == "multiplicacion":
        resultado *= int(numeroPantalla.get())
    elif operacion == "division":
        resultado /= int(numeroPantalla.get())
    numeroPantalla.set(resultado)
    operacion = ""
    reset_pantalla = True

# -----------------fila 1------------------------
boton7 = Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botondiv = Button(miFrame, text="/", width=3, command=lambda:division(numeroPantalla.get()))
botondiv.grid(row=2, column=4)

# -----------------fila 2------------------------
boton4 = Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5 = Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult = Button(miFrame, text="x", width=3, command=lambda:multiplicacion(numeroPantalla.get()))
botonMult.grid(row=3, column=4)

# -----------------fila 3------------------------
boton1 = Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2 = Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3 = Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest = Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=4, column=4)

# -----------------fila 4------------------------
boton0 = Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa = Button(miFrame, text=",", width=3, command=lambda:numeroPulsado(","))
botonComa.grid(row=5, column=2)
botonIgual = Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonIgual.grid(row=5, column=3)
botonSum = Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)

# -----------------fila 5------------------------
botonC = Button(miFrame, text="C", width=3, command=lambda:teclaBorrar(""))
botonC.grid(row=6, column=1)

raiz.mainloop()
