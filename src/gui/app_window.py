from customtkinter import *
from app.wifi_speed_test import *
import threading
import os
from time import sleep
from queue import Queue

file_path = "resources" 

class AppWindow:

    def __init__(self) -> None:
        self.page = CTk()
        self.page.geometry("840x640")
        self.page.title("Wifi Speed Test")
        self.page.config(bg="#121421")

        self.page.rowconfigure(0, weight=1)
        self.page.columnconfigure(1, weight=1)

        self.queue = Queue()

        # Side Frame
        self.side_frame = CTkFrame(self.page, fg_color="#f2f2f2", corner_radius=3, height=640, width=200)
        self.side_frame.grid(row=0, column=0, sticky="ns", padx=0, pady=0, ipadx=25)
        self.side_frame.rowconfigure(1, weight=1)
        self.side_frame.columnconfigure(0, weight=1)

        self.do_test = CTkButton(self.side_frame, text="Test", fg_color="#583B8A", width=100, corner_radius=5, command=self.test_clicked)
        self.do_test.grid(row=1, column=0, pady=(0, 150))

        self.cancel_test = CTkButton(self.side_frame, text="Cancel", fg_color="#583B8A", width=100, corner_radius=5, command=self.cancel_execution)
        self.cancel_test.grid(row=1, column=0, pady=(0, 0))

        self.save_data = CTkButton(self.side_frame, text="Save Data", fg_color="#583B8A", width=100, corner_radius=5, command=self.save_data_in_archive)
        self.save_data.grid(row=1, column=0, pady=(150, 0))

        # Device Info Label
        self.device_info = CTkLabel(self.page, text=None, corner_radius=3, fg_color="#583B8A", bg_color="transparent", width=300, height=400)
        self.device_info.grid(row=0, column=1, pady=(0, 150), padx=(0, 285))

        self.text = CTkLabel(self.device_info, text="Board Info", font=("Arial", 24))
        self.text.grid(row=0, column=0, pady=(0, 350))

        # Terminal Label
        self.terminal_label = CTkLabel(self.page, text=None, corner_radius=3, fg_color="black", bg_color="transparent", width=600, height=150)
        self.terminal_label.grid(row=0, column=1, pady=(450, 0))

        self.loading_label = CTkLabel(self.terminal_label, text="", corner_radius=3, bg_color="transparent")
        self.loading_label.grid(row=0, column=0)

        self.page.mainloop()

    def test_clicked(self):
        self.loading_label.configure(text="Running Test...")
        threading.Thread(target=self.start_test).start()

    def start_test(self):
        connection_speed()
        self.loading_label.configure(text="Test Completed")
        sleep(3)
        data_collected = df_connection_speed()
        self.loading_label.configure(text=data_collected)

    def cancel_execution(self):
        raise KeyboardInterrupt("Cancelling test")

    def save_data_in_archive(self):
        folder_path = os.path.join(file_path, f"wifi_speed_test_{date}.csv")
        data = df_connection_speed()
        data.to_csv(folder_path, index=False)