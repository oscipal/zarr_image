import xarray as xr
import numpy as np
import zarr

def get_idx(array1, array2):
    min = np.where(array1==array2[0])[0][0]
    max = np.where(array1==array2[-1])[0][0]+1
    return min, max

filename = "INCAL_HOURLY_RR_202506.nc"
artifact_path = os.path.join("/tmp", filename)
nfs_path = "/eodc/private/openeo_platform/zarr_nacho"

data = xr.open_dataset(f"/eodc/private/openeo_platform/zarr_nacho/{filename}", mask_and_scale=False).load()

store = zarr.storage.LocalStore("/eodc/private/openeo_platform/zarr_nacho/INCA_test.zarr")
group = zarr.group(store=store)
x_extent = group["x"][:]
y_extent = group["y"][:]

x_min, x_max = get_idx(x_extent, data["x"].values)
y_min, y_max = get_idx(y_extent, data["y"].values)

origin = np.datetime64("2011-03-15T00:00:00").astype("datetime64[h]")
time_min, time_max = data.time.values[0].astype("datetime64[h]"), data.time.values[-1].astype("datetime64[h]")+1
time_delta_min, time_delta_max = (time_min - origin).astype("int64"), (time_max - origin).astype("int64")

group["RR"][time_delta_min:time_delta_max, y_min:y_max, x_min:x_max] = data["RR"].values