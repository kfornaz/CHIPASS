#!/usr/bin/env python
# coding: utf-8

# In[42]:


import numpy as np
import healpy as hp
#import ConfigParser
from astropy.io import fits as pyfits
import matplotlib.pyplot as plt
import sys
import astropy as ap
from IPython.display import clear_output
import glob


# In[59]:


maps = glob.glob('chisq_c0001_k*.fits') # Bins Karin .fits
maps.sort()


# In[101]:


for i in range(len(maps)):
    chi2_maps = hp.mollview(hp.read_map(maps[i]), title="chisq_c0001_k0000"+str(i)+".fits",cmap="viridis", min=-10, max=10000000)
    plt.savefig("chisq_c0001_k0000"+str(i)+".png",  dpi=500, bbox_inches='tight', pad_inches=0.5)


# In[67]:


maps_synch = glob.glob('synch_1.4-chipass_c0001_k000*.fits')
maps_synch.sort()


# In[124]:


for i in range(len(maps)):
    synch_maps = hp.mollview(hp.read_map(maps_synch[i]), title="synch_1.4-chipass_c0001_k000"+str(i)+".fits",cmap="viridis", min=-10, max=3000)
    plt.savefig("synch_1.4-chipass_c0001_k000"+str(i)+".png",  dpi=500, bbox_inches='tight', pad_inches=0.5)


# In[23]:


for i in range(len(maps)):
    synch_maps = hp.mollview(hp.read_map(maps_synch[i]), title="synch_1.4-chipass_c0001_k000"+str(i)+".fits",cmap="viridis", min=-10, max=3000, norm='hist')
    plt.savefig("synch_1.4-chipass_c0001_k000"+str(i)+"normHist.png",  dpi=500, bbox_inches='tight', pad_inches=0.5)

