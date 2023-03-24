import numpy as np
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#data = np.random.random(size=(3, 3, 3))
#z, x, y = data.nonzero()
M = np.array([10,30,50,         10,30,50,70,      10,30,50,70,10,30,50,70])
w_m=np.array([80.63,78.54,77.49,61.78,59.69,58.64,57.60,41.89,39.79,38.75,37.70,18.85,16.76,14.66,13.61])
n = np.array([67.20,79.87,82.79,64.36,62.70,80.16,78.32,62.33,73.69,79.72,74.04,67.32,69.92,60.28,58.32])

plt.title('\u03B7=f(M,\u03C9)')
plt.xlabel('\u03C9')
plt.ylabel('M')
ax.set_zlabel('\u03B7') #plt.zlabel('\u03B7	')
#ax.scatter(w_m, M, n, c=n, alpha=1)
#ax.plot_surface(w_m, M, n, cmap ='viridis', edgecolor ='green')
#ax.plot3D(w_m, M, n, 'green')
ax.plot_trisurf(w_m, M, n, color='pink')
plt.show()