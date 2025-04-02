from flask import Flask,render_template,request
from joblib import load
import pandas as pd
def loading(n,p,k,temp,hum,ph,rf):
    model1=load("CRS.joblib")
    res=[]
    label=['rice','maize','chickpea','kidneybeans','pigeonpeas','mothbeans',
    'mungbean','blackgram','lentil','pomegranate','banana','mango','grapes',
    'watermelon','muskmelon','apple','orange','papaya','coconut','cotton',
    'jute','coffee']

    res.append(float(n))
    res.append(float(p))
    res.append(float(k))
    res.append(float(temp))
    res.append(float(hum))
    res.append(float(ph))
    res.append(float(rf))
    df=pd.DataFrame([res],columns=['N','P','K','temperature','humidity','ph','rainfall'])
    return label[model1.predict(df)[0]]
app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def home():
    if request.method=='POST':
        n=request.form.get('Nitrogen')
        p=request.form.get('Phosphorous')
        k=request.form.get('Pottasium')
        temp=request.form.get('Temparature')
        hum=request.form.get('Humidity')
        ph=request.form.get('pH')
        rf=request.form.get('Rainfall')

        try:
            cn=loading(n,p,k,temp,hum,ph,rf)
            data1={'result':cn}
            return render_template('result.html',data=data1)
        except Exception as e:
            return f"Error: {str(e)}"
    return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)
