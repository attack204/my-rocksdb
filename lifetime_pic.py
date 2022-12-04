from curses import keyname
from pickle import BINSTRING
import matplotlib.pyplot as plt
import numpy as np
x_list = []
type_list = []
lifetime_list = []
predict_list = []
kind_correct = {
    "0": 0,
    "-1": 0,
    "1": 0,
    "-2": 0,
    "-3": 0,
    "-4": 0,
    "-5": 0,
    "-6": 0
}
kind_num = {
    "0": 0,
    "-1": 0,
    "1": 0,
    "-2": 0,
    "-3": 0,
    "-4": 0,
    "-5": 0,
    "-6": 0
}
kind_ave = {
    "0": 0,
    "-1": 0,
    "1": 0,
    "-2": 0,
    "-3": 0,
    "-4": 0,
    "-5": 0,
    "-6": 0
}

for line in open("lifetime.out"):
    if(len(line.split(' ')) == 4 and len(line.split(' ')[0]) > 0 and int(line.split(' ')[0]) < 6 and len(line.split(' ')[1]) > 0):
        #print(line.split(' '))
        x_list.append(int(line.split(' ')[0]))
        type_list.append(int(line.split(' ')[1]))
        lifetime_list.append(int(line.split(' ')[2]))
        predict_list.append(int(line.split(' ')[3]))

for l in range(0, 6): #each level
    tot = 0 
    correct = 0
    sum = 0
    data1_list = []
    datan1_list = [] #compact by top level
    data0_list = [] 
    THRESHOLD = 5 * (l + 1)
    for i in range(0, len(x_list)):
        if x_list[i] == l:
            key=str(type_list[i])
            sum = sum + lifetime_list[i]
            kind_ave[key] += lifetime_list[i]
            diff = predict_list[i] - lifetime_list[i]
            if type_list[i] == 1:
                data1_list.append(diff)
            elif type_list[i] < 0:
                datan1_list.append(diff)
            elif type_list[i] == 0:
                data0_list.append(diff)
            tot = tot + 1
            kind_num[key] += 1
            if diff >= -THRESHOLD and diff <= THRESHOLD:
                correct = correct + 1
                kind_correct[key] += 1

    if tot == 0:
        continue
    print("level %d correct rate=%lf average_lifetime=%lf" % (l, correct / tot, sum / tot)) #right number 
    for typ in range(-6, 2):
        key = str(typ)
        if (kind_num[key] != 0):
            print("T%d Accuracy=%.3lf AveLifetime=%.3lf num=%d" % (typ, kind_correct[key] / kind_num[key], kind_ave[key] / kind_num[key], kind_num[key]))
    plt.hist(data0_list, bins=20, color="blue")
    plt.show()
    if(datan1_list not = 0):
        plt.hist(datan1_list, bins=20, color="yellow")
        plt.show()
    plt.hist(data1_list, bins=20, color="red")
    plt.show()

