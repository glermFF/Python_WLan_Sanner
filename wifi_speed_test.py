import pandas as pd
import speedtest as st
#import matplotlib as plot
import keyboard
import sched
import time

DELAY_TIME = int(3)
download = []
upload = []
ping = []

stest = st.Speedtest()
scheduler = sched.scheduler(time.time, time.sleep)

st_ping = stest.results.ping


def df_servers_list():
    servers_list = stest.get_servers()
    all_servers_list = pd.DataFrame(servers_list)
    return all_servers_list

def best_server():
    best = stest.get_best_server()

    print(f"Best server: {best['host']} | {best['country']}")

    scheduler.enter(DELAY_TIME, 0, best_server)

def connection_speed():
    '''Collect internet speed data'''
    temp_download = '{:.2f}'.format(stest.download() / 10 ** 6)
    temp_upload = '{:.2f}'.format(stest.upload() / 10 ** 6)

    download.append(temp_download)
    upload.append(temp_upload)
    ping.append(st_ping)

def df_connection_speed():
    connection_speed()
    data = {'Download': download, 'Upload': upload, 'Ping': ping}
    df_data = pd.DataFrame(data, columns=['Download(mbs)', 'Upload(mbs)', 'Ping(mbs)'])

    print(f"{df_data}")

    scheduler.enter(DELAY_TIME, 1, df_connection_speed)

best_server()
df_connection_speed()

try:
    scheduler.run(blocking=True)
    if keyboard.is_pressed('q') is True:    
        raise KeyboardInterrupt
    time.sleep(0.5)
except KeyboardInterrupt:
    print("Exiting program")