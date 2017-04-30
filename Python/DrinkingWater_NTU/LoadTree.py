import _pickle
import sys

try :
    print('Importing DecisionTreeClassifier')
    with open('DrinkgingWater_NTU.pkl', 'rb') as fid:
        clf_gini = _pickle.load(fid)
except:
    print("Failed to import DecisionTreeClassifier")
    sys.exit()

#Predict dataset
print(clf_gini.predict([[2.5,103,0]]))
print(clf_gini.predict([[2.5,50,0]]))