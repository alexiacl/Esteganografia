import pandas as pd
import numpy as np
import csv
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.tree import export_graphviz
import six
import sys
#from sklearn.externals.six import StringIO  
from six import StringIO
from IPython.display import Image  
import pydotplus
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
from termcolor import colored as cl # text customization

col_names = ['m00', 'm10', 'm01', 'm20', 'm11', 'm02', 'm30', 'm21', 'm12', 'm03', 'mu20', 'mu11', 'mu02', 'mu30', 'mu21', 'mu12', 'mu03', 'nu20', 'nu11', 'nu02', 'nu30', 'nu21', 'nu12', 'nu03', 'output']
data = pd.read_csv("/Users/alexiacazon/Documents/momentosfinales.csv", header=0, names=col_names)
#print("head", data.head())


feature_cols = ['m00', 'm10', 'm01', 'm20', 'm11', 'm02', 'm21', 'm12', 'mu20', 'mu11', 'mu02', 'mu21', 'mu12', 'mu03', 'nu20', 'nu11', 'nu02', 'nu30', 'nu21', 'nu12', 'nu03']
#print(data[feature_cols])
# print(data.output)
X=data[feature_cols]
Y=data.output

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=1) ##USAREMOS EL 70% de los datos para entrenar y el 30% para probar


clf = DecisionTreeClassifier(criterion='entropy', max_depth=7)

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)
print("ids")
print(X_test)
y_pred = clf.predict(X_test)
print("prediccion", y_pred)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
#Imprime arbol de decision
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=['0','1'])

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('arbol.png')
Image(graph.create_png())
