from flask import Flask , render_template , request 
import pickle
import numpy as np
app=Flask(__name__)

model=pickle.load(open(r"model.pkl","rb"))   # Loading the model

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/predict',methods=['GET','POST'])
def predict():
    area=float(request.form['area'])
    bedrooms=int(request.form['bedrooms'])
    bathrooms=int(request.form['bathrooms'])

    prediction=model.predict([[area,bedrooms,bathrooms]])[0]
    prediction=round(prediction,2)
    return render_template("index.html",result=f"Predicted price is : ${prediction}")
if __name__=='__main__' :
    app.run()
