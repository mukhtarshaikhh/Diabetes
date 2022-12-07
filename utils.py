import numpy as np
import json
import pickle

class Diabetes_Pred():
    def __init__(self, Glucose, BloodPressure, SkinThickness, Insulin, BMI, 
    DiabetesPedigreeFunction, Age):
        
        self.Glucose=Glucose
        self.BloodPressure=BloodPressure
        self.SkinThickness=SkinThickness
        self.Insulin=Insulin
        self.BMI=BMI
        self.DiabetesPedigreeFunction=DiabetesPedigreeFunction
        self.Age=Age

    def load_model(self):
        with open("decision_tree.pkl", "rb") as f:
            self.model= pickle.load(f)

        with open ("project_json.json","r") as f:
            self.json_data=json.load(f)

        with open("Scaling.pkl", "rb") as f:
            self.scalling_model=pickle.load(f)

    def diabetes_predicition(self):

        self.load_model()
        test_array=np.zeros(len(self.json_data["column_names"]))

        test_array[0]=self.Glucose
        test_array[1]=self.BloodPressure
        test_array[2]=self.SkinThickness
        test_array[3]=self.Insulin
        test_array[4]=self.BMI
        test_array[5]=self.DiabetesPedigreeFunction
        test_array[6]=self.Age

        print(test_array)
        sc_val=self.scalling_model.transform([test_array])

        diab_pred=self.model.predict(sc_val)[0]
        print(diab_pred)
        return diab_pred

# if __name__ == "__main__":

    # Glucose=148.000
    # BloodPressure=50.000
    # SkinThickness=35.000
    # Insulin=0.000
    # BMI=33.600
    # DiabetesPedigreeFunction=0.627
    # Age=50.000

    
    # db=Diabetes_Pred(Glucose, BloodPressure, SkinThickness,
    # Insulin, BMI, DiabetesPedigreeFunction, Age)

    # db.diabetes_predicition()


