import customtkinter as ctk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



vect = [27, 48, 36, 47, 50]
tests = [1,2,3,4,5]

def show_graph():
    connection_speed()

    ax.clear()

    testes = np.array(tests)

    ax.set_title("Velocidade - Download")
    ax.set_ylabel("velociade(mbps)")
    ax.set_xlabel("Teste")

    ax.plot(testes, wifi.download, label='Download', marker='.', linestyle="-", color="purple")

    canvas.draw()


def save_graph():
    pass

page = ctk.CTk()
page.geometry("840x640")
page.title("Wifi Speed Test")
page.grid_columnconfigure(0, weight=1)

fig, ax = plt.subplots()

canvas = FigureCanvasTkAgg(fig)
canvas.get_tk_widget().pack(pady=(25,0))

frame = ctk.CTkFrame(page, height=420, fg_color="transparent")
frame.pack(pady=(20,0))

do_test = ctk.CTkButton(frame, text="Test", command=show_graph)
do_test.pack(padx=20, pady=(10,0), side="left")

graph_file = ctk.CTkButton(frame, text="Save Graph", command=save_graph)
graph_file.pack(padx=20, pady=(10, 0), side="left")

page.mainloop()