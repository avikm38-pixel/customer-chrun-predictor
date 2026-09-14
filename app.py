from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('model_columns.pkl', 'rb') as f:
    model_columns = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    
    input_df = pd.DataFrame([data])
    
    
    input_df = pd.get_dummies(input_df)
    
    
    input_df = input_df.reindex(columns=model_columns, fill_value=0)
    
    
    prediction = int(model.predict(input_df)[0])
    probability = float(model.predict_proba(input_df)[0][1]) 
