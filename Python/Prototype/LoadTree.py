import _pickle

try :
    with open('ProtoType.pkl', 'rb') as fid:
        clf_gini = _pickle.load(fid)
except:
    print("failed QQ")

print(clf_gini.predict([[1.98,1,0,0,0]]))