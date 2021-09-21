# %%
# week 4 Thursday, numpy package
# functions; attributes; methods
# np array have to have the same data type, so we can do math 
import numpy as np
from numpy.core.defchararray import array
import random as random

array1 = np.array([1,2,3])
array2 = np.array([(1,2,3),(4,5,6)])
array3 = np.ones((1,3))*6
array3.dtype
array3.dt
np.array()
# %%
a = np.random.randint(1,100,(6,12))
print(np.std(a))
print(np.mean(a[:,2]))
print(np.mean(a))
print(np.mean(a,axis=0)) #column mean 
print(np.mean(a,axis=1)) #row mean