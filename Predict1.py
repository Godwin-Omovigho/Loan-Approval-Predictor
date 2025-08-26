import streamlit as st
import pandas as pd
import numpy as np
import pickle


# The top of the app
st.set_page_config(page_title="Loan Approval Predictor", layout="wide")
st.title("Loan Approval Predictor 💰")


def load_model():
    model=pickle.load(open("C:\\Users\\HPEE\\Documents\\GitHub\\Loan-Approval-Predictor\\random_forest_model.pkl",'rb'))
    
    return model


model=load_model()






def show_predict_page():
    
    # Disclaimer Sidebar
    
    st.sidebar.header("About This App")
    st.sidebar.info(
    "This app predicts the likelihood of a loan being approved based on user-provided "
    "data. This is for educational purposes and is not financial advice."
    )

    # --- Create columns for the form ---
    st.header("Please Enter Your Details")
    
    
    Age = st.number_input("Age", min_value=0, max_value=70, step=1)
    if Age <=18:
        st.warning("Please enter a valid age")
    else:
        st.success(f"Your age is {Age}")
    
    
    Gender =st.selectbox("Gender",["Female","Male"])
    Education = st.selectbox("Education",["Associate","Bachelor", "Doctorate", "High School","Master"])
    Home_Ownership = st.selectbox("Home Ownership",["Mortgage","Own","Rent","Other"])


    st.subheader("Financial Information")
    Income = st.number_input("Income",min_value=100, max_value=10000000, step=1)
    if Income <=10:
        st.warning('Enter a valid amount')
    else:
        st.success(f'Your income is {Income}')
    Loan_Amount = st.number_input('Loan Amount',min_value=10,max_value=10000000)
    Loan_Intent = st.selectbox("Loan Intent",["Debt consolidation","Education","Home improvement","Medical","Personal","Venture"])
    Loan_interest_rate= st.number_input("Loan Interest Rate",min_value=3.5,max_value=40.0,step=0.5)
    
    if Loan_Amount >0:
        Loan_percent_income = (Loan_Amount/Income)

    Loan_percent_income = st.number_input("Loan Percent Income", value=Loan_percent_income,disabled=True)
    
    st.success(f"Your Loan_percent_income is {Loan_percent_income}")

    st.subheader("Credit History")
    Credit_score = st.number_input("Credit Score")
    previous_loan_defaults_on_file = st.selectbox("Defaults",["No","Yes"])


  
    ok=st.button('Show Loan Status')


    if ok:
    
        Gender_map={"Male":1, "Female":0}
        Education_map= {"Associate":0,"Bachelor":1, "Doctorate":2, "High School":3,"Master":4}
        Home_Ownership_map={"Mortgage":0,"Own":1,"Other":1,"Rent":3}
        Loan_Intent_map={"Debt consolidation":0,"Education":1,"Home improvement":2,"Medical":3,"Personal":4,"Venture":5}
        Defaults_map={"No":0,"Yes":1}
    
        # Encode the data
        Gender = Gender_map[Gender]
        Education = Education_map[Education]
        Home_Ownership=Home_Ownership_map[Home_Ownership]
        Loan_Intent = Loan_Intent_map[Loan_Intent]
        previous_loan_defaults_on_file=Defaults_map[previous_loan_defaults_on_file]
    
        X=np.array([[Age,Gender,Education,Income,Home_Ownership,Loan_Amount,Loan_Intent,Loan_interest_rate,Loan_percent_income,Credit_score,previous_loan_defaults_on_file]])
    
        prediction=model.predict(X)
        #prediction=np.argmax(prediction)
        
        st.success(f"predicted value is {prediction}")
    
        if prediction == 1:
            st.success("Congratulations! You are likely to qualify for the loan. 🎉")
        else:
            st.error("Unfortunately, you are not likely to qualify for the loan. 😔")

    #st.success(f"your values are: {X}")

#X = X.astype(float)

#if ok:
 #   model=data.predict(X)
    
  #  if model==0:
   #     return st.subheader("You do not qualify for a loan")
    #if model==1:
     #   return st.subheader('You qualify for a loan')