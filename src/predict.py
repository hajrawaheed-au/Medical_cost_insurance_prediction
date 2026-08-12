# Import libraries

import joblib
import pandas as pd
# Load Model
model=joblib.load("models/random_forest_model.pkl")

# User Input
while True:
    age = int(input("Enter age:"))
    sex=input("Enter gender (male/female): ").lower()
    bmi=int(input("Enter Bmi:"))
    children=int(input("Enter no of children:"))
    smoker=input("smoker?(yes/no): ").lower()
    region=input("Enter region (southwest/southeast/northwest/northeast): ").lower()
    
    # Encoding column
    sex_encoded= 1 if sex=="female" else 0
    smoker_encoded= 1 if smoker== "yes" else 0
    dict={
    "northeast" : 0,
    "northwest" : 1,
    "southeast": 2,
    "southwest": 4 
    }
    
    region_encoded=dict[region.lower()]
    
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [sex_encoded],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker_encoded],
        'region': [region_encoded]
    })
    # predictions
    prediction=model.predict(input_data)
    print("Predicted Charges Value: ",prediction[0])
    