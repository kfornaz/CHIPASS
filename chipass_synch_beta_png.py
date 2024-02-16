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

maps_synch = glob.glob('synch_beta_c0001_k*.fits')
maps_synch.sort()

for i in range(len(maps_synch)):
    synch_maps = hp.mollview(hp.read_map(maps_synch[i]), title="synch_beta_c0001_k0000"+str(i)+".fits",cmap="viridis", min=-10, max=10)
    plt.savefig("synch_beta_c0001_k0000"+str(i)+".png",  dpi=200, bbox_inches='tight', pad_inches=0.5)







