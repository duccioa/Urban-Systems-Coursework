import powerlaw
import pandas as pd
import numpy as np
import scipy as sp
import numpy.linalg as npl
import scipy.stats as sps
import matplotlib.pyplot as plt
import patsy
import statsmodels.api as sm
import os
import matplotlib.pyplot as plt
import matplotlib
import math


###EXAMPLE###

data = np.random.exponential(1.2, 100)
 # data can be list or numpy array
results = powerlaw.Fit(data)
print results.power_law.alpha
print results.power_law.xmin
R, p = results.distribution_compare('power_law', 'lognormal')

plt.plot(range(0,100), np.random.exponential(1.2, 100))
plt.hist(np.random.exponential(0.4, 100000), 300)
plt.hist(math.log(np.random.exponential(0.4, 100000)), 300)