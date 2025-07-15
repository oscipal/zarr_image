import xarray as xr
import numpy as np
import zarr
import os
import sys

def write_data(var):
    artifact_path = f"/tmp/INCAL_HOURLY_{var}_{ym}.nc"  # adjust if needed

    def get_idx(array1, array2):
        min = np.where(array1==array2[0])[0][0]
        max = np.where(array1==array2[-1])[0][0]+1
        return min, max

    nfs_path = "/eodc/private/openeo_platform/zarr_nacho"

    data = xr.open_dataset(artifact_path, mask_and_scale=False).load()

    store = zarr.storage.LocalStore("/eodc/private/openeo_platform/zarr_nacho/INCA_test.zarr")
    group = zarr.group(store=store)
    x_extent = group["x"][:]
    y_extent = group["y"][:]

    x_min, x_max = get_idx(x_extent, data["x"].values)
    y_min, y_max = get_idx(y_extent, data["y"].values)

    origin = np.datetime64("2011-03-15T00:00:00").astype("datetime64[h]")
    time_min, time_max = data.time.values[0].astype("datetime64[h]"), data.time.values[-1].astype("datetime64[h]")+1
    time_delta_min, time_delta_max = (time_min - origin).astype("int64"), (time_max - origin).astype("int64")

    group[var][time_delta_min:time_delta_max, y_min:y_max, x_min:x_max] = data[var].values

if __name__=="__main__":
    var = sys.argv[1]
    ym = sys.arv[2]
    write_data(var, ym)
    