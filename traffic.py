# SVM regressor to estimate traffic

import numpy as np
from sklearn import preprocessing
from sklearn.svm import SVR
import matplotlib.pyplot as plt 

input_file = 'traffic_data.txt'

# Reading the data
X = []
Y = []
count = 0
with open(input_file, 'r') as f:
    for line in f.readlines():
        data = line[:-1].split(',')
        X.append(data[:1])
        Y.append(data[-1])

Y[-1] = 9
print(X)
print(Y)

colors = colors = ['black', 'blue', 'purple', 'yellow', 'white', 'red', 'lime', 'cyan', 'orange', 'gray']

for i in range(len(colors)):
    plt.scatter(X, Y, c=colors[i])
    
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title("PCA Scatter Plot")
plt.show()