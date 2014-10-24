#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy import integrate
from scipy.integrate import quad

#define plot size in inches (width, height) & resolution(DPI)
fig = plt.figure(figsize=(6, 6), dpi=100)

# plot Trento results
######################################################################################
seed, impact, npart, mult, ecc2, ecc3, area = np.loadtxt(sys.argv[1],unpack=True,skiprows=1)
factor = 18.5
mult = np.asarray([i for i in (factor*mult).astype(int) if i >= 12])
bins = np.linspace(12,180,169)
plt.hist(mult,bins,normed=True,color='cyan',histtype='step',label="Trento: pPb @ 5.02 TeV",linewidth=1.5)
print "Trento:",mult.mean()

# plot ALICE pPb exp data
######################################################################################
tmin, tmax, navg, prob, totprob = np.loadtxt("ALICE-pPb.dat",unpack=True,skiprows=2)
widths = tmax-tmin
heights = prob/widths

# normalize exp data
nvec = np.linspace(12.0,186.0,175)
fn = interp1d(navg, heights, kind='cubic')
norm = integrate.quad(fn, 12.0, 186.)[0]
mean = integrate.quad(lambda x: x*fn(x)/norm, 12., 186.)[0]
plt.errorbar(navg,heights/norm,xerr=0.06*navg,yerr=0.035*heights,fmt='o',label="ALICE: pPb @ 5.02 TeV")
print "ALICE:",mean
 
# plot properties
#########################################################################################
print "factor:",factor
plt.xlim([0,200])
plt.ylim([1e-7,0.1])
plt.title("pPb Nch Distribution")
plt.legend(loc='lower left',fontsize=15,frameon=False)
plt.xlabel("$N_{ch}$",fontsize=15)
plt.ylabel("P($N_{ch}$)",fontsize=15)
plt.annotate('PRELIMINARY', xy=(0.5, 0.92), xycoords='axes fraction',fontsize=20,color='gray')
plt.yscale('log')
plt.savefig("pPb.pdf")
plt.show()
