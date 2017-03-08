# SVM regressor to estimate traffic

import numpy as np
from sklearn import preprocessing
from sklearn.svm import SVR
from flask import Flask, render_template, request
import matplotlib.pyplot as plt 

input_file = 'traffic_data.txt'


# Reading the data
X = []
Y = []
count = 0
with open(input_file, 'r') as f:
    for line in f.readlines():
        data = line[:-1].split(',')
        X.append(data[:])
        Y.append(data[-1])

Y[-1] = 9
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