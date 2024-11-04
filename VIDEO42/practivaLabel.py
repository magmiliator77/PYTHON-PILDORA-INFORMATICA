from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

miImagen=PhotoImage(file="WS2c.png")


Label(miFrame,image=miImagen).place(x=200, y=100)


#Label(miFrame, text="Hola alumnos de python", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200) #PERMITE PERMITE UBICAR ALGO MEDIANTE LAS COORDENADAS X E Y



root.mainloop()