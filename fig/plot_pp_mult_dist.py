#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt

#define plot size in inches (width, height) & resolution(DPI)
fig = plt.figure(figsize=(5.5, 9), dpi=100)

# plot trento results
###########################################################################
seed, impact, npart, mult, ecc2, ecc3, area = np.loadtxt(sys.argv[1],unpack=True)
factor = 0.19
mult = np.asarray([i for i in (factor*mult).astype(int) if i >= 1])
bins = np.linspace(0.5,60.5,61)
plt.hist(mult,bins,normed=True,label="Trento pp 2.36 TeV",histtype='step',color='violet',linewidth=1.5)
print "Trento: ",mult.mean()

# plot ALICE pp NSD 2.36 TeV |eta| < 1.0
############################################################################################################################
x, xlow, xhigh, y, dyp1, dym1, dyp2, dym2 = np.loadtxt("ALICE-pp-multdist.dat",unpack=True,skiprows=10)
dx = xhigh-xlow
norm = np.inner(y,dx)
y = y/norm
xavg = np.inner(y,x)
print "ALICE NSD: ",xavg
plt.errorbar(x, y, fmt='o',color='teal',markeredgecolor = 'none', yerr=dyp1-dym1, label="ALICE pp 2.36 TeV NSD")
plt.legend(loc='lower left',fontsize=15,frameon=False)

# plot CMS pp NSD 2.36 TeV |eta| < 1.0
############################################################################################################################
x, xlow, xhigh, y, dyp1, dym1, dyp2, dym2 = np.loadtxt("CMS-pp-multdist.dat",unpack=True,skiprows=11)
dx = xhigh-xlow
norm = np.inner(y,dx)
y = y/norm
xavg = np.inner(y,x)
print "CMS NSD: ",xavg
plt.errorbar(x, y, fmt='o',color='purple',markeredgecolor = 'none', yerr=dyp1-dym1, label="CMS pp 2.36 TeV NSD")
plt.legend(loc='lower left',fontsize=15,frameon=False)

# plot properties
##############################################
print "factor:",factor
plt.yscale('log')
plt.xlim([0.0,55.0])
plt.ylim([0.0001,0.1])
plt.xlabel("$dNch/d\eta$",fontsize=15)
plt.ylabel("P($dNch/d\eta$)",fontsize=15)
plt.annotate('PRELIMINARY', xy=(0.5, 0.92), xycoords='axes fraction',fontsize=20,color='gray')
plt.title("pp Nch Distribution")
plt.show();
