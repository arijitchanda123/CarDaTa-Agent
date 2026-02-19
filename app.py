# 1. Library imports
import uvicorn
from fastapi import FastAPI
from CarNotes import CarNote
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("random_forest_model.pkl","rb")
classifier=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome ': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_banknote(data:CarNote):
    data = data.dict()
    Present_Price=data['Present_Price']
    Kms_Driven=data['Kms_Driven']
    Owner=data['Owner']
    number_of_year=data['number_of_year']
    Car_Name_encoded=data['Car_Name_encoded']
    Fuel_Type_Diesel=data['Fuel_Type_Diesel']
    Fuel_Type_Petrol=data['Fuel_Type_Petrol']
    Seller_Type_Individual=data['Seller_Type_Individual']
    Transmission_Manual=data['Transmission_Manual']

   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[Present_Price,Kms_Driven,Owner,number_of_year,Car_Name_encoded,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]])
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload
