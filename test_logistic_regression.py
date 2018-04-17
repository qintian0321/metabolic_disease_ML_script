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
from sklearn.datasets import load_iris#load data
from sklearn.linear_model import LogisticRegression#Logistic Regression Class
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
input_file="C:/Users/chris/Dropbox/Public/My_Research/Curt_lab/metabolic_disease/metab1_input.csv"
d=pd.read_csv(input_file,header=0)
