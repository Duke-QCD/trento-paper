#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy import integrate
from scipy.integrate import quad

#define plot size in inches (width, height) & resolution(DPI)
fig = plt.figure(figsize=(5.5, 9), dpi=100)

# plot Trento results
######################################################################################
seed, impact, npart, mult, ecc2, ecc3 = np.loadtxt(sys.argv[1],unpack=True,skiprows=1)
factor = 17.8
mult = np.asarray([i for i in (factor*mult) if i >= 19.82]) 
bins = np.linspace(19.82,3334.0,100)
plt.hist(mult,bins,normed=True,color='cyan',histtype='step',label="Trento: Pb-Pb @ 2.76 TeV",linewidth=1.5)
print "Trento:",mult.mean()

# plot ALICE PbPb exp data
######################################################################################
tmin, tmax, navg, prob, totprob = np.loadtxt("PbPb_Nch_2760_ALICE_2014.dat",unpack=True,skiprows=2)
widths = tmax - tmin
heights = prob/widths

# normalize exp data
nvec = np.linspace(19.82,3334,200)
fn = interp1d(navg, heights, kind='cubic')
norm = integrate.quad(fn, 19.82, 3334)[0]
plt.plot(nvec,fn(nvec)/norm,'r-')
mean = integrate.quad(lambda x: x*fn(x)/norm, 19.82, 3334.)[0]
plt.errorbar(navg,heights/norm,xerr=0.06*navg,yerr=0.01*heights,fmt='o',label="ALICE: Pb-Pb @ 2.76 TeV")
print "ALICE:",mean
 
# plot properties
################################################################################
print "factor:",factor
plt.xlim([0,3750])
#plt.ylim([1e-7,0.1])
plt.title("Pb-Pb Nch Distribution")
plt.legend(loc='lower left',fontsize=15,frameon=False)
plt.xlabel("$N_{ch}$",fontsize=15)
plt.ylabel("P($N_{ch}$)",fontsize=15)
plt.annotate('PRELIMINARY', xy=(0.5, 0.92), xycoords='axes fraction',fontsize=20,color='gray')
plt.yscale('log')
plt.show()
