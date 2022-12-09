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
    real_lifetime_list = []
    sum = 0
    tot = 0
    for i in range(0, len(x_list)):
        if x_list[i] == l:
            real_lifetime_list.append(lifetime_list[i])
            sum += lifetime_list[i]
            tot += 1
    print("level=%d average lifetime=%d" % (l, sum / tot))
    if(len(real_lifetime_list) != 0):
        plt.hist(real_lifetime_list, bins=20, color="yellow")
        plt.show()
