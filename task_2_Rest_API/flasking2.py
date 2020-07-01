import numpy as np
from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/api',methods=['POST', 'GET'])
def predict():
    # Get the data from the POST request.
    # data = request.get_json(force=True)
    data = []
    t = request.json['t']
    cpu = request.json['CPU']
    rx = request.json['RxKBTot'] 
    tx = request.json['TxKBTot']
    print(t, cpu, rx, tx)
    data= {'0':[t], '1':[cpu], '2':[rx], '3':[tx]} 
    p = pd.DataFrame(data) 
    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict(p)
    # Take the first value of prediction
    output = prediction[0]
    
    # print(p)
    # print(output)

    return jsonify({"label":str(output)})
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000, debug=True)