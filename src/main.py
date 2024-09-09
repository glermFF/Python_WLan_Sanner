#from gui.app_window import main_page
import customtkinter as ctk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from app.wifi_speed_test import *


def show_graph():
    connection_speed()
    data_frame = df_connection_speed()

    ax.clear()

    #Graph 1
    y = data_frame["Download(mbs)"]

    ax.set_ylabel("Velociade(mbps)")
    ax.set_xlabel("Teste")

    ax.plot(y,  marker='.', linestyle="--", color="purple")
    ax.grid()

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

main_frame = ctk.CTkFrame(page, fg_color="transparent", corner_radius=3)
main_frame.pack(anchor="center",pady=(35,0),padx=40 ,ipadx=10, ipady=20)

do_test = ctk.CTkButton(main_frame, text="Test", fg_color="black", width=40, corner_radius=5, command=show_graph)
do_test.pack(padx=40, pady=(0,0), side="left")

graph_file = ctk.CTkButton(main_frame, text="Save Graph", fg_color="black", width=40, corner_radius=5, command=save_graph)
graph_file.pack(padx=20, pady=(0, 0), side="right")

page.mainloop()