import os
import tarfile
from six.moves import urllib

HOUSING_TGZ = "housing.tgz"

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets/housing"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "/" + HOUSING_TGZ


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, HOUSING_TGZ)
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

if not os.path.exists(os.path.join(HOUSING_PATH, HOUSING_TGZ)):
    print("downloading housing data")
    fetch_housing_data()
else:
    print("housing data is already there")

