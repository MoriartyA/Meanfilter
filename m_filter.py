# -*- coding:cp936 -*-
import numpy as np
import matplotlib.pylab as plt

def txt2mat(filename):
    """read .txt file """
    fr = open(filename, 'r')

    alllines = fr.readlines()
    numberOfLines = len(alllines)
    returnmat = np.zeros(numberOfLines)
    index = 0
    for line in alllines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnmat[index] = listFromLine[-1]
        index += 1
    fr.close()
    return returnmat

def mat2txt(filename, datas):
    """write txt file"""
    fw = open(filename, 'w')
    np.savetxt(filename, datas, fmt='%.2f')
    fw.close()

def smoothdata(data, num):
    """filter the data"""
    numoflines = len(data)
    for i in range(num, numoflines-num):
        data[i] = np.sum(data[i-num:i+num+1])/(2.0*num + 1.0)
    return data


datain = txt2mat("data.txt")
x=range(len(datain))
#plt.plot(x,datain,label='Origin Data')
fdata = smoothdata(datain, 3)
mat2txt('smooth.txt',fdata)
plt.plot(x,fdata,  linewidth=2,label='Mean Filter')
plt.title("compare")
plt.legend(loc='lower right')
plt.show()