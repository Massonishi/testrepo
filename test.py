# -*- coding: utf-8 -*-


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