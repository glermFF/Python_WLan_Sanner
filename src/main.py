from gui.app_window import main_page
import app.wifi_speed_test
import flet 


while True:
    try:
        app.connection_speed()
    except KeyboardInterrupt:
        print("Dados finais coletados")
        app.df_connection_speed()
        break