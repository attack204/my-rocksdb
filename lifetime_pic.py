from curses import keyname
from pickle import BINSTRING
import matplotlib.pyplot as plt
import numpy as np
THRESHOLD = 25 
x_list = []
type_list = []
lifetime_list = []
predict_list = []
data1_list = []
datan1_list = []
data0_list = []
sum = 0
kind_correct = {
    "0": 0,
    "-1": 0,
    "1": 0,
    "-2": 0,
    "-3": 0
}
kind_num = {
    "0": 0,
    "-1": 0,
    "1": 0,
    "-2": 0,
    "-3": 0
}
kind_ave = {
    "0": 0,
    "-1": 0,
    "1": 0,
    "-2": 0,
    "-3": 0
}

for line in open("lifetime.out"):
    if(len(line.split(' ')) == 4 and len(line.split(' ')[0]) > 0 and int(line.split(' ')[0]) < 6 and len(line.split(' ')[1]) > 0):
        #print(line.split(' '))
        x_list.append(int(line.split(' ')[0]))
        type_list.append(int(line.split(' ')[1]))
        lifetime_list.append(int(line.split(' ')[2]))
        predict_list.append(int(line.split(' ')[3]))

tot = 0
correct = 0
for i in range(0, len(x_list)):
    if x_list[i] == 5 or x_list[i] >= 0:
        key=str(type_list[i])
        sum = sum + lifetime_list[i]
        kind_ave[key] += lifetime_list[i]
        diff = predict_list[i] - lifetime_list[i]
        if type_list[i] == 1:
            data1_list.append(diff)
        elif type_list[i] == -1:
            datan1_list.append(diff)
        elif type_list[i] == 0:
            data0_list.append(diff)
        tot = tot + 1
        kind_num[key] += 1
        if diff >= -THRESHOLD and diff <= THRESHOLD:
            correct = correct + 1
            kind_correct[key] += 1


print("ALL", correct / tot)
if (kind_num["0"] != 0):
	print("T1 Accuracy", kind_correct["0"] / kind_num["0"], "AveLifetime", kind_ave["0"] / kind_num["0"])
if (kind_num["-1"] != 0):
	print("T2 Accuracy", kind_correct["-1"] / kind_num["-1"],  "AveLifetime", kind_ave["-1"] / kind_num["-1"])
if (kind_num["1"] != 0):
	print("T3 Accuracy", kind_correct["1"] / kind_num["1"],  "AveLifetime", kind_ave["1"] / kind_num["1"])
print(sum / tot)
plt.hist(data0_list, bins=20)
plt.show()
plt.hist(datan1_list, bins=20, color="yellow")
plt.show()
plt.hist(data1_list, bins=20, color="red")
plt.show()

