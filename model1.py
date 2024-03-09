from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
import numpy as np


def predict_carornot(img):
    try:
        model=load_model('car_or_not.h5')
        image = img_to_array(img)
        image = preprocess_input(image)
        key1=0
        image=np.expand_dims(image,axis=0)
        pred = model(image)
        pred_labels=np.argmax(pred,axis=1)
        d={0:'Car',1:'Not a car'}
        for key in d.keys():
            if pred_labels[0]==key:
                key1=key
                print("validating whether car or not...........Result:",d[key])
                print("car assessment complete")
        return d[key1]
    except Exception as e:
        print(e)  

def predict_damageornot(img):
    try:
        model=load_model('damage_or_not.h5')
        image = img_to_array(img)
        image = preprocess_input(image)
        key1=0
        image=np.expand_dims(image,axis=0)
        pred = model(image)
        pred_labels=np.argmax(pred,axis=1)
        d={0:'Whole car',1:'Damaged Car'}
        for key in d.keys():
            if pred_labels[0]==key:
                key1=key
                print("validating whether damaged or not...........Result:",d[key])
                print("car damage assessment complete")
        return d[key1]
    except Exception as e:
        print(e)  


def predict_location(img):
    try:
        model=load_model('damage_location.h5')
        image = img_to_array(img)
        image = preprocess_input(image)
        key1=0
        image=np.expand_dims(image,axis=0)
        pred = model(image)
        pred_labels=np.argmax(pred,axis=1)
        d={0:'Front',1:'Rear',2:'Side'}
        for key in d.keys():
            if pred_labels[0]==key:
                key1=key
                print("validating location of damage...........Result:",d[key])
                print("severity assessment complete")
        return d[key1]
    except Exception as e:
        print(e) 

# def predict_severity(img):
#     try:
#         model=load_model('severity_costestimation.h5')
#         image = img_to_array(img)
#         print("Line 1",image)
#         image = preprocess_input(image)
#         print("Line 2",image)
#         key1=0
#         image=np.expand_dims(image,axis=0)
#         print("Line 3",image)
#         pred = model(image)
#         pred_labels=np.argmax(pred,axis=1)
#         d={0:'Minor',1:'Moderate',2:'Major'}
#         for key in d.keys():
#             if pred_labels[0]==key:
#                 key1=key
#                 print("validating severity...........Result:",d[key])
#                 print("car damage assessment complete")
#         return d[key1]
#     except Exception as e:
#         print(e)   

def predict_severity_and_cost(img,cartype):
    try:
        model = load_model('severity_costestimation.h5')
        image = img_to_array(img)
        image = preprocess_input(image)
        image = np.expand_dims(image, axis=0)
        pred = model.predict(image)
        pred_label = np.argmax(pred, axis=1)[0]
        severity_mapping = {0: 'minor', 1: 'moderate', 2: 'severe'}
        severity = severity_mapping[pred_label]
        cost_estimations = {
            'minor': {
            'Toyota': 15000,
            'Honda': 14000,
            'Ford': 16000,
            'Maruti Suzuki': 12000,
            'Hyundai': 13000,
            'Mahindra': 15500,
            'TATA Motors': 14500,
            'Volkswagen': 17000,
            'Renault': 13500
            },
            'moderate': {
            'Toyota': 25000,
            'Honda': 24000,
            'Ford': 26000,
            'Maruti Suzuki': 22000,
            'Hyundai': 23000,
            'Mahindra': 26500,
            'TATA Motors': 24500,
            'Volkswagen': 28000,
            'Renault': 22500
            },
            'severe': {
            'Toyota': 50000,
            'Honda': 48000,
            'Ford': 52000,
            'Maruti Suzuki': 45000,
            'Hyundai': 47000,
            'Mahindra': 51000,
            'TATA Motors': 49000,
            'Volkswagen': 54000,
            'Renault': 46000
            }
}

        # Assuming user selects 'Toyota' as the car company
        car_company = cartype  # You can modify this to take user input
        cost = cost_estimations[severity][car_company]
        print(f"Severity: {severity}, Estimated cost for {car_company} at {severity} severity: Rs. {cost}")
        return severity, cost
    except Exception as e:
        print("Error:", e)



def predict_internaldamage(img):
    try:
        model=load_model('Seatsnew.h5')
        image = img_to_array(img)
        image = preprocess_input(image)
        key1=0
        image=np.expand_dims(image,axis=0)
        pred = model(image)
        pred_labels=np.argmax(pred,axis=1)
        d={0:'Not_Damaged',1:'Damaged'}
        for key in d.keys():
            if pred_labels[0]==key:
                key1=key
                print("validating internal damage...........Result:",d[key])
                print("internal damage assessment complete")
        return d[key1]
    except Exception as e:
        print(e) 
