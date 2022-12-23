import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ttkwidgets import Table
import math


root = tk.Tk()

root.title("ICM - Tensão vs Deformação")

root.geometry("750x700")

label = tk.Label(root, text = "Seja bem vindo!")
label2 = tk.Label(root, text = "Determine um ângulo para obter um gráfico tensão deformação na zona elástica, em função deste ângulo")
label2.pack()
entry = tk.Entry(root)
entry.pack()
texto_digitado = entry.get()
angulo = 0

def processar_texto():
    texto_digitado = entry.get()
    angulo = int(texto_digitado)
    entry.delete(0, "end")
    resultado.config(text="O ângulo é " + texto_digitado + "°")
    update_plot(angulo)

def update_plot(angulo):
    
    alfa = math.tan(math.radians(angulo))

    x = [0.01 * i for i in range(100)]
    y = [alfa * i for i in x]

    ax.clear()
    ax.plot(x, y)
    #Mostrando dois pontos do gráfico
    print("(",x[10],",",y[10],")\n")
    print("(",x[50],",",y[50],")\n")
    canvas.draw()


button = tk.Button(root, text="Enviar", command=processar_texto)
button.pack()

resultado = tk.Label(root, text=" ")

label.pack()

resultado.pack()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel("Deformação")
ax.set_ylabel("Tensão ")

canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()
plot_widget.pack(side="top", fill="both", expand=True)




root.mainloop()




