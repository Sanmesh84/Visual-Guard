from flask import Flask, request, jsonify
from flask_cors import CORS
from model1 import predict_carornot,predict_damageornot,predict_location,predict_severity_and_cost,predict_internaldamage
import numpy as np
import cv2
import io
import PIL.Image as Image
app = Flask(__name__)
CORS(app, resources={r"/getprediction": {"origins": "http://127.0.0.1:5500"},r"/getdamage":{"origins": "http://127.0.0.1:5500"}})

@app.route('/getprediction', methods=['POST'])

def sample():
    print("Hello")
    try:
        file = request.files['img']
        cartype=request.form['cartype']
        print(file.filename)
        #file_bytes = np.fromfile(file, np.uint8)
        file_bytes=file.read()
        file=Image.open(io.BytesIO(file_bytes))
        #file = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        file=file.resize((224,224))
        if(predict_carornot(file)=="Car"):
            if(predict_damageornot(file)=="Damaged Car"):
                location=predict_location(file)
                severity, cost = predict_severity_and_cost(file,cartype)
                return jsonify({'CAR_or_NOT': "Yes",'Damaged_or_Not':"YES",
                                'LOCATION':location,'severity': severity, 'cost': cost})
            else:
                return jsonify({'Damaged_or_Not': "No"})   
        else:
            return jsonify({'CAR_or_NOT': "No"})

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/getdamage', methods=['POST'])
def internaldamage():
    try:
        file = request.files['seatimg']
        #cartype=request.form['cartype']
        print(file.filename)
        #file_bytes = np.fromfile(file, np.uint8)
        file_bytes=file.read()
        file=Image.open(io.BytesIO(file_bytes))
        #file = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        file=file.resize((224,224))
        damagedseat=predict_internaldamage(file)
        return jsonify({'Seat_damaged_or_not': damagedseat})
                                
        

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)

