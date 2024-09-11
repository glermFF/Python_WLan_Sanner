from customtkinter import *
from app.wifi_speed_test import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

class AppWindow:

    def __init__(self) -> None:
        self.page = CTk()
        self.page.geometry("840x640")
        self.page.title("Wifi Speed Test")
        self.page.grid_columnconfigure(0, weight=1)

        fig = Figure(figsize=(4.5, 4.5), facecolor="#f5ffff")
        self.ax = fig.add_subplot()

        self.canvas = FigureCanvasTkAgg(fig)
        self.canvas.get_tk_widget().pack(pady=(35,0))

        self.main_frame = CTkFrame(self.page, fg_color="transparent", corner_radius=3)
        self.main_frame.pack(anchor="center",pady=(35,0),padx=40 ,ipadx=10, ipady=20)

        self.do_test = CTkButton(self.main_frame, text="Test", fg_color="black", width=40, corner_radius=5, command=self.show_graph) #
        self.do_test.pack(padx=40, pady=(0,0), side="left")

        self.graph_file = CTkButton(self.main_frame, text="Save Graph", fg_color="black", width=40, corner_radius=5) #command=save_graph
        self.graph_file.pack(padx=20, pady=(0, 0), side="right")

        self.page.mainloop()

    def show_graph(self):
        connection_speed()
        data_frame = df_connection_speed()

        self.ax.clear()

        #Graph 1
        x = np.array([1,2,3,4,5])
        y = data_frame["Download(mbs)"]

        self.ax.set_ylabel("Velociade(mbps)")
        self.ax.set_xlabel("Teste")

        self.ax.set_facecolor('#f5ffff')
        self.ax.fill_between(x=x, y1=y)
        self.ax.plot(x, y,  marker='.', linestyle="--", color="purple")
        self.ax.grid()

        self.canvas.draw()