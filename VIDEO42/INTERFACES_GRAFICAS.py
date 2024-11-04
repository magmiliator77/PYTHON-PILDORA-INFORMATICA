from tkinter import *

raiz=Tk()

raiz.title("TEST WINDOW")

#raiz.resizable(1,0)

#raiz.iconbitmap("icon.ico")

raiz.geometry("650x350")

raiz.config(bg="blue")

miFrame=Frame()
 
miFrame.pack(fill="y", expand="True")

miFrame.config(bg="red")

miFrame.config(width="650", height="350")

raiz.mainloop()







