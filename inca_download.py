from urllib.request import urlretrieve
import os

url = "https://public.hub.geosphere.at/datahub/resources/inca-v1-1h-1km/filelisting/RR/INCAL_HOURLY_RR_202506.nc"
filename = os.path.basename(url)
base = "/tmp"
urlretrieve(url, os.path.join(base,filename))
                              


