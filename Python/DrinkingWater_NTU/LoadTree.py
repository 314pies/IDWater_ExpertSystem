import _pickle
import sys

try :
    print('Importing DecisionTreeClassifier')
    with open('ProtoType.pkl', 'rb') as fid:
        clf_gini = _pickle.load(fid)
except:
    print("Failed to import DecisionTreeClassifier")
    sys.exit()

#Predict dataset
print(clf_gini.predict([[3,100,0]]))