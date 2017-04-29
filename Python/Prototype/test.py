import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.metrics import accuracy_score
from sklearn import tree

#balance_data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/balance-scale/balance-scale.data',sep= ',', header= None)
balance_data = pd.read_csv('trainData.csv',sep= ',', header= None)

print ("Dataset Lenght:: " + str(len(balance_data)))
print ("Dataset Shape:: "+str( balance_data.shape))

print("Dataset:: ")
print (balance_data.head())

X = balance_data.values[:, 1:6]
Y = balance_data.values[:,0]
#X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)


clf_gini = DecisionTreeClassifier(criterion = "gini")
#clf_gini = DecisionTreeClassifier()

'''
clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 0,
                              max_depth=None, min_samples_leaf=5)
'''
'''
clf_gini = DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=3,
            max_features=None, max_leaf_nodes=None, min_samples_leaf=5,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            presort=False, random_state=100, splitter='best')
'''


clf_gini.fit(X, Y)

print(clf_gini.predict([[1.98,1,0,0,0]]))

export_graphviz(clf_gini,out_file="alabagua.dot",feature_names=['T','Q1','Q2','Q3','Q4'])


pred = clf_gini.predict(X)
#print(pred)

CorrectCount=0
for i in range(0,len(pred)):
    if Y[i]== pred[i]:
        CorrectCount = CorrectCount+1

print("Accuracy is: " + str(CorrectCount/len(pred)))

#print (accuracy_score(X,pred)*100)

print("The super ending!!!")