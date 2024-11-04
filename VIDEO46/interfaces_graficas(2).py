from tkinter import *

raiz=Tk()
raiz.title("CUADROS DE TEXTOS ")

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

#Video 46

minombre=StringVar()

#Video 46

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="orange", justify="center")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

#VIDEO 46

textoComentario=Text(miFrame, width=16, height=16)
textoComentario.grid(row=4, column=1, padx=10, pady=10)


ScrollVert=Scrollbar(miFrame, command=textoComentario.yview)
ScrollVert.grid(row=4, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=ScrollVert.set)

#VIDEO 46


nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=3, column=0,sticky="e", padx=10, pady=10) 

passLabel=Label(miFrame, text="Password:")
passLabel.grid(row=1, column=0,sticky="e", padx=10, pady=10) 

#VIDEO 46

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0,sticky="e", padx=10, pady=10) 

def codigoBoton():
    minombre.set("Miguel")

botonEnvio=Button(miFrame, text="Enviar", command=codigoBoton)
botonEnvio.grid(row=5, column=1)



raiz.mainloop()






