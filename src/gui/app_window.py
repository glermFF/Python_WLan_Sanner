from customtkinter import *
from PIL import Image
from app.wlan_info import *
from time import sleep
import threading
import socket
import os

file_path = "resources" 

class AppWindow:

    def __init__(self) -> None:
        self.page = CTk()
        self.page.title("Python Scanner")
        self.page.geometry("840x640")

        self.page.resizable(width=False, height=False)
        self.page.config(bg="#121421")

        get_wlan_info()
        self.i_info = result["Interface"]
        self.i_ip = result["IP"]
        self.i_mac = result["MAC"]

        # Sidebar
        self.sidebar = CTkFrame(self.page, width=240)
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)

        self.label = CTkLabel(self.sidebar, text="Tools Guide", font=CTkFont(size=18, weight="bold")).pack(pady=10)

        self.btn_host = CTkButton(self.sidebar, text="Host Discovery")
        self.btn_sniff = CTkButton(self.sidebar, text="Sniffing")
        self.btn_ports = CTkButton(self.sidebar, text="Port Analyses")

        self.btn_host.pack(pady=5, fill="x")
        self.btn_sniff.pack(pady=5, fill="x")
        self.btn_ports.pack(pady=5, fill="x")

        # Main
        self.main_area = CTkFrame(self.page)
        self.main_area.pack(side="left", fill="both", expand=True, padx=10, pady=15)

        self.content_frame = CTkFrame(self.main_area)
        self.content_frame.pack(fill="both", expand=True)

        ## Commands
        self.commands = CTkTextbox(self.content_frame, wrap="word")
        self.commands.pack(side="top", fill="x", padx=10, pady=(10, 0))

        self.commands.bind("<Return>", self.handle_enter)
        self.commands.bind("<BackSpace>", self.handle_backspace)
        self.commands.bind("<Key>", self.prevent_editing_above)

        self.terminal_index = "[Commands]: "
        self.insert_prompt()

        ## Logs
        self.logs = CTkTextbox(self.main_area, height=150)
        self.logs.pack(fill="x", padx=10, pady=(5, 5))
        self.logs.insert("end", "[Logs]: \n")

        self.page.mainloop()

    # Integrated Terminal
    def insert_prompt(self):
        self.commands.insert("end", self.terminal_index)
        self.commands.mark_set("insert", "end")
        self.commands.see("end")


    def handle_backspace(self, event):
        index = self.commands.index("insert")
        line, col = map(int, index.split('.'))
        if col <= len(self.terminal_index) and self.commands.get(f"{line}.0", f"{line}.end").startswith(self.terminal_index):
            return "break"
        return None
    
    def handle_enter(self, event):
        index = self.commands.index("insert")
        line_num = index.split('.')[0]
        line_start = f"{line_num}.0"
        line_text = self.commands.get(line_start, 'end-1c')

        if line_text.startswith(self.terminal_index): # Get only what the user typed
            command = line_text[len(self.terminal_index):].strip()
        else:
            command = line_text.strip()

        if command:
            output = self.run_command(command)
            self.commands.insert("end", "\n" + output +"\n")
        else: # If nothing was typed, insert a new prompt line
            self.commands.insert("end", "\n")

        self.insert_prompt() # Add a new line in the terminal
        return "break"

    def prevent_editing_above(self, event):
        if event.keysym in ["Up", "Down", "Left"]:
            return "break"

    # Functionalities
    def run_command(self, command):
        if command == "clean":
            return "limpando"
        
        elif command.startswith("scan"):
            args = command.split()
            if len(args) == 2:
                target_ip = args[1]
                return self.scan_host(target_ip)
            else:
                return "correct syntax: scan <target_ip>"
            
        elif command == "quit":
            self.page.quit()

        return f"{command} it's not valid"

    def scan_host(self, target_ip, ports=None):
        if ports is None:
            ports = [22, 80]

        for port in ports:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    if s.connect_ex((target_ip, port)) == 0:
                        return f"{port} open"
                    else:
                        return f"{port} closed"
                    
            except Exception as e:
                return f"Error on port{port}: {str(e)}"

        return "\n Scan finalizado"

    def test_clicked(self):
        self.loading_label.configure(text="Running Test...")
        self.cancel_test.configure(state="normal")
        try:
            threading.Thread(target=self.start_test).start()
        except KeyboardInterrupt:
            self.loading_label.configure(text="Test Cancelled")
            self.cancel_test.configure(state="disabled")
"""

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
"""

"""

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
        
        self.save_data = CTkButton(self.actions, text="Save Data", fg_color="#583B8A", width=100, height=50, corner_radius=5, state="disabled", border_width=3, command="")
        self.save_data.pack(side="left", padx=30, pady=20)

        button_2 = CTkButton(self.actions, text="Cancel", fg_color="#583B8A", width=100, height=50, corner_radius=5, state="disabled", border_width=3, command="")
        button_2.pack(side="left", padx=30, pady=20)        


        #Images
        self.speed_test_image = CTkImage(dark_image=Image.open('resources/images/control_panel.png'), size=(50, 50))
        self.scan_image = CTkImage(dark_image=Image.open('resources/images/connection_search.png'), size=(50, 50))
        self.device_image = CTkImage(dark_image=Image.open('resources/images/router_signal.png'), size=(50, 50))
"""