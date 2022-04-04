#Importing Important library
import pandas as pd
import streamlit as st
import pickle
from datetime import date
    
#date_time = datetime.fromtimestamp(1887639468)
today = date.today()
f = open("file_logger.txt", "a")

#Import pickle file
pickle_in = open("heart_classifier.pkl","rb")
heart_classifier=pickle.load(pickle_in)


def main():
    
    #code is the header
    html_temp = """
   <div style="background-color:tomato;padding:10px">
   <h2 style="color:white;text-align:center;">Streamlit Heart Disease Prediction ML App </h2>
   </div>
   """
   
   
    st.markdown(html_temp,unsafe_allow_html=True)
    st.info("")
    
    #--------------------------------------------------------------------------
    
    
    #Code for file prediction
    data = st.file_uploader("Choose a csv file for Prediction", ["csv"])
    if data is not None:
        
        f.write(f"{today} : Dataset uploaded")
        f.write("\n")
        
        df = pd.read_csv(data)
        st.markdown("Dataset you have uploaded")
        
        f.write(f"{today} : Dataset Shown")
        f.write("\n")
        
        st.dataframe(df)
        
        try:
            f.write(f"{today} : Prediction Started")
            f.write("\n")
            
            ans = heart_classifier.predict(df)
            df["predcited_value"] = ans
            
            f.write(f"{today} : Prediction Complete")
            f.write("\n")
            
            st.markdown("Dataset after Prediction")
            st.dataframe(df)
            
            f.write(f"{today} : Dataset Shown")
            f.write("\n")
            
            
            if st.button("Download"):
                df.to_csv("Result.csv")
                st.success("Download Complete")
                
                f.write(f"{today} : Dataset Downloaded after Prediction")
                f.write("\n")
                
          
        except Exception as e:
            st.error("Invalid file formate, Please! Try Again")
            
            f.write(f"{today} : {e}")
            f.write("\n")
           
            
    #--------------------------------------------------------------------------
        
        
     
    html_temp = """
    <h2 style="color:White;text-align:center;">Or</h2>
    </div>
    """


    st.markdown(html_temp,unsafe_allow_html=True)
     
    #------------------------------------------------------------------------
    
    #Code for inputs and predicting the output
    age = st.text_input("Age:-")
    sex = st.selectbox("Gender:- sex (1 = male, 0 = female)", [1, 0])
    cp = st.selectbox("Chest Pain Type:- Value 1: typical angina, Value 2: atypical angina, Value 3: non-anginal pain, Value 4: asymptomatic",[1, 2, 3, 4])
    trestbps = st.text_input("trestbps:- resting blood pressure (mm Hg on admission to the hospital)")
    chol = st.text_input("chol:- cholesterol measurement in mg/dl")
    fbs = st.selectbox("fbs:- fasting blood sugar (> 120 mg/dl, 1 = true; 0 = false)", [0, 1])
    restecg = st.selectbox("Restecg:- Resting electrocardiographic measurement (0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy by Estes' criteria)", [0, 1, 2])
    thalach = st.text_input("Thalach:- maximum heart rate achieved")
    exang = st.selectbox("Exang:- Exercise induced angina (1 = yes; 0 = no)", [0, 1])
    oldpeak = st.text_input("Oldpeak:- ST depression induced by exercise relative to rest ('ST' relates to positions on the ECG plot)")
    slope = st.selectbox("Slope:- ST segment (Value 1: upsloping, Value 2: flat, Value 3: downsloping)", [1, 2, 3])
    ca = st.text_input("Ca:- The number of major vessels (0-3)")
    thal = st.text_input("Thal:- blood disorder called thalassemia (3 = normal; 6 = fixed defect; 7 = reversable defect)")


    if st.button("Predict"):
        try:
            f.write(f"{today} : Individual Prediction Started")
            f.write("\n")
            
            result = heart_classifier.predict([[age,sex,cp,trestbps,chol,fbs,
                                    restecg,thalach,exang,oldpeak,slope,ca,thal]])
            st.markdown("If Output : 1 than Yes")
            st.markdown("If Output : 0 than No")
            st.success('The output is {}'.format(result))
            
            f.write(f"{today} : Individual Prediction Complete")
            f.write("\n")
            
            
        except Exception as e:
            st.error("Invalid Input, Please! try again....")
            
            f.write(f"{today} : {e}")
            f.write("\n")
            
            

    
if __name__ == '__main__' :
    main()
    