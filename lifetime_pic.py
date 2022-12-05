from curses import keyname
from pickle import BINSTRING
import matplotlib.pyplot as plt
import numpy as np
x_list = []
type_list = []
lifetime_list = []
predict_list = []
real_type = []
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
    if(len(line.split(' ')) == 5 and len(line.split(' ')[0]) > 0 and int(line.split(' ')[0]) < 6 and len(line.split(' ')[1]) > 0):
        #print(line.split(' '))
        x_list.append(int(line.split(' ')[0]))
        type_list.append(int(line.split(' ')[1]))
        lifetime_list.append(int(line.split(' ')[2]))
        predict_list.append(int(line.split(' ')[3]))
        real_type.append(int(line.split(' ')[4]))

for l in range(0, 6): #each level
    tot = 0 
    correct = 0
    sum = 0
    data1_list = [] #compacted by unknown file
    data1_list_miss = []
    datan1_list = [] #compacted by top level
    datan1_list_miss = [] #compacted by top level but prediction is incorrent
    data0_list = [] #compacted by current level and prediction is right
    data0_list_miss = [] #compacted by current level but prediction is incorrent
    THRESHOLD = 5 * (l + 1)
    #print("test size=%d", len(x_list))
    level0_num = 0 #compacted by current level num
    level1_num = 1 #compacted by top level num
    for i in range(0, len(x_list)):
        
        if x_list[i] == l:
            key=str(type_list[i])
            sum = sum + lifetime_list[i]
            kind_ave[key] += lifetime_list[i]
            diff = predict_list[i] - lifetime_list[i]
            
            if type_list[i] == 1:
                if real_type[i] == -1:
                    data1_list.append(diff)
                else:
                    data1_list_miss.append(diff)
            elif type_list[i] < 0:
                if real_type[i] == -1: #compacted
                    datan1_list.append(diff)
                else:
                    datan1_list_miss.append(diff)
            elif type_list[i] == 0:
                if real_type[i] == 0:  
                    data0_list.append(diff)
                else:
                    data0_list_miss.append(diff) #type_list[i] == 0 but real_type[i] == 1
            
            tot = tot + 1
            kind_num[key] += 1
            if real_type[i] == -1:
                level1_num += 1
            else:
                level0_num += 1
            if diff >= -THRESHOLD and diff <= THRESHOLD:
                correct = correct + 1
                kind_correct[key] += 1

    if tot == 0:
        continue
    print("level %d correct rate=%.3lf average_lifetime=%.3lf level0_num=%d level1_num=%d" % (l, correct / tot, sum / tot, level0_num, level1_num)) #right number 
    for typ in range(-6, 2):
        key = str(typ)
        if (kind_num[key] != 0):
            print("T%s Accuracy=%.3lf AveLifetime=%.3lf num=%d" % (key, kind_correct[key] / kind_num[key], kind_ave[key] / kind_num[key], kind_num[key]))
    if(len(data0_list) != 0):
        plt.hist(data0_list, bins=20, color="yellow")
        plt.show()
    if(len(data0_list_miss) != 0):
        plt.hist(data0_list_miss, bins=20, color="orange")
        plt.show()
    if(len(datan1_list) != 0):
        plt.hist(datan1_list, bins=20, color="red")
        plt.show()
    if(len(datan1_list_miss) != 0):
        plt.hist(datan1_list_miss, bins=20, color="pink")
        plt.show()
    if(len(data1_list) != 0):
        plt.hist(data1_list, bins=20, color="black")
        plt.show()
    if((len(data1_list_miss) != 0)):
        plt.hist(data1_list_miss, bins=20, color="brown")
        plt.show()

