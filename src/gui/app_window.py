from customtkinter import *
from app.wifi_speed_test import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator
import numpy as np
import threading

ARRAY_INDEX = [1,2,3,4,5]

class AppWindow:

    def __init__(self) -> None:
        self.page = CTk()
        self.page.geometry("840x640")
        self.page.title("Wifi Speed Test")
        self.page.config(bg="#121421")

        self.page.rowconfigure(0, weight=1)
        self.page.columnconfigure(1, weight=1)

        fig = Figure(figsize=(4.0, 4.0), facecolor="#f5ffff")
        self.ax = fig.add_subplot()

        self.canvas = FigureCanvasTkAgg(fig)
        self.canvas.get_tk_widget().grid(row=0, column=1, padx=10, pady=10)

        self.side_frame = CTkFrame(self.page, fg_color="#f2f2f2", corner_radius=3, height=640, width=200)
        self.side_frame.grid(row=0, column=0, sticky="ns", padx=0, pady=0, ipadx=25)
        self.side_frame.rowconfigure(1, weight=1)
        self.side_frame.columnconfigure(0, weight=1)

        self.do_test = CTkButton(self.side_frame, text="Test", fg_color="#583B8A", width=100, corner_radius=5, command=self.start_test)
        self.do_test.grid(row=1, column=0, pady=(0, 250))

        self.clear_graph = CTkButton(self.side_frame, text="Clear", fg_color="#583B8A", width=100, corner_radius=5, command=self.clear)
        self.clear_graph.grid(row=1, column=0, pady=(0, 130))

        self.cancel_test = CTkButton(self.side_frame, text="Cancel", fg_color="#583B8A", width=100, corner_radius=5)
        self.cancel_test.grid(row=1, column=0, pady=(0, 0))

        self.save_graph = CTkButton(self.side_frame, text="Save Graph", fg_color="#583B8A", width=100, corner_radius=5)
        self.save_graph.grid(row=1, column=0, pady=(130, 0))

        self.loading_label = CTkLabel(self.page, text="", fg_color="transparent", bg_color="transparent")
        self.loading_label.grid(row=0, column=1, pady=(0, 0))

        self.page.mainloop()

    def start_test(self):
        self.loading_label.configure(text="Testing...")
        threading.Thread(target=self.show_graph).start()

    def clear(self):
        self.ax.clear()
        self.canvas.draw()

    def show_graph(self):
        connection_speed()
        data_frame = df_connection_speed()

        self.ax.clear()

        #Graph 1
        x = np.array(ARRAY_INDEX)
        x = data_frame.index
        y = data_frame["Download(mbs)"]


        self.ax.set_ylabel("Velociade(mbps)")
        self.ax.set_xlabel("Teste")

        self.ax.set_facecolor('#f5ffff')
        self.ax.fill_between(x=x, y1=y)
        self.ax.plot(x, y,  marker='.', linestyle="--", color="purple")
        self.ax.grid()

        self.ax.xaxis.set_major_locator(MaxNLocator(integer=True))

        self.canvas.draw()
        self.loading_label.configure(text="")