from customtkinter import *
from app.wifi_speed_test import *
from app.wlan_info import *
import threading
import os
from time import sleep

file_path = "resources" 

class AppWindow:

    def __init__(self) -> None:
        self.page = CTk()
        self.page.geometry("840x640")
        self.page.title("Wifi Speed Test")
        self.page.config(bg="#121421")

        self.page.rowconfigure(0, weight=1)
        self.page.columnconfigure(1, weight=1)

        get_wlan_info()
        self.i_info = result["Interface"]
        self.i_ip = result["IP"]
        self.i_mac = result["MAC"]
        
        # Side Frame
        self.side_frame = CTkFrame(self.page, fg_color="#f2f2f2", corner_radius=3, height=640, width=200)
        self.side_frame.grid(row=0, column=0, sticky="ns", padx=0, pady=0, ipadx=25)
        self.side_frame.rowconfigure(1, weight=1)
        self.side_frame.columnconfigure(0, weight=1)

        self.do_test = CTkButton(self.side_frame, text="Test", fg_color="#583B8A", width=100, corner_radius=5, command=self.test_clicked)
        self.do_test.grid(row=1, column=0, pady=(0, 150))

        self.cancel_test = CTkButton(self.side_frame, text="Cancel", state="disabled",fg_color="#583B8A", width=100, corner_radius=5, command=self.cancel_execution)
        self.cancel_test.grid(row=1, column=0, pady=(0, 0))

        self.save_data = CTkButton(self.side_frame, text="Save Data", state="disabled",fg_color="#583B8A", width=100, corner_radius=5, command=self.save_data_in_archive)
        self.save_data.grid(row=1, column=0, pady=(150, 0))

        # Interface Info Label
        self.device_info = CTkFrame(self.page, corner_radius=3, fg_color="#583B8A", bg_color="transparent")
        self.device_info.grid(row=0, column=1, pady=(0, 250), padx=(0, 410), sticky="ns")

        self.text = CTkLabel(self.device_info, text="Wlan Interface", font=("Arial", 24))
        self.text.grid(padx=50 , pady=10)

        self.info = CTkLabel(self.device_info, text=f"Interface: {self.i_info}", font=("Arial", 12))
        self.info.grid(padx=50, pady=10)

        self.info = CTkLabel(self.device_info, text=f"Ip (actual network): {self.i_ip}", font=("Arial", 12))
        self.info.grid(padx=50, pady=10)

        self.info = CTkLabel(self.device_info, text=f"Mac: {self.i_mac}", font=("Arial", 12))
        self.info.grid(padx=50, pady=10)

        # Terminal Label
        self.terminal_frame = CTkFrame(self.page, fg_color="#000000", corner_radius=3)
        self.terminal_frame.grid(row=0, column=1, padx=30, pady=(465, 10), sticky="ns", ipadx=600)

        self.loading_label = CTkLabel(self.terminal_frame, text="", corner_radius=3, bg_color="transparent")
        self.loading_label.grid(padx=5, pady=5)

        self.page.mainloop()

    def test_clicked(self):
        self.loading_label.configure(text="Running Test...")
        self.cancel_test.configure(state="normal")
        try:
            threading.Thread(target=self.start_test).start()
        except KeyboardInterrupt:
            self.loading_label.configure(text="Test Cancelled")
            self.cancel_test.configure(state="disabled")

    def start_test(self):
        connection_speed()
        self.loading_label.configure(text="Test Completed")
        sleep(3)
        self.save_data.configure(state="normal")
        data_collected = df_connection_speed()
        self.loading_label.configure(text=data_collected)

    def cancel_execution(self):
        raise KeyboardInterrupt("Cancelling test")

    def save_data_in_archive(self):
        folder_path = os.path.join(file_path, f"wifi_speed_test_{date}.csv")
        data = df_connection_speed()
        data.to_csv(folder_path, index=False)