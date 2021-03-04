from matplotlib import pyplot as plt
from matplotlib import style

#scatter plot --------------------------Co-relation
x = [1,2,3,4,5]
y = [2,4,5,6,10]
plt.scatter(x,y)        #  x,y, color

#graph info
plt.title("scatter Graph")
plt.xlabel(x)
plt.ylabel(y)
plt.legend()

plt.show()
