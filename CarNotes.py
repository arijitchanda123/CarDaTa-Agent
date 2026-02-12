from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class CarNote(BaseModel):
    Present_Price:float
    Kms_Driven:int
    Owner:int
    number_of_year:int
    Car_Name_encoded:int
    Fuel_Type_Diesel:bool
    Fuel_Type_Petrol:bool
    Seller_Type_Individual:bool
    Transmission_Manual:bool