import sys
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.metrics import accuracy_score
from sklearn import tree
import _pickle

'''__________File names__________'''
trainDataFileName = "trainData.csv"
TreeGraphFileName = "ProtoTypeGraph.dot"
ExportedTreeFileName = "ProtoType.pkl"


'''__________Load training dataset__________'''
try:
    print("Loading training Dataset. file name: " + trainDataFileName)
    balance_data = pd.read_csv(trainDataFileName,sep= ',', header= None)
except:
    print("Failed to load training Dataset. ")
    sys.exit()

print ("training dataset loaded. Dataset Lenght: " + str(len(balance_data)) + ", Dataset Shape: "+str( balance_data.shape))

print("Splitting training dataset to target and feature variables")
X = balance_data.values[:, 1:6]
Y = balance_data.values[:,0]

'''__________Create Desision Tree__________'''
print("Creating DecisionTreeClassifier")
    #Create DecisionTreeClassifier with some parameters,
    # visit "http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html"
    # or "http://dataaspirant.com/2017/02/01/decision-tree-algorithm-python-with-scikit-learn/"
    # for more details
PrototypeTree = DecisionTreeClassifier(criterion ="gini", max_depth=None)

'''__________Train Desision Tree___________'''
print("Training DecisionTreeClassifier")
PrototypeTree.fit(X, Y)
print("Training done")

'''__________Caculate accuracy__________'''
print("Caculating accuracy.")
pred = PrototypeTree.predict(X)
CorrectCount=0
for i in range(0,len(pred)):
    if Y[i]== pred[i]:
        CorrectCount = CorrectCount+1
print("Accuracy is: " + str(CorrectCount/len(pred)))

'''_______Export Desision Tree Graph________'''
print("Exporting Desision Tree Graph. file name: " + TreeGraphFileName)
export_graphviz(PrototypeTree, out_file=TreeGraphFileName, feature_names=['T', 'Q1', 'Q2', 'Q3', 'Q4'])
print("Decision Tree Graph exported.")


'''__________Save DecisionTreeClassifier to disk__________'''
print("Exporting Decision Tree to disk. file name: " + ExportedTreeFileName)
with open(ExportedTreeFileName, 'wb') as fid:
    _pickle.dump(PrototypeTree, fid)
print("Decision Tree saved")

print("~~~End~~~")