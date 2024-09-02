import pandas as pd
import speedtest as st
#import matplotlib as plot
import datetime
import time

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
    temp_download = '{:.2f}'.format(stest.download() / 10 ** 6)
    temp_upload = '{:.2f}'.format(stest.upload() / 10 ** 6)
    st_ping = '{:.2f}'.format(stest.results.ping)
    server = best_server()
    day = datetime.date.today()

    download.append(temp_download)
    upload.append(temp_upload)
    ping.append(st_ping)
    date.append(day)

    print(f"Download: {temp_download} Mbps, Upload: {temp_upload} Mbps, Ping: {st_ping} ms, Server: {server}, Data do teste: {day}")

def df_connection_speed():
    data = {'Download(mbs)': download, 'Upload(mbs)': upload, 'Ping(mbs)': ping, 'Date': date}
    df_data = pd.DataFrame(data)

    print(f"{df_data}")
