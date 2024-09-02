import app.wifi_speed_test

while True:
    try:
        app.connection_speed()
    except KeyboardInterrupt:
        print("Dados finais coletados")
        app.df_connection_speed()
        break