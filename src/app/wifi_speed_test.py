import pandas as pd
import speedtest as st
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
    try:
        while x < 5:
            temp_download = '{:.2f}'.format(stest.download() / 10 ** 6)
            temp_upload = '{:.2f}'.format(stest.upload() / 10 ** 6)
            st_ping = '{:.2f}'.format(stest.results.ping)
            day = datetime.date.today()

            download.append(temp_download)
            upload.append(temp_upload)
            ping.append(st_ping)
            date.append(day)

            x += 1
    except Exception:
        print("Aborting test")

    finally:
        return 0

def df_connection_speed():
    data = {'Download(mbs) ': download, ' Upload(mbs) ': upload, ' Ping(mbs) ': ping, ' Date ': date}
    df_data = pd.DataFrame(data)

    return df_data