"""tab.py includes facilities for handling CSP data tables
"""

from conf import *

from dask import delayed
from astropy.io import fits
from astropy import table as t

from glob import glob

class CSPSet(object):
    def __init__(self, dataframe, specs, lam):
        """Continuous stellar pop data, including spectra, wavelengths, and other data

        Parameters:
        -----------
        dataframe : `dask.DataFrame`
            dataframe with CSP properties
        specs : `dask.array`
            array with CSP spectra
        lam : `dask.array`
            array with wavelengths of CSP spectra
        """
        store_attr()

    @classmethod
    def from_CSPdir(cls, cspdir=CSP_BASEDIR, cspglob='CSPs_??.fits'):
        """read in CSP data from files
        
        Parameters:
        -----------
        cspdir : str
            directory to look in
        cspglob : str
            pattern to match in filenames
        """

        cspdata = [delayed(read_CSP_data)(fn)
                   for fn in glob(os.path.join(cspdir, cspglob))]
        dfs, specs, ls = zip(*cspdata)

        df = ddf.from_delayed(dfs)
        specs = da.stack([da.from_delayed])

        return cls(dataframe=df, specs=sp, lam=ls[0])

    @staticmethod
    def read_CSP_data(fname, cspname='meta', specname='flam', lname='lam'):
        """read in CSP data from single file

        Parameters
        ----------
        fname : str
            file name
        cspname : str
            extension name for CSP table
        specname : str
            extension name for spectra
        lname : str
            extension name for lam
        """
        
        with fits.open(fname) as hdulist:
            df = t.Table(hdulist[cspname].data).to_pandas()
            specs = hdulist[specname].data
            l = hdulist[lname].data

        return df, specs, l
