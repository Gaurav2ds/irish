from smtplib import SMTPRecipientsRefused
from flask import Flask ,request,render_template
import pickle
import numpy as np
app = Flask(__name__)
model1 = pickle.load(open('model.pkl','rb'))

@app.route("/")
def index():
	
	return render_template("index.html")

@app.route("/irish", methods=['POST', 'GET'])
def irish():
    input_data=np.zeros(3)


    SepalLengthCm=request.form['SepalLengthCm']
    SepalWidthCm=request.form['SepalWidthCm']
    PetalLengthCm=request.form['PetalLengthCm']
    PetalWidthCm=request.form['PetalWidthCm']
    print(SepalLengthCm)
    prediction= model1.predict([[SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]])
    

    Species=prediction[0]
    if Species == 0:
        Specie="Setosa"

    elif Species ==1:
        Specie="Versicolor"
    elif Species ==2:
        Specie ="Virginica"
        





    return render_template("index.html",Species=Specie)
	

if __name__ == "__main__":
    app.run(host="0.0.0.0,"debug=False)
