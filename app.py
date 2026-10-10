import joblib
import pandas as pd
new_house = pd.DataFrame([{
    "OverallQual": 7,
    "GrLivArea": 1850,
    "LotArea": 8500,
    "BedroomAbvGr": 3,
    "FullBath": 2,
    "YearBuilt": 2005,
    "GarageCars": 2,
    "GarageArea": 520,
    "TotalBsmtSF": 900,
    "Fireplaces": 1,
    "Neighborhood": "CollgCr",
    "HouseStyle": "2Story"
}])



print("Model saved successfully!")

model = joblib.load("house_prediction.pkl")

joblib.dump(model, "house_price_model.pkl")

predictions = model.predict(new_house)

# print(predictions[0])

import streamlit  as st      # to run app  -->   python -m streamlit run app.py
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠"
)
st.title("🏠 Ames House Price Prediction")
st.write("Enter house details to predict the sale price.")

# # Load trained model
@st.cache_resource
def load_model():
    return joblib.load("house_price_model.pkl")

model = load_model()

# # Input fields
import streamlit as st
Name = st.text_input("Enter the Name:")
OverallQual = st.number_input("Overall Quality", 1, 10, 7)
GrLivArea = st.number_input("Living Area", min_value=1, value=1850)
LotArea = st.number_input("Lot Area", min_value=1, value=8500)
BedroomAbvGr = st.number_input("Bedrooms", min_value=0, value=3)
FullBath = st.number_input("Full Bathrooms", min_value=0, value=2)
YearBuilt = st.number_input("Year Built", min_value=1800, max_value=2026, value=2005)
GarageCars = st.number_input("Garage Cars", min_value=0, value=2)
GarageArea = st.number_input("Garage Area", min_value=0, value=520)
TotalBsmtSF = st.number_input("Basement Area", min_value=0, value=900)
Fireplaces = st.number_input("Fireplaces", min_value=0, value=1)

Neighborhood = st.selectbox(
    "Neighborhood",
    ["CollgCr", "Veenker", "Crawfor", "NoRidge",
     "Mitchel", "Somerst", "NWAmes", "OldTown"]
)

HouseStyle = st.selectbox(
    "House Style",
    ["2Story", "1Story", "1.5Fin", "SLvl",
     "SFoyer", "2.5Unf", "2.5Fin", "1.5Unf"]
)

# # Prediction button
if st.button("Predict Price"):

    new_house = pd.DataFrame([{
        "OverallQual": OverallQual,
        "GrLivArea": GrLivArea,
        "LotArea": LotArea,
        "BedroomAbvGr": BedroomAbvGr,
        "FullBath": FullBath,
        "YearBuilt": YearBuilt,
        "GarageCars": GarageCars,
        "GarageArea": GarageArea,
        "TotalBsmtSF": TotalBsmtSF,
        "Fireplaces": Fireplaces,
        "Neighborhood": Neighborhood,
        "HouseStyle": HouseStyle
    }])

    try:
        prediction = model.predict(new_house)[0]

        st.success(" Prediction Successful!")
        st.metric(
            label="Predicted Sale Price",
            value=f"${prediction:,.2f}"
        )
        st.metric(
            label="predicted sale price in ₹ ",
            value=f"₹{prediction * 96.78:,.2f}"

        )

    except Exception as e:
        st.error(f"Prediction error: {e}")
      

