#!/usr/bin/env python

import prettyplotlib as ppl
import matplotlib.pyplot as plt
from matplotlib import rc
from prettyplotlib import brewer2mpl
import numpy as np
import math
import sys

fig = plt.figure(figsize=(9, 9), dpi=100)
plt.rc('text',color="0.3")

A = np.linspace(0,5,1000)
B = 1.0

minimum = np.minimum(A,B)
mean = (A+B)/2
geometric = np.sqrt(A*B)
harmonic = 2*A*B/(A+B)
maximum = np.maximum(A,B)

ppl.plot(A,mean,'-', label="p= 1: arithmetic", linewidth=1.75)
ppl.plot(A,geometric,'-', label="p= 0: geometric", linewidth=1.75)
ppl.plot(A,harmonic,'-', label="p=-1: harmonic", linewidth=1.75)
 
plt.tick_params(labelsize=20, labelcolor="0.3")
plt.xlabel("$T_B$", color="0.3", fontsize=25)
plt.ylabel("$M_p(T_A,T_B)$", color="0.3", fontsize=25)
plt.annotate('$T_A$ = 1', xy=(0.05, 0.9), xycoords='axes fraction',fontsize=25, color="0.3")

plt.legend(loc='lower right',fontsize=20, frameon=False, shadow=True)
plt.xlim([0,5.0])
plt.show()
