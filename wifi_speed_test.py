import pandas as pd
import sched
import speedtest as st
import time

DELAY_TIME = int(1)
download = []
upload = []
ping = []

stest = st.Speedtest()
scheduler = sched.scheduler(time.time, time.sleep)

st_download = stest.download()
st_upload = stest.upload()
st_ping = stest.results.ping
stest.get_best_server()

#! FUNÇÃO PARA USAR NOS TESTES
def df_all_results():
    all_results = stest.results.dict()
    all_results_pd = pd.DataFrame(all_results)
    return all_results_pd

def connection_speed():
    '''Collect internet speed data'''
    temp_download = '{:.2f}'.format(stest.download() / 10 ** 6)
    temp_upload = '{:.2f}'.format(stest.upload() / 10 ** 6)

    download.append(temp_download)
    upload.append(temp_upload)
    ping.append(st_ping)

    print(f"Next test will execute in {DELAY_TIME}.")

    scheduler.enter(DELAY_TIME, 0, connection_speed)

def df_connection_speed():
    data = {'Download': download, 'Upload': upload, 'Ping': ping}
    df_data = pd.DataFrame(data, columns=['Download', 'Upload', 'Ping'])

    scheduler.enter(DELAY_TIME, 1, df_connection_speed)

    return df_data


connection_speed()
#print(df_all_results())
print(df_connection_speed())