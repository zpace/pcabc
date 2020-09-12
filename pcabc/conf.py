import numpy as np
import pandas as pd
import dask.dataframe as ddf
import dask.array as da

from fastcore.utils import store_attr
import os.path
from os import environ

from pcabc import __version__

# environment variables govern directory structure
BASEDIR = os.path.abspath(environ.get('MaNGAPCA_BASE', default='.'))
CSP_BASEDIR = environ.get(
    'MaNGAPCA_CSPBASE', os.path.join(BASEDIR, 'CSPs'))
FAKEDATA_BASEDIR = os.path.join(BASEDIR, 'results_fakedata')
RESULTS_BASEDIR = os.path.join(BASEDIR, 'results')