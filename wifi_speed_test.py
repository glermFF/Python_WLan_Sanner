import pandas as pd
import sched
import speedtest as st
import time

DELAY_TIME = int(15)

stest = st.Speedtest()
scheduler = sched.scheduler()

st_download = stest.download()
st_upload = stest.upload()
st_ping = stest.results.ping
stest.get_best_server()

def df_all_results():
    all_results = stest.results.dict()
    all_results_pd = pd.DataFrame(all_results)
    return all_results_pd

def speed_test():
    df_results = {'Download': st_download, 'Upload': st_upload, 'Ping': st_ping}
    df_frame = pd.DataFrame(df_results, columns=['Download', 'Upload', 'Ping'])
def download_speed_test():
    df_download = df_all_results()
    df_download = df_download['download']
    for x in df_download.index:
        df_download.loc[x] = 10 ** 6
    return df_download

df_all_results()