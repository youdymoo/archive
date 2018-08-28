
# coding: utf-8

# In[170]:


import numpy as np
from matplotlib import pyplot as plt
from itertools import permutations, product
import random


# In[171]:


# paratemers 
layers = 2
dimension = 2*layers + 1
density = np.zeros((dimension,dimension,dimension))
trajectory = []  # save the density at each time step 
# sink_loc = [0,0,0]
# discretization parameters
# hexagon_length
h = 1
# distance between grids, assuming that dx = dy = dz
dx = np.sqrt(3)*h
dy = dx; dz = dx;
# time uses for the marching method
T = 1


# In[172]:


class grid:
    def __init__(self, index):
        self.coordinate = index
        self.neb_coordinate = [ [(x+y) for x,y in zip(self.coordinate,list(i))] for i in list(permutations([0,1,-1]))]
        self.boundary = 0          # if 1, thiis is on boundary, then use the boundary condition, do not update
        self.density = 0.0          # local value of density
        v_max = 50; density_max = 20;
        self.speed = v_max*(1-self.density/density_max) # average speed
        self.flux = self.speed*self.density # flux
    
    def update(self, neighbor_grids):
        if self.boundary == 0:  # not boundary grid
            # insert three iterations of grid values here 
            pass

# a list save grids temporarily and foward to density
grids = []

# random initial density
for i,j in product(range(dimension), range(dimension)):
    for k in range(dimension):
        density[i,j,k] = 100*random.random()
        gd = grid([i,j,k])
        gd.density = density[i,j,k]
        if max(gd.coordinate) == dimension-1 or min(gd.coordinate) == 0:
            gd.boundary = 1
            gd.density = 0        # constant boundary condition
        # check if the index is valid for the hexagonal system
        grids.append(gd)
        
        
def lax_friedrichs(timestep, density, grids):
    new_density =np.zeros((dimension,dimension,dimension))
    for i,j in product(range(dimension), range(dimension)): # the dimension that needs to be updated
        for k in range(dimension):                          # the dimension to fix
            # start from here -----------------------------------------------------
            # insert the update here
            for gd in grids:
                neighbor_grids = []        # find all neighbor grids as objects
                gd.update(neighbor_grids)  
                new_density[i,j,k] = gd.density
    return new_density
            
        
### update density
t = 0; timestep = 0;
while(t<T):
    # stability condition
    dt = 0.5*dx
    t+=dt
    timestep += 1
    new_density = lax_friedrichs(timestep, density, grids)  # update density
    trajectory.append(density)

# visualize trajectory

