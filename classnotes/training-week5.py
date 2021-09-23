# %%
# week 4 Thursday, numpy package
# functions; attributes; methods
# np array have to have the same data type, so we can do math 
import numpy as np
import os as os 
os.getcwd()

# %%
list_name = [1, 2, 3, 4, 5, 6, 7]
print(list_name[0])
print(list_name[-1])
print(list_name[3:6])
print(list_name[0:])
print(list_name[-2:])
print(list_name[1:6:2])

# print every item in list_name
# method 1 
for i in range(len(list_name)):
    print(list_name[i])

# method 2
for i in list_name:
    print(i)

# method 3
for i in (0,1,2,3):
    print(list_name[i])

a = 5
if a in list_name:
    print("True")
    if a < 100:
        print("No")
else:
    print("I dont know")

nlist = [list_name[i] for i in range(len(list_name)) if list_name[i] > 3]
# %%
