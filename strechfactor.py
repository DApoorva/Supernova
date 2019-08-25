# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 15:27:01 2019

@author: Mayur, Apoorva
"""

from numpy import genfromtxt
import matplotlib.pyplot as plt
import sys

if(len(sys.argv) != 3 ):
    print("Usage: strechfactor.py <Path to csv file> <Path to output file>")
    exit()
filename = sys.argv[1]
my_data = genfromtxt(filename, delimiter=',')

X = my_data[1:,:1].flatten()
Y = my_data[1:,1:].flatten()

# Plot the Time(s) rate versus Mmax
graph = plt.plot(X, Y, marker='.', linestyle='none')
#plt.margins(0.02)
graph = plt.title('B Band')
graph = plt.xlabel('Strech Factor(s)')
graph = plt.ylabel('mb-mv')

plt.savefig(sys.argv[2])
# Draw the plot
plt.show()
