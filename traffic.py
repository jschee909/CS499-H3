# SVM regressor to estimate traffic

import numpy as np
from sklearn import preprocessing
from sklearn.svm import SVR
from flask import Flask, render_template, request
import matplotlib.pyplot as plt 
from sklearn import svm
import pandas as pd


input_file = 'traffic_data.txt'


fd = pd.DataFrame(columns = ['Freeway', 'Direction','Day', 'Time','Traffic'])

# Reading the data
a = []
b = []
count = 0
with open(input_file, 'r') as f:
    for line in f.readlines():
        data = line[:-1].split(',')
        a.append(data[:-1])
        b.append(data[-1])

b[-1] = '9'
print(a)
print(b)

X = []
Y = []
for k in a:
    X.append([int(v) for v in k])
    

for k in b:
    Y.append([int(v) for v in k])

print(X)
print(Y)





app = Flask(__name__)

@app.route('/')
def index():
  return render_template('template.html')

@app.route('/traffic.py')
def data():
  print('Data Submitted')
  req = request.args.get('wanted')
  arg = req.split(',')
  str = ','.join(arg)
  return str




if __name__ == '__main__':
  app.run(debug=True)