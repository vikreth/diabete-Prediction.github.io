import streamlit as st
import numpy as np
import string
import pickle
st.set_option('deprecation.showfileUploaderEncoding', False)
model = pickle.load(open('model_pkl.pkl', 'rb'))


def main():
    st.header("ការប៉ាន់ស្មាននៃការកើតជម្ងឺទឹកនោមផ្អែមចំពោះស្ត្រី")
    st.subheader("សូមបញ្ចូលព័ត៌មានរបស់អ្នកដូចខាងក្រោម")

    Pregnancies = st.slider("Input Your Number of Pregnancies", 0, 16)
    Glucose = st.slider("Input your Gluclose", 74, 200)
    BloodPressure = st.slider("Input your Blood Pressure", 30, 130)
    SkinThickness = st.slider("Input your Skin thickness", 0, 100)
    Insulin = st.slider("Input your Insulin", 0, 200)
    BMI = st.slider("Input your BMI", 14.0, 60.0)
    DiabetesPedigreeFunction = st.slider(
        "Input your Diabetes Pedigree Function", 0.0, 6.0)
    Age = st.slider("Input your Age", 0, 100)

    inputs = [[Pregnancies, Glucose, BloodPressure, SkinThickness,
               Insulin, BMI, DiabetesPedigreeFunction, Age]]

    if st.button('Predict'):
        result = model.predict(inputs)
        updated_res = result.flatten().astype(int)
        if updated_res == 0:
            st.write("អ្នកមិនមានជម្ងឺទឹកនោមផ្អែមទេ។")
        else:
            st.write(
                "អ្នកប្រហែលជាបានកើតជម្ងឺទឹកនោមផ្អែមហើយ​ សូមប្រញាប់ទៅជួបគ្រូពេទ្យដែលនៅជិតអ្នកបំផុត។")


if __name__ == '__main__':
    main()
