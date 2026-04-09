import xarray as xr
import numpy as np
import pandas as pd

path = "/glade/work/kumar34/GSEI2070_DAT/gistemp1200_GHCNv4_ERSSTv5.nc"

ds = xr.open_dataset(path)

print("=" * 60)
print("GISTEMP v4 – Surface Temperature Analysis Dataset Exploration")
print("=" * 60)

print("\n[Dataset Overview]")
print(ds)

print("\n[Dimensions]")
for dim, size in ds.dims.items():
    print(f"  {dim}: {size}")

print("\n[Variables]")
for var in ds.data_vars:
    print(f"  Variable name : {var}")
    print(f"  Long name     : {ds[var].attrs.get('long_name', 'N/A')}")
    print(f"  Units         : {ds[var].attrs.get('units', 'N/A')}")

print("\n[Spatial Resolution]")
lat = ds["lat"].values
lon = ds["lon"].values
lat_res = round(float(np.diff(lat).mean()), 4)
lon_res = round(float(np.diff(lon).mean()), 4)
print(f"  Latitude  resolution : {lat_res}°")
print(f"  Longitude resolution : {lon_res}°")
print(f"  Lat range : {lat.min():.2f}° to {lat.max():.2f}°")
print(f"  Lon range : {lon.min():.2f}° to {lon.max():.2f}°")

print("\n[Institution]")
print(f"  {ds.attrs.get('institution', 'See global attributes below')}")
print(f"  Title     : {ds.attrs.get('title', 'N/A')}")
print(f"  References: {ds.attrs.get('references', 'N/A')}")

print("\n[Time Information]")
time = ds["time"]
print(f"  Total time steps : {len(time)}")
print(f"  Start date       : {str(time.values[0])[:10]}")
print(f"  End date         : {str(time.values[-1])[:10]}")

t0 = pd.Timestamp(str(time.values[0]))
t1 = pd.Timestamp(str(time.values[1]))
delta_days = (t1 - t0).days
if delta_days <= 1:
    res_label = "Daily"
elif delta_days <= 31:
    res_label = "Monthly"
else:
    res_label = "Other"
print(f"  Time resolution  : {res_label} (~{delta_days} day(s) between steps)")

start_year = t0.year
end_year   = pd.Timestamp(str(time.values[-1])).year
print(f"  Start year       : {start_year}")
print(f"  End year         : {end_year}")
print(f"  Total years      : {end_year - start_year + 1}")

print("\n[All Global Attributes]")
for key, val in ds.attrs.items():
    print(f"  {key}: {val}")
 
print("\n[Done – GISTEMP Analysis Complete]")
ds.close()

