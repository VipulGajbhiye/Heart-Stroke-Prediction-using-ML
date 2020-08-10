from tkinter import *
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle
from sklearn.ensemble import RandomForestClassifier

def prediction_model():
    x = [[int(entry_1.get()), int(entry_2.get()), int(entry_3.get()), int(entry_4.get()), int(entry_5.get()), int(entry_6.get()), int(entry_7.get()), int(entry_8.get()), int(entry_9.get()), float(entry_10.get()), int(entry_11.get()), int(entry_12.get()), int(entry_13.get())]]
    randomforest = pickle.load(open('model.sav', 'rb'))
    predictions = randomforest.predict(x)
    if predictions==0:
        myText.set('********Less chance of Heart Stroke********')
    else:
        myText.set('********High chance of Heart Stroke********')

df=pd.read_csv('heart.csv')

predictors = df.drop(['target'], axis=1)
target = df["target"]
x_train, x_val, y_train, y_val = train_test_split(predictors, target, test_size = 0.22, random_state = 0)
randomforest = RandomForestClassifier()
randomforest.fit(x_train, y_train)
y_pred = randomforest.predict(x_val)

filename = 'model.sav'
pickle.dump(randomforest, open(filename, 'wb'))

win=Tk()
win.geometry("550x780")
win.title("Heart Stroke Predictor")
regTitle=Label(win,text="Patient Details",width=20,font=("bold",20))
age=name=Label(win,text="Age:",width=50,font=("bold",13))
sex=Label(win,text="Sex(0=Male,1=Female):",width=50,font=("bold",13))
cp=Label(win,text="Chest pain type(0,1,2,3):",width=50,font=("bold",13))
trestbps=Label(win,text="Resting blood pressure:",width=50,font=("bold",13))
chol=Label(win,text="Serum cholestoral in mg/dl:",width=50,font=("bold",13))
fbs=Label(win,text="Fasting blood sugar > 120 mg/dl:",width=50,font=("bold",13))
restecg=Label(win,text="Resting electrocardiographic results (values 0,1,2):",width=50,font=("bold",13))
thalach=Label(win,text="Maximum heart rate achieved:",width=50,font=("bold",13))
exang=Label(win,text="Exercise induced angina:",width=50,font=("bold",13))
oldpeak=Label(win,text="Oldpeak:",width=50,font=("bold",13))
slope=Label(win,text="The slope of the peak exercise ST segment:",width=50,font=("bold",13))
ca=Label(win,text="Number of major vessels (0-3) colored by flourosopy:",width=50,font=("bold",13))
thal=Label(win,text="thal( 0 = normal; 1 = fixed defect; 2 = reversable defect):",width=50,font=("bold",13))

entry_1=Entry(win,width=10)
entry_2=Entry(win,width=10)
entry_3=Entry(win,width=10)
entry_4=Entry(win,width=10)
entry_5=Entry(win,width=10)
entry_6=Entry(win,width=10)
entry_7=Entry(win,width=10)
entry_8=Entry(win,width=10)
entry_9=Entry(win,width=10)
entry_10=Entry(win,width=10)
entry_11=Entry(win,width=10)
entry_12=Entry(win,width=10)
entry_13=Entry(win,width=10)

regTitle.grid(row=0,pady=10)
age.grid(row=2, pady=10)
sex.grid(row=4, pady=10)
cp.grid(row=6, pady=10)
trestbps.grid(row=8, pady=10)
chol.grid(row=10, pady=10)
fbs.grid(row=12, pady=10)
restecg.grid(row=14, pady=10)
thalach.grid(row=16, pady=10)
exang.grid(row=18, pady=10)
oldpeak.grid(row=20, pady=10)
slope.grid(row=22, pady=10)
ca.grid(row=24, pady=10)
thal.grid(row=26, pady=10)
entry_1.grid(row=2,column=1, pady=10)
entry_2.grid(row=4,column=1, pady=10)
entry_3.grid(row=6,column=1, pady=10)
entry_4.grid(row=8,column=1, pady=10)
entry_5.grid(row=10,column=1, pady=10)
entry_6.grid(row=12,column=1, pady=10)
entry_7.grid(row=14,column=1, pady=10)
entry_8.grid(row=16,column=1, pady=10)
entry_9.grid(row=18,column=1, pady=10)
entry_10.grid(row=20,column=1, pady=10)
entry_11.grid(row=22,column=1, pady=10)
entry_12.grid(row=24,column=1, pady=10)
entry_13.grid(row=26,column=1, pady=10)

myText = StringVar();
but = Button(win, text="Predict",width=20,font=("bold",13),bg='brown',fg='white', command=prediction_model)
but.grid(row=28,columnspan=2, pady=10)
result = Label(win, text="",width=50,font=("bold",13), textvariable=myText).grid(row=29)

win.mainloop()