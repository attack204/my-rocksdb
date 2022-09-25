import matplotlib.pyplot as plt
import numpy as np
THRESHOLD = 25 
num_list = []
x_list = []
data_list = []
for line in open("lifetime.out"):
    if(len(line.split(' ')) == 2 and len(line.split(' ')[0]) > 0 and int(line.split(' ')[0]) < 6 and len(line.split(' ')[1]) > 0):
        #print(line.split(' '))
        x_list.append(int(line.split(' ')[0]))
        num_list.append(int(line.split(' ')[1]))

tot = 0
correct = 0
for i in range(0, len(x_list)):
    if x_list[i] == 5:
        print(num_list[i])
        data_list.append(num_list[i])
        tot = tot + 1
        if num_list[i] >= -THRESHOLD and num_list[i] <= THRESHOLD:
            correct = correct + 1;

print(correct / tot)
plt.hist(data_list, bins=20)

plt.show()

# print(len(num_list))
# print(len(x_list))
# x = np.array(x_list)
# y = np.array(num_list)
# plt.scatter(x, y, s=0.1)
# plt.show()
