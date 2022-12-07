from flask import Flask, jsonify, request, render_template, url_for
from utils import Diabetes_Pred

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")

# @app.route("/test")
# def predict():
#     return "main page"

@app.route("/result", methods=["POST","GET"])
def predicition():
    if request.method == "POST":
        data=request.form
        print(data)
        Glucose=eval(data["Glucose"])
        BloodPressure=eval(data["BloodPressure"])
        SkinThickness=eval(data["SkinThickness"])
        Insulin=eval(data["Insulin"])
        BMI=eval(data["BMI"])
        DiabetesPedigreeFunction=eval(data["DiabetesPedigreeFunction"])
        Age=eval(data["Age"])
        # Glucose=148.000
        # BloodPressure=50.000
        # SkinThickness=35.000
        # Insulin=0.000
        # BMI=33.600
        # DiabetesPedigreeFunction=0.627
        # Age=50.000
        obj=Diabetes_Pred(Glucose,BloodPressure,SkinThickness,Insulin,
        BMI,DiabetesPedigreeFunction,Age)

        result=obj.diabetes_predicition()
        if result==1:
            return render_template("form.html", pred="Pateint is Diabetic")
        else:
            return render_template("form.html", pred="Pateint is Non Diabetic")


if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)