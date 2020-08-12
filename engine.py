import sys
from flask import Flask
from flask import request, redirect , render_template
import pandas as pd
# from numpy import *
import numpy as np
from sklearn import preprocessing
from sklearn import datasets, linear_model


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Flask!"

@app.route('/test', methods = ['POST'])
def test():
    data =pd.read_csv('./data/train dataset.csv')
    array = data.values

    for i in range(len(array)):
        if array[i][0]=="Male":
            array[i][0]=1
        else:
            array[i][0]=0


    df=pd.DataFrame(array)

    maindf =df[[0,1,2,3,4,5,6]]
    mainarray=maindf.values
    # print (mainarray)


    temp=df[7]
    train_y =temp.values
    # print(train_y)
    # print(mainarray)
    train_y=temp.values

    for i in range(len(train_y)):
        train_y[i] =str(train_y[i])



    mul_lr = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg',max_iter =1000)
    mul_lr.fit(mainarray, train_y)

    predict = []
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    openess = request.form['openess']
    neurotics = request.form['neurotics']
    conscientiousness = request.form['conscientiousness']
    agreeableness = request.form['agreeableness']
    extraversion = request.form['extraversion']

    if(gender == "Male"):
        predict.append(1)
    
    else:
        predict.append(0)
    
    predict.append(age)
    predict.append(openess)
    predict.append(neurotics)
    predict.append(conscientiousness)
    predict.append(agreeableness)
    predict.append(extraversion)

    # prediction = prediction_method(predict)
    

    predict_array =[]
    for i in range(0, len(predict)): 
        predict_array.append(int(predict[i]))

    predict_array = np.array(predict_array, ndmin=2)
    predict_result = mul_lr.predict(predict_array)
    return render_template("result.html" , result =predict_result , name= name ) 


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000 , debug=True)


