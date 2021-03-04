import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style

#Histogram -----------------------------------Catagorise Quantitative data by ranges

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()
