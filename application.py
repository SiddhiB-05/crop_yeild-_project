from flask import Flask,request,jsonify,render_template

import pickle
import numpy as np
import pandas as pd

rf_regressor=pickle.load(open('models/rf_regressor.pkl','rb'))
preprocessor=pickle.load(open('models/preprocessor.pkl','rb'))
application=Flask(__name__)   

app=application  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_data', methods=['GET','POST'])
def predict():
    if request.method=='POST':
        data = request.get_json()

        Area = data['area']
        Item = data['item']
        Year = int(data['year'])
        average_rain_fall_mm_per_year = float(data['rainfall'])
        pesticides_tonnes = float(data['pesticides'])
        avg_temp = float(data['avg_temp'])

        input_df = pd.DataFrame([{
            'Area': Area,
            'Item': Item,
            'Year': Year,
            'average_rain_fall_mm_per_year': average_rain_fall_mm_per_year,
            'pesticides_tonnes': pesticides_tonnes,
            'avg_temp': avg_temp
        }])

        transformed_data = preprocessor.transform(input_df)
        result = rf_regressor.predict(transformed_data)

        return jsonify({
            "prediction": int(result[0]),
            "crop": Item,
            "region": Area
        })  
    else:
        return render_template('home.html')

if __name__=="__main__":  
    app.run(debug=True)     

