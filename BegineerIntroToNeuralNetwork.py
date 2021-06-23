# Paste this on jupyter notebook.
#  %matplotlib inline
from matplotlib import pyplot as plt
import numpy as np

data = [ [3, 1.5, 1],
         [2, 1, 0],
         [4, 1.5, 1],
         [3, 1, 0],
         [3.5, .5, 1],
         [2, .5, 0],
         [5.5, 1, 1],
         [1, 1, 0]
# Here, datas are length, width, type; type = 0 for red and 1 for blue
        ]

mystery_flower = [4.5, 1]

# print(data[0])   # Gives data of first index

# print(data[0][1])  # Gives data of index 1 from item of data at index 0 since it is list inside list.

# Network
#       0       (Flower type)
#      / \     ( w1, w2, b)
#     0   0   ( Inputs: Length, Width)

# Now, taking random w1, w2 and bias as:
w1 = np.random.randn()
w2 = np.random.randn()
b = np.random.randn()

# Since our output is just 0 or 1, sigmoid is good to use as activation function here.

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1-sigmoid(x))


T = np.linspace(-6, 6, 100)   # Range to plot the graph. Print it to get the datas.
# print(T)
Y = sigmoid_derivative(T)
A = sigmoid(T)
# print(Y)   # Now, Y is between 0 and 1
plt.plot(T, A, c='r')
plt.plot(T, Y, c='b')

# Training loop:


# Training loop:
for i in range(1,1001):  # Running loop 1000 times or, for i in range(1000): also could be!
    # print(i)
