import pandas as pd
import streamlit as st
import joblib
import numpy as np

# ================== Page Config ==================
st.set_page_config(page_title="🔥 Calorie Burn Predictor", page_icon="🔥", layout="wide")

# ================== Load Model ==================
@st.cache_resource
def load_model():
    return joblib.load("calorie_predictor.pkl")

try:
    model = load_model()
except Exception as e:
    st.error(f"⚠️ Could not load model: {e}")
    st.stop()

# ================== CSS Styling ==================
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #e0eafc 0%, #cfdef3 100%);
    font-family: 'Segoe UI', sans-serif;
}

h1, h2, h3 {
    color: #0A74DA !important;
    font-weight: 900;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #0A74DA, #4FB3FF);
    color: white;
    font-weight: bold;
    border-radius: 12px;
    padding: 0.7rem 1.5rem;
    border: none;
}
.stButton>button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #4FB3FF, #0A74DA);
}

/* Result card */
.result-card {
    background: #eaf4ff;
    border-left: 6px solid #0A74DA;
    padding: 1rem;
    border-radius: 10px;
    font-weight: bold;
    font-size: 1.3rem;
    margin-top: 20px;
}

/* Sticky footer */
footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background: #f9f9f9;
    border-top: 1px solid #ddd;
    padding: 10px 0;
    text-align: center;
    z-index: 100;
}
</style>
""", unsafe_allow_html=True)

# ================== Helpers ==================
def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)

def categorize_bmi(bmi_value: float) -> str:
    if bmi_value < 18.5:
        return "Underweight"
    elif 18.5 <= bmi_value < 25:
        return "Normal"
    elif 25 <= bmi_value < 30:
        return "Overweight"
    else:
        return "Obese"

def advice(bmi_category: str) -> str:
    if bmi_category == "Underweight":
        return "⚠️ Your BMI is low. Consider a healthy diet."
    elif bmi_category == "Normal":
        return "✅ Healthy BMI range. Keep it up!"
    elif bmi_category == "Overweight":
        return "⚠️ You are overweight. Exercise more & eat balanced meals."
    else:
        return "❗ Obese. Consult a doctor/fitness expert for a plan."

# ================== HERO TITLE ==================
st.markdown("""
<div style="text-align:center; margin-bottom:30px;">
    <h1 style="
        font-size:3rem;
        font-weight:900;
        color:#0A74DA;
        display:inline-block;
        border-bottom:4px solid #0A74DA;
        padding-bottom:10px;
        margin-bottom:5px;
    ">
        🔥 Calorie Burn Predictor
    </h1>
    <p style="font-size:1.2rem; color:#333; font-weight:400; margin-top:10px;">
        AI-powered fitness app to estimate calories burned during workouts 🏋️‍♂️
    </p>
</div>
""", unsafe_allow_html=True)

# ================== Tabs ==================
tabs = st.tabs(["ℹ️ About", "🏃 Single Prediction", "📂 Batch Upload"])

# ========== ABOUT TAB ==========
with tabs[0]:
    col1, col2 = st.columns([1,2])
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/2964/2964514.png", width=220)  # illustration
    with col2:
        st.markdown("## ℹ️ About This App")
        st.write("""
        Welcome to the **Calorie Burn Predictor**!  
        This app uses **Machine Learning** to predict calories you burn during a workout session.  

        ### ⚡ Features
        - Predict calories based on **Age, Gender, Height, Weight, Duration, Heart Rate, Body Temp, BMI**.  
        - Provides **BMI Category** & health advice.  
        - Supports **Single Entry** or **Batch CSV Upload**.  

        ### 🏗️ Workflow
        1. Input your workout details manually 🏃  
        2. Or upload a `.csv` for batch predictions 📂  
        3. The app calculates **BMI** & **BMI Category**  
        4. Model outputs calorie predictions 🔥  
        """)

# ========== SINGLE PREDICTION ==========
with tabs[1]:
    st.header("🏃 Single Prediction")
    st.markdown("### 👤 Personal Details")
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.slider("Age", 10, 100, 25)
    height = st.number_input("Height (cm)", 100.0, 250.0, 170.0)
    weight = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)

    st.markdown("### 💪 Workout Info")
    duration = st.slider("Duration (minutes)", 1, 180, 30)
    heart_rate = st.slider("Heart Rate (bpm)", 60, 200, 100)
    body_temp = st.slider("Body Temperature (°C)", 35.0, 45.0, 37.0)

    # Feature engineering
    bmi = calculate_bmi(weight, height)
    bmi_cat = categorize_bmi(bmi)

    if st.button("🎯 Predict Calories Burned"):
        try:
            data = {
                "Gender": [gender],
                "Age": [age],
                "Height": [height],
                "Weight": [weight],
                "Duration": [duration],
                "Heart_Rate": [heart_rate],
                "Body_Temp": [body_temp],
                "BMI": [bmi],
                "BMI_Category": [bmi_cat]
            }
            df = pd.DataFrame(data)
            y_pred_sqrt = model.predict(df)
            prediction = np.square(y_pred_sqrt)[0]

            st.markdown(f"<div class='result-card'>🔥 Estimated Calories Burned: <b>{prediction:.2f} kcal</b></div>", unsafe_allow_html=True)
            st.info(f"💡 BMI: {bmi:.2f} ({bmi_cat})")
            st.write(advice(bmi_cat))
        except Exception as e:
            st.error(f"⚠️ Error making prediction: {e}")

# ========== BATCH UPLOAD ==========
with tabs[2]:
    st.header("📂 Batch Upload Prediction")
    st.write("Upload a CSV file with the following columns: **Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp**")
    
    # sample csv
    sample = """Gender,Age,Height,Weight,Duration,Heart_Rate,Body_Temp
Male,25,175,70,45,120,38
Female,30,160,60,30,105,37.8
Male,40,180,85,20,95,37.2"""
    st.download_button("📥 Download Sample CSV", sample, "sample.csv")
    
    file = st.file_uploader("Upload CSV", type="csv")
    if file:
        df = pd.read_csv(file)
        df["BMI"] = df["Weight"] / ((df["Height"] / 100) ** 2)
        df["BMI_Category"] = df["BMI"].apply(categorize_bmi)
        
        y_pred_sqrt = model.predict(df)
        df["Predicted_Calories"] = np.square(y_pred_sqrt)
        
        st.success("✅ Predictions Done")
        st.dataframe(df)
        
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Predictions", data=csv, file_name="calorie_predictions.csv", mime="text/csv")

# ================== STICKY FOOTER ==================
st.markdown(
    """
    <footer>
        <p style="font-size:15px; color:#555; margin:4px;">
            Built with ❤️ using <b>Streamlit</b>
        </p>
        <div style="margin:6px 0;">
            <a href="mailto:morenikejieuba@gmail.com" target="_blank" style="text-decoration:none;">
                <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" 
                     width="26" style="margin:0 8px;" title="Email">
            </a>
            <a href="https://www.linkedin.com/in/morenikeji-euba-92a125190/" target="_blank" style="text-decoration:none;">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" 
                     width="26" style="margin:0 8px;" title="LinkedIn">
            </a>
        </div>
        <p style="font-size:12px; color:#aaa; margin:4px;">© 2025 Euba Morenikeji</p>
    </footer>
    """,
    unsafe_allow_html=True
)