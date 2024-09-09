import pandas as pd
import speedtest as st
#import matplotlib.pyplot as plot
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#import numpy as np
import datetime

download = []
upload = []
ping = []
date = []

stest = st.Speedtest()

def best_server():
    best = stest.get_best_server()

    return f"{best['host']} | {best['country']}"

def connection_speed():
    '''Collect internet speed data'''

    x = 0
    while x < 5:
        temp_download = '{:.2f}'.format(stest.download() / 10 ** 6)
        temp_upload = '{:.2f}'.format(stest.upload() / 10 ** 6)
        st_ping = '{:.2f}'.format(stest.results.ping)
        #server = best_server()
        day = datetime.date.today()

        download.append(temp_download)
        upload.append(temp_upload)
        ping.append(st_ping)
        date.append(day)

        x += 1

    print("done")

    #print(f"Download: {temp_download} Mbps, Upload: {temp_upload} Mbps, Ping: {st_ping} ms, Server: {server}, Data do teste: {day}")

def df_connection_speed():
    data = {'Download(mbs)': download, 'Upload(mbs)': upload, 'Ping(mbs)': ping, 'Date': date}
    df_data = pd.DataFrame(data)

    return df_data