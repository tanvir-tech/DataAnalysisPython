# little design
from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")                                     # using style

#plot info
x = [1,2,3,4,5]
y = [2,4,5,6,10]
plt.plot(x,y,"g",label="First line",linewidth=5)        #  x,y, color, label-of-line, linewidth

#graph info
plt.title("Basic Graph")
plt.xlabel(x)
plt.ylabel(y)

plt.legend()
plt.grid(True, color="r")

plt.show()
