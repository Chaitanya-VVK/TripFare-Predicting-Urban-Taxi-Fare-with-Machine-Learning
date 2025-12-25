TripFare is an end-to-end Machine Learning project that predicts the total taxi fare for an urban trip based on ride details such as distance, duration, passenger count, time of travel, and surcharges.
**Project Overview**
The project uses real-world NYC taxi trip data to perform:
Data cleaning and preprocessing
Feature engineering (trip distance, duration, time-based features)
Exploratory Data Analysis (EDA)
Outlier handling using IQR
Model training and comparison
Multiple regression models were evaluated, including Linear, Ridge, Lasso, Random Forest, and Gradient Boosting.
Random Forest Regressor achieved the best performance with an R² score of ~0.99.
**Tech Stack**
Python, Pandas, NumPy
Scikit-learn
Matplotlib
Streamlit
Joblib
**Deployment**
The final model is deployed using Streamlit, allowing users to input trip details and instantly receive a predicted fare through an interactive web interface.
**Outcome**
A complete, production-ready ML pipeline demonstrating real-world data science workflow from data analysis to deployment.
