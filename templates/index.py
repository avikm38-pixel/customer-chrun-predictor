<!DOCTYPE html>
<html>
<head>
    <title>Customer Churn Predictor</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }
        label { display: block; margin-top: 12px; font-weight: bold; }
        input, select { width: 100%; padding: 8px; margin-top: 4px; }
        button { margin-top: 20px; padding: 10px 20px; background: #333; color: white; border: none; cursor: pointer; }
        #result { margin-top: 20px; font-size: 20px; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Predict Customer Churn</h1>
    <form id="predictForm">
        <label>Gender</label>
        <select name="gender">
            <option value="Male">Male</option>
            <option value="Female">Female</option>
        </select>

        <label>Senior Citizen</label>
        <select name="SeniorCitizen">
            <option value="0">No</option>
            <option value="1">Yes</option>
        </select>

        <label>Partner</label>
        <select name="Partner">
            <option value="Yes">Yes</option>
            <option value="No">No</option>
        </select>

        <label>Dependents</label>
        <select name="Dependents">
            <option value="Yes">Yes</option>
            <option value="No">No</option>
        </select>

        <label>Tenure (months)</label>
        <input type="number" name="tenure" min="0" required>

        <label>Phone Service</label>
        <select name="PhoneService">
            <option value="Yes">Yes</option>
            <option value="No">No</option>
        </select>

        <label>Multiple Lines</label>
        <select name="MultipleLines">
            <option value="No">No</option>
            <option value="Yes">Yes</option>
            <option value="No phone service">No phone service</option>
        </select>

        <label>Internet Service</label>
        <select name="InternetService">
            <option value="DSL">DSL</option>
            <option value="Fiber optic">Fiber optic</option>
            <option value="No">No</option>
        </select>

        <label>Online Security</label>
        <select name="OnlineSecurity">
            <option value="Yes">Yes</option>
            <option value="No">No</option>
            <option value="No internet service">No internet service</option>
        </select>

        <label>Online Backup</label>
        <select name="OnlineBackup">
            <option value="Yes">Yes</option>
            <option value="No">No</option>
            <option value="No internet service">No internet service</option>
        </select>

        <label>Device Protection</label>
        <select name="DeviceProtection">
            <option value="Yes">Yes</option>
            <option value="No">No</option>
            <option value="No internet service">No internet service</option>
        </select>

        <label>Tech Support</label>
        <select name="TechSupport">
            <option value="Yes">Yes</option>
            <option value="No">No</option>
            <option value="No internet service">No internet service</option>
        </select>

        <label>Streaming TV</label>
        <select name="StreamingTV">
            <option value="Yes">Yes</option>
            <option value="No">No</option>
            <option value="No internet service">No internet service</option>
        </select>

        <label>Streaming Movies</label>
        <select name="StreamingMovies">
            <option value="Yes">Yes</option>
            <option value="No">No</option>
            <option value="No internet service">No internet service</option>
        </select>

        <label>Contract</label>
        <select name="Contract">
            <option value="Month-to-month">Month-to-month</option>
