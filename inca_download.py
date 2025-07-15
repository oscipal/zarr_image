from urllib.request import urlretrieve
import os
import sys

def download_data(var):
    print(var)
    url = f"https://public.hub.geosphere.at/datahub/resources/inca-v1-1h-1km/filelisting/{var}/INCAL_HOURLY_{var}_{ym}.nc"
    filename = os.path.basename(url)
    base = "/tmp"
    urlretrieve(url, os.path.join(base,filename))
    
                              
if __name__ == "__main__":
    var = sys.argv[1]
    ym = sys.argv[2]
    download_data(var, ym)

