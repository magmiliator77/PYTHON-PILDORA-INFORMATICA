import tkinter as tk


def click():
    print("Button clicked!")

raiz = tk.Tk()
button = tk.Button(raiz, text="click ME", command=click)
button.pack()
raiz.mainloop()
