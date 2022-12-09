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
    "2": 0,
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
    "2": 0,
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
    "2": 0,
    "-2": 0,
    "-3": 0,
    "-4": 0,
    "-5": 0,
    "-6": 0
}

for line in open("lifetime.out"):
    #print(line.split(' '))
    x_list.append(int(line.split(' ')[0]))
    predict_list.append(int(line.split(' ')[1]))
    type_list.append(int(line.split(' ')[2]))
    lifetime_list.append(int(line.split(' ')[3]))
    real_type.append(int(line.split(' ')[4]))

for l in range(0, 6): #each level
    real_lifetime_list_0 = []
    real_lifetime_list_n1 = []
    sum = 0
    tot = 0
    cnt0 = 0
    cntn1 = 0
    for i in range(0, len(x_list)):
        if x_list[i] == l:
            if real_type[i] == 0:
                real_lifetime_list_0.append(lifetime_list[i])
                cnt0 += 1
            else:
                real_lifetime_list_n1.append(lifetime_list[i])
                cntn1 += 1
            sum += lifetime_list[i]
            tot += 1
    print("level=%d average lifetime=%d cnt0=%d cntn1=%d" % (l, sum / tot, cnt0, cntn1))
    if(len(real_lifetime_list_0) != 0):
        plt.hist(real_lifetime_list_0, bins=20, color="yellow")
        plt.show()
    if(len(real_lifetime_list_n1) != 0):
        plt.hist(real_lifetime_list_n1, bins=20, color="red")
        plt.show()

