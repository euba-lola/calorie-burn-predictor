## CALORIE BURN PREDICTOR 🏋️‍♂️

## Project Overview  
In today’s health-conscious world, tracking **calorie expenditure** is essential for fitness enthusiasts and professionals. Many fitness apps provide estimates, but they often lack **data-driven accuracy** and fail to combine important factors such as **demographics, workout intensity, and body composition**.  
This project develops a **machine learning pipeline** that predicts the number of calories burned during workouts by combining **demographic data, workout details, and physiological signals (heart rate & body temperature)**.  
The final solution is deployed as a **Streamlit web application** where users or trainers can input data manually or upload CSV files to get **real-time calorie estimates, BMI calculation, and fitness advice**.  

---

## Dataset Description  
The dataset consists of **demographic details and workout session information**. The features used include:  
- **Gender** – Male/Female  
- **Age** – in years  
- **Height** – in cm  
- **Weight** – in kg  
- **Duration** – workout duration in minutes  
- **Heart Rate** – beats per minute during workout  
- **Body Temperature** – Celsius, measured during workout  

### Target Variable  
- **Calories Burned (Continuous)** → the estimated calorie expenditure per workout.  

---

## Data Preprocessing  
### 1. Data Cleaning  
- Checked and handled missing values.  
- Ensured data consistency (units like cm, kg, minutes).  

### 2. Feature Engineering  
Created additional features to improve predictive power:  
- **BMI (Body Mass Index)** = `weight / (height/100)^2`  
- **BMI Category** = {Underweight, Normal, Overweight, Obese}  

### 3. Encoding & Scaling  
- `Gender` was encoded into numerical representation.  
- Continuous variables were standardized for model performance.  

---

## Exploratory Data Analysis (EDA)  
- **Distribution Analysis** → Visualized age, heart rate, weight, and calorie burned.  
- **Correlation Heatmap** → identified strong relationships between weight, duration, heart rate, and calorie output.  
- **BMI Distribution** → visualized various body categories in relation to calorie burn.  

---

## Model Building  

### Models Tested  
A range of regression algorithms were tested to predict calorie burn:  

- **Linear Regression** → Baseline benchmark model.  
- **Decision Tree Regressor** → Captures non-linear relationships.  
- **Random Forest Regressor** → Ensemble model, reduces variance.  
- **Gradient Boosting Regressor** → Boosting method, strong performance with complex patterns.  
- **Support Vector Regressor (SVR)** → Captures non-linear patterns via kernel tricks.  

### Evaluation Metrics  
- **Mean Squared Error (MSE)**  
- **Root Mean Squared Error (RMSE)**  
- **R² Score**  

---

## Model Selection  
After testing and tuning all models:  
- **Random Forest Regressor** consistently achieved the best performance.  
- High **R² score** (capturing variance in calories burned).  
- Low **MSE and RMSE** (fewer errors in predictions).  
- Balanced bias vs. variance.  
The final model was therefore chosen as a **Random Forest Regressor** and saved using **joblib** for deployment.  

---

## 🚀 Deployment  
The final model was deployed using **Streamlit Cloud**, enabling real-time predictions.  

### Features of the App  
- 👤 **Single Prediction**  
  - Enter: gender, age, height, weight, duration, heart rate, and body temperature.  
  - Get: predicted calories burned, BMI value, BMI category, and health advice.  

- 📂 **Batch Upload Mode**  
  - Upload a CSV file with workout records.  
  - Get predictions for all records at once.  
  - Downloadable CSV of results.
 
## Author  
**Morenikeji Euba**  
- 📧 [Email](mailto:morenikejieuba@gmail.com)  
- 💼 [LinkedIn](https://www.linkedin.com/in/morenikeji-euba-92a125190/)  

---
## License  
This project is licensed under the **MIT License** – free to use, modify, and share.  

---
## Acknowledgements  
- The Streamlit team for the open-source framework.  
- scikit-learn contributors.  
- Inspiration from health & fitness tracking applications.  


 **Try it here:** [https://calorie-burn-predictor.streamlit.app/](https://calorie-burn-predictor.streamlit.app/)  
