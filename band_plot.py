# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 15:27:01 2019

@author: Mayur, Apoorva
"""

from numpy import genfromtxt
import matplotlib.pyplot as plt
import numpy as np
import sys

if(len(sys.argv) != 3 ):
    print("Usage: band_plot.py <Path to csv file> <Path to output file>")
    exit()
filename = sys.argv[1]
my_data = genfromtxt(filename, delimiter=',')

X = my_data[1:,:1].flatten()
Y = my_data[1:,1:].flatten()

# Plot the Time of Decay rate versus Time of Decay
graph = plt.plot(X, Y, marker='.', linestyle='none')
#plt.margins(0.02)
graph = plt.xlabel('Time of Decay')
graph = plt.ylabel('Absolute Magnitude (Mmax)')
X = X[X!=0]
Y = Y[Y!=0]
# Perform a linear regression using np.polyfit(): a, b
a, b = np.polyfit(X, Y, 1)

# Print the results to the screen
print('slope =', a)
print('intercept =', b)

# Make theoretical line to plot
x = np.array([0, abs(max(X))])
y = a * x + b

# Add regression line to your plot
graph = plt.plot(x, y)
plt.savefig(sys.argv[2]+".png")
# Draw the plot
plt.show()
