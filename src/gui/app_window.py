from customtkinter import *
from PIL import Image
from app.wifi_speed_test import *
from app.wlan_info import *
from time import sleep
import threading
import os

file_path = "resources" 

class AppWindow:

    def __init__(self) -> None:
        self.page = CTk()
        self.page.geometry("840x640")
        self.page.title("Swosh Scan")
        self.page.resizable(width=False, height=False)
        self.page.config(bg="#121421")

        get_wlan_info()
        self.i_info = result["Interface"]
        self.i_ip = result["IP"]
        self.i_mac = result["MAC"]

        #Images
        self.speed_test_image = CTkImage(dark_image=Image.open('resources/images/control_panel.png'), size=(50, 50))
        self.scan_image = CTkImage(dark_image=Image.open('resources/images/connection_search.png'), size=(50, 50))
        self.device_image = CTkImage(dark_image=Image.open('resources/images/router_signal.png'), size=(50, 50))

        #Frames
        self.side_frame = CTkFrame(master=self.page, fg_color="#f2f2f2", border_width=5, width=125)
        self.side_frame.pack(side="left", fill="y")

        self.status_info = CTkFrame(self.page, fg_color="#f2f2f2", border_width=5, width=300 , height=300)
        self.status_info.pack(pady=100, padx=100)

        self.actions = CTkFrame(self.page, fg_color="#000000", border_width=5)
        self.actions.pack(side="bottom")

        #Buttons
        
        ##Side 
        self.speed_test = CTkButton(self.side_frame, text="",image=self.speed_test_image, fg_color="transparent", width=75, height=75, corner_radius=5,border_width=3)
        self.speed_test.pack(padx=30, pady=20)

        self.scan = CTkButton(self.side_frame, text="", image=self.scan_image, fg_color="transparent", width=75, height=75, corner_radius=5,border_width=3)
        self.scan.pack(padx=30, pady=20)

        self.device = CTkButton(self.side_frame, text="", image=self.device_image, fg_color="transparent", width=75, height=75, corner_radius=5,border_width=3)
        self.device.pack(padx=30, pady=20)

        ##Actions
        button_1 = CTkButton(self.actions, text="Test", fg_color="#583B8A", width=100, height=50, corner_radius=5,border_width=3, command=self.test_clicked)
        button_1.pack(side="left", padx=30, pady=20)
        
        self.save_data = CTkButton(self.actions, text="Save Data", fg_color="#583B8A", width=100, height=50, corner_radius=5, state="disabled", border_width=3, command=self.save_data_in_archive)
        self.save_data.pack(side="left", padx=30, pady=20)

        button_2 = CTkButton(self.actions, text="Cancel", fg_color="#583B8A", width=100, height=50, corner_radius=5, state="disabled", border_width=3, command=self.cancel_execution)
        button_2.pack(side="left", padx=30, pady=20)        

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