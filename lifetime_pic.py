from curses import keyname
from pickle import BINSTRING
import matplotlib.pyplot as plt
import numpy as np
x_list = []
type_list = []
lifetime_list = []
predict_list = []
real_type = []

def addtwodimdict(thedict, key_a, key_b, val): 
    if key_a in adic:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a:{key_b: val}})

for line in open("lifetime.out"):
    #print(line.split(' '))
    x_list.append(int(line.split(' ')[0]))
    predict_list.append(int(line.split(' ')[1]))
    type_list.append(int(line.split(' ')[2]))
    lifetime_list.append(int(line.split(' ')[3]))
    real_type.append(int(line.split(' ')[4]))

for l in range(0, 6): #each level
    kind_correct = {
        "0": {"0": 0, "-1": 0},
        "-1": {"0": 0, "-1": 0},
        "1": {"0": 0, "-1": 0},
        "2": {"0": 0, "-1": 0},
        "-2": {"0": 0, "-1": 0},
        "-3": {"0": 0, "-1": 0},
        "-4": {"0": 0, "-1": 0},
        "-5": {"0": 0, "-1": 0},
        "-6": {"0": 0, "-1": 0}
    }
    kind_num = {
        "0": {"0": 0, "-1": 0},
        "-1": {"0": 0, "-1": 0},
        "1": {"0": 0, "-1": 0},
        "2": {"0": 0, "-1": 0},
        "-2": {"0": 0, "-1": 0},
        "-3": {"0": 0, "-1": 0},
        "-4": {"0": 0, "-1": 0},
        "-5": {"0": 0, "-1": 0},
        "-6": {"0": 0, "-1": 0}
    }
    kind_ave = {
        "0": {"0": 0, "-1": 0},
        "-1": {"0": 0, "-1": 0},
        "1": {"0": 0, "-1": 0},
        "2": {"0": 0, "-1": 0},
        "-2": {"0": 0, "-1": 0},
        "-3": {"0": 0, "-1": 0},
        "-4": {"0": 0, "-1": 0},
        "-5": {"0": 0, "-1": 0},
        "-6": {"0": 0, "-1": 0}
    }
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

    level0_num = 0 #compacted by current level num
    leveln1_num = 0 #compacted by top level num
    level1_num = 0 #compacted by unknow file
    for i in range(0, len(x_list)):
        
        if x_list[i] == l:
            key1=str(type_list[i])
            key2=str(real_type[i])
            sum = sum + lifetime_list[i]
            kind_ave[key1][key2] += lifetime_list[i]
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
            kind_num[key1][key2] += 1
            if real_type[i] == -1:
                leveln1_num += 1
            elif real_type[i] == 1:
                level1_num += 1
            else:
                level0_num += 1
            if diff >= -THRESHOLD and diff <= THRESHOLD:
                correct = correct + 1
                kind_correct[key1][key2] += 1

    if tot == 0:
        continue
    print("level %d correct_rate=%.3lf average_lifetime=%.3lf type-1_num=%d type0_num=%d type1_num=%d" % (l, correct / tot, sum / tot, leveln1_num, level0_num, level1_num)) #right number 
    for key1 in kind_num:
        for key2 in kind_num[key1]:
            if(kind_num[key1][key2] != 0):
                print("T%s Real_Type=%s Accuracy=%.3lf AveLifetime=%.3lf num=%d" % (key1, key2, kind_correct[key1][key2] / kind_num[key1][key2], kind_ave[key1][key2] / kind_num[key1][key2], kind_num[key1][key2]))
    if(l != 4): 
        continue
    if(len(data0_list) != 0):
        plt.hist(data0_list, bins=20, color="yellow")
        plt.show()
    if(len(data0_list_miss) != 0):
        plt.hist(data0_list_miss, bins=20, color="orange")
        plt.show()
    if(len(datan1_list) != 0):
        plt.hist(datan1_list, bins=20, color="red")
        plt.show()
    # if(len(datan1_list_miss) != 0):
    #     plt.hist(datan1_list_miss, bins=20, color="pink")
    #     plt.show()
    if(len(data1_list) != 0):
        plt.hist(data1_list, bins=20, color="black")
        plt.show()
    # if((len(data1_list_miss) != 0)):
    #     plt.hist(data1_list_miss, bins=20, color="brown")
    #     plt.show()

