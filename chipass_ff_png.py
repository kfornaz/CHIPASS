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

maps_ff = glob.glob('ff_1.4-chipass_c0001_k*.fits')
maps_ff.sort()

for i in range(len(maps_ff)):
    ff_maps = hp.mollview(hp.read_map(maps_ff[i]), title="ff_1.4-chipass_k0000"+str(i)+".fits",cmap="jet", min=0, max=5000)
    plt.savefig("ff_1.4-chipass_k0000"+str(i)+".png",  dpi=200, bbox_inches='tight', pad_inches=0.5)







