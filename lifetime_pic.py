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


ans_list = []
real_distribution = []
for i in range(0, len(x_list)):
    ans_list.append(predict_list[i] - lifetime_list[i])
    real_distribution.append(lifetime_list[i])

plt.hist(ans_list, bins=100, color="green")
plt.show()
plt.hist(real_distribution, bins=100, color="red")
plt.show()

for l in range(0, 7): #each level
    kind_correct = {
        "0": {"0": 0, "-1": 0},
        "-1": {"0": 0, "-1": 0},
        "1": {"0": 0, "-1": 0},
        "2": {"0": 0, "-1": 0},
        "3": {"0": 0, "-1": 0},
        "4": {"0": 0, "-1": 0},
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
        "3": {"0": 0, "-1": 0},
        "4": {"0": 0, "-1": 0},
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
        "3": {"0": 0, "-1": 0},
        "4": {"0": 0, "-1": 0},
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
    data3_list = [] #compacted by top level
    data3_list_miss = [] #compacted by top level but prediction is incorrent
    data4_list = [] #compacted by current level and prediction is right
    data4_list_miss = [] #compacted by current level but prediction is incorrent
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
            elif type_list[i] == 3:
                if real_type[i] == -1: #compacted
                    data3_list.append(diff)
                else:
                    data3_list_miss.append(diff)
            elif type_list[i] == 4:
                if real_type[i] == -1:  
                    data4_list.append(diff)
                else:
                    data4_list_miss.append(diff) #type_list[i] == 0 but real_type[i] == 1
            
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
                print("T%s S%s Accuracy=%.3lf Predict_Ave=%.3lf num=%d" % (key1, key2, kind_correct[key1][key2] / kind_num[key1][key2], kind_ave[key1][key2] / kind_num[key1][key2], kind_num[key1][key2]))
    if((l != 3) and (l != 4) and (l != 5) and (l != 6)): 
        continue
    if(len(data1_list) != 0): #short-lived
        plt.hist(data1_list, bins=20, color="red") #upper
        plt.show()
    if((len(data1_list_miss) != 0)):
        plt.hist(data1_list_miss, bins=20, color="orange") #current
        plt.show()
    if(len(data3_list) != 0):
        plt.hist(data3_list, bins=20, color="yellow") #upper
        plt.show()
    if(len(data3_list_miss) != 0):
        plt.hist(data3_list_miss, bins=20, color="green") #current
        plt.show()
    if(len(data4_list) != 0):
        plt.hist(data4_list, bins=20, color="blue") #upper
        plt.show()
    if(len(data4_list_miss) != 0):
        plt.hist(data4_list_miss, bins=20, color="purple") #current
        plt.show()




#4 [0-9]* 0 [0-9]* -1
