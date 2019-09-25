from osgeo import gdal
import urllib.request

# download data
url = 'https://swatshare.rcac.purdue.edu/temp/MOD16A2.A2014001.h11v04.105.2015034134036.hdf'
filename = 'data.hdf'
urllib.request.urlretrieve(url, filename)

# Read the downloaded hdf file
hdf = gdal.Open(filename, gdal.GA_ReadOnly)

# Print Metadata
print(hdf.GetMetadata())