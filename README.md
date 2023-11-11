# employee_satisfaction_classification


## This project consists of two main parts:

## Employee Satisfaction Dataset Classification:

- A classification model is trained to predict employee satisfaction levels using various factors such as last evaluation, number of projects, salary, work accident,etc . The model utilizes machine learning techniques to identify patterns in the data and make predictions on new employee data.

- Flask Web Interface for Prediction:
  
A Flask web application is developed to provide a user-friendly interface for making predictions on employee satisfaction levels. Users can enter the relevant employee data, and the application will display the predicted satisfaction level.

- Dataset Description
  
The employee satisfaction dataset contains information on various factors related to employee satisfaction, including last evaluation, number of projects, salary, work accident,avg monthly hours,time spend in company,work accident, promotion in last 5 years,department,satisfaction level. The satisfaction level is categorized into three classes: not satisfied, moderate, and highly satisfied.

- Classification Model
- 
The classification model is trained using a machine learning algorithm, such as logistic regression, Decision tree, SVM,etc. The model is trained on the employee satisfaction dataset to learn the relationship between the various factors and the satisfaction level. Once trained, the model can be used to predict the satisfaction level for new employee data.

- Flask Web Interface
  
The Flask web application is a Python-based web application framework that allows for easy creation of web interfaces. The application provides a user-friendly interface for entering employee data and displaying the predicted satisfaction level.

## Usage

## To use the classification model and Flask web interface, follow these steps:

### Train the classification model:

- Load the employee satisfaction dataset.
- Split the data into training and testing sets.
- Train the chosen machine learning algorithm on the training data.
- Evaluate the model's performance on the testing data.
  
 ### Run the Flask web application:

- Install the required dependencies, including Flask and the machine learning library used for the model.
- Create a Flask application and define the routes for the web interface.
- Load the trained classification model into the application.
- Implement the web interface for entering employee data and displaying predictions.
  
### Make predictions:

- Enter the employee data into the web interface.
- Click the "Submit" button to generate the predicted satisfaction level.
