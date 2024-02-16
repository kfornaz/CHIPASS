#!/usr/bin/env python
# coding: utf-8

import numpy as np
import healpy as hp
#import ConfigParser
from astropy.io import fits as pyfits
import matplotlib.pyplot as plt
import sys
import astropy as ap
from IPython.display import clear_output
import glob

maps = glob.glob('chisq_c0001_k*.fits') # Bins Karin .fits
maps.sort()

for i in range(len(maps)):
    chi2_maps = hp.mollview(hp.read_map(maps[i]), title="chisq_c0001_k0000"+str(i)+".fits",cmap="viridis", min=-10, max=10000000)
    plt.savefig("chisq_c0001_k0000"+str(i)+".png",  dpi=200, bbox_inches='tight', pad_inches=0.5)

