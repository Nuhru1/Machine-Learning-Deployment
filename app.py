import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [x for x in request.form.values()]
    final_features = np.array(int_features).reshape(1, -1)
    prediction = model.predict(final_features)

    name = {
        1: "Iris Setosa",
        -1: "Iris versiColor",
        0: "Iris virginica"
        }


    output = name[prediction[0]]

    return render_template('index.html', Result='The Specy is $ {}'.format(output))



if __name__ == "__main__":
    app.run(debug=True)