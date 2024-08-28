import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

# Measurements for n1024
#M               = np.array([  10,   50,  100,  100,  10,   10,   20,   40,  200,  100,   200,  200,  200,  300,  300,  300,   300,    5])
#ef_construction = np.array([  20,   50,   10,  100, 100,  200,   20,   40,  200,  200,   100,    0,   50,  100,   50,   50,   200,    5])
#recall          = np.array([0.22, 0.49, 0.61, 0.72, 0.2, 0.27, 0.15, 0.43, 0.90, 0.72,  0.83, 0.96, 0.97, 0.95, 0.89, 0.89,  0.85, 0.02])

# Measurements for n256
M               = np.array([  10,   10,  100,  200,  300,   200,   300,   25,   10,   75,  150,  280])
ef_construction = np.array([  10,  100,  100,  200,  300,    10,    10,   25,  300,   75,  150,   50])
recall          = np.array([0.22, 0.31, 0.89, 0.95, 0.97,  0.95,  0.97, 0.43, 0.45, 0.79, 0.92, 0.91])



# Create a meshgrid for the data
M_grid, ef_grid = np.meshgrid(np.linspace(M.min(), M.max(), 300), 
                              np.linspace(ef_construction.min(), ef_construction.max(), 300))

# Interpolate recall values onto the meshgrid
recall_grid = griddata((M, ef_construction), recall, (M_grid, ef_grid), method='cubic')


# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(M_grid, ef_grid, recall_grid, cmap='viridis')

# Add labels
ax.set_xlabel('M')
ax.set_ylabel('ef_construction')
ax.set_zlabel('recall')

plt.show()