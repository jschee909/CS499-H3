
from sklearn.svm import SVC
from flask import Flask, request, render_template


app = Flask(__name__)

dPoints = []
output = []
model = SVC(gamma=0.001, C=100.)


@app.route('/')
def index():
  return render_template('template.html')


@app.route('/getData', methods=['POST'])
def getData():
    ID = request.form['ID']
    dir = request.form['dir']
    day = request.form['day']
    time = request.form['time']
    status = request.form['status']
    dPoints.append([str(ID), str(dir), str(day), str(time)])
    output.append(int(status))

    return "Added data"


@app.route('/predictTraffic', methods=['POST'])
def predictTraffic():
    if (len(dPoints) <= 1 ):
        return ("We need at least two to make a prediction", 400)
    else:
        model.fit(dPoints, output)

        ID = request.form['ID']
        dir = request.form['dir']
        day = request.form['day']
        time = request.form['time']
        print("")
        prediction = model.predict([[str(ID), str(dir), str(day), str(time)]])

        print("Datapoints:", dPoints)
        print("Outputs: ", output)
        print("Predicted Traffic Status: ", prediction)

        return ("Prediction: " + str(prediction), 200)


if __name__ == '__main__':
  app.run(debug=True)
