import pickle
import numpy as np
from flask import Flask, render_template, request
import joblib


app = Flask(__name__)
load_model=pickle.load(open(r"C:\Users\sanal\Desktop\satisfaction\model.sav",'rb'))

Department_mapping = {
    0: 'Accoundant',
    1: 'Support',
    2: 'Marketing',
    3: 'IT',
    4: 'RandD',
    5: 'Technical',
    6: 'Product_mng',
    7: 'Sales',
    8: 'Management',
    9: 'Hr'

}
salary_mapping = {0:'high',1:'medium',2:'low'}

satisfaction_mapping = {
    0: 'Less Satisfied',
    1: 'Moderate',
    2: 'Highly Satisfied'
}



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = []  
    last_evaluation = request.form.get('last_evaluation')
    print(f'Last Evaluation: {last_evaluation}')

    # Access form values using request.form.get() with the corresponding name attribute
    last_evaluation = float(request.form.get('last_evaluation'))
    number_project = int(request.form.get('number_project'))
    average_montly_hours = int(request.form.get('average_montly_hours'))
    time_spend_company = int(request.form.get('time_spend_company'))
    work_accident = int(request.form.get('work_accident'))
    promotion_last_5years = int(request.form.get('promotion_last_5years'))
    
    # Assuming `features` is defined somewhere earlier in your code

    # Encode Department
    department = request.form['department']
    department_encoded = [0] * 10  # Assuming there are 10 different departments
    department_encoded[int(department)] = 1
    features.extend(department_encoded)

    # Encode Salary
    salary = request.form['salary']
    salary_encoded = [0] * 3  # Assuming there are 3 different salary levels
    salary_encoded[int(salary)] = 1
    features.extend(salary_encoded)

# Now you can pass `features` to your machine learning model for prediction


    # Construct the features list
    features = [last_evaluation, number_project, average_montly_hours, time_spend_company, 
                work_accident, promotion_last_5years, department, salary]

    try:
     department = Department_mapping[int(features[6])]
    except KeyError:
     department = 'Unknown Department'

    try:
     salary = salary_mapping[int(features[7])]
    except KeyError:
     salary = 'Unknown Salary'

    department = Department_mapping.get(department, 0)  # Default to 0 if not found
    salary = salary_mapping.get(salary, 2)  # Default to 2 if not found

    # Now you can pass `features` to your machine learning model for prediction
    features[6] = department
    features[7] = salary

    prediction = load_model.predict([features])
    predicted_satisfaction = satisfaction_mapping[prediction[0]]


    return render_template('index.html', prediction_text=predicted_satisfaction)

if __name__ == '__main__':
    app.run(debug=True)
