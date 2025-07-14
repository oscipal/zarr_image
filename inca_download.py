from urllib.request import urlretrieve
import os
import sys

def download_data(var):
    url = f"https://public.hub.geosphere.at/datahub/resources/inca-v1-1h-1km/filelisting/{var}/INCAL_HOURLY_{var}_202506.nc"
    filename = os.path.basename(url)
    base = "/tmp"
    urlretrieve(url, os.path.join(base,filename))
    print(var)
                              
if __name__ == "__main__":
    var = sys.argv[1]
    download_data(var)

