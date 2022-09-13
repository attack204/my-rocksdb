import matplotlib.pyplot as plt
import numpy as np

num_list = []
x_list = []
for line in open("level.out"): 
    x_list.append(int(line.split(' ')[0]))
    num_list.append(int(line.split(' ')[1])) 
print(len(num_list))
print(len(x_list))
x = np.array(x_list)
y = np.array(num_list)
plt.scatter(x, y, s=1)
plt.show()
