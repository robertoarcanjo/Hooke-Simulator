import tkinter as tk
import sqlite3 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

root = tk.Tk()

root.title("ICM - Tensão vs Deformação")

root.geometry("750x700")

label = tk.Label(root, text = "Seja bem vindo!")

entry = tk.Entry(root)
entry.pack()

def processar_texto():
    texto_digitado = entry.get()
    entry.delete(0, "end")
    resultado.config(text=texto_digitado)

button = tk.Button(root, text="Enviar", command=processar_texto)
button.pack()

resultado = tk.Label(root, text=" ")

label.pack()

resultado.pack()


x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

fig = plt.figure()

ax = fig.add_subplot(111)
ax.set_xlabel("Deformação")
ax.set_ylabel("Tensão ")


ax.plot(x, y)

canvas = FigureCanvasTkAgg(fig, master=root)

plot_widget = canvas.get_tk_widget()

plot_widget.pack(side="top", fill="both", expand=True)

root.mainloop()