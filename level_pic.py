import matplotlib.pyplot as plt
import numpy as np

font_size=15
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]
num_list = []
x_list = []
for line in open("level.out"): 
    x_list.append(int(line.split(' ')[0]))
    num_list.append(int(line.split(' ')[1])) 
print(len(num_list))
print(len(x_list))
x = np.array(x_list)
y = np.array(num_list)
plt.xlabel('clock', fontsize=font_size)  
plt.ylabel('level', fontsize=font_size)
plt.scatter(x, y, s=5)
plt.show()