#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chris
#
# Created:     16/04/2018
# Copyright:   (c) chris 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#from sklearn.datasets import load_iris#load data
from sklearn.linear_model import LogisticRegression#Logistic Regression Class
from sklearn.linear_model import LogisticRegressionCV#Cross validation for LogisticRegression
import matplotlib.pyplot as plt#plotting purpose
import pandas as pd#use pandas data frame
import numpy as np
input_file="C:/Users/chris/Dropbox/Public/My_Research/Curt_lab/metabolic_disease/metab1_input.csv"
data=pd.read_csv(input_file)
train_X=data.iloc[:,1:47]#select columns for input
train_Y=data.iloc[:,47]#select column for output
logi_clf=LogisticRegression(solver="newton-cg",multi_class="multinomial",C=1000.0,max_iter=10000,verbose=1)
logi_clf.fit(train_X,train_Y)
print(logi_clf.score(train_X,train_Y))
predict_label=logi_clf.predict(train_X)
predict_pro=logi_clf.predict_proba(train_X)
output=open("C:/Users/chris/Dropbox/Public/My_Research/Curt_lab/metabolic_disease/output_result.txt","w")
print >>output,"SampleName","Prediction","Truth"
for i in range(len(predict_label)):
    if predict_label[i]!=train_Y[i]:
        print >>output, data.iloc[i,0],predict_label[i],train_Y[i]
output.close()
#multinomial_logistic=LogisticRegressionCV(cv=5,penalty='l1',solver='liblinear',class_weight="balanced",n_jobs=4,multi_class='ovr')
#multinomial_logistic.fit(train_X,train_Y)