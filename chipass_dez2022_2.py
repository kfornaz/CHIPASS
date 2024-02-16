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


maps_res = glob.glob('res_1.4-chipass_c0001_k0000*.fits') # Bins Karin .fits
maps_res.sort()


# In[101]:


for i in range(len(maps_res)):
    res_maps = hp.mollview(hp.read_map(maps_res[i]), title="res_1.4-chipass_c0001_k0000"+str(i)+".fits",cmap="viridis", min=0, max=60)
    plt.savefig("res_1.4-chipass_c0001_k0000"+str(i)+".png",  dpi=500, bbox_inches='tight', pad_inches=0.5)


# In[67]:


maps_synch = glob.glob('synch_1.4-chipass_c0001_k000*.fits')
maps_synch.sort()


# In[124]:


for i in range(len(maps)):
    synch_maps = hp.mollview(hp.read_map(maps_synch[i]), title="synch_1.4-chipass_c0001_k000"+str(i)+".fits",cmap="viridis", min=-10, max=3000)
    plt.savefig("synch_1.4-chipass_c0001_k000"+str(i)+".png",  dpi=500, bbox_inches='tight', pad_inches=0.5)


# In[137]:


chi2_maps =hp.read_map("res_1.4-chipass_c0001_k000006.fits")
hp.mollview(chi2_maps, min=0, max=60)


# In[ ]:




