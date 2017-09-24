# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 12:01:48 2017

@author: MassOnishi
"""
import numpy as np
import pprint
from matplotlib import pyplot as plt

x = []
x2 = []
y = []
a = 2
counter = 0

for i in range(30):   
    counter = i
    multi = a**i
    x.append(counter)
    x2.append(counter)
    y.append(multi)

pprint.pprint("x : " + str(x[:30]) + "y : " + str(y[:30]))

    
exy = [np.exp(i) for i in range(30)]
#pprint.pprint(exy)

plt.plot(x, y, label = "multiY")
plt.plot(x2, exy, label = "expY")
plt.legend()
plt.show()