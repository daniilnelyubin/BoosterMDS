from kNearestNeighbor import kNearestNeighbor
from sklearn.datasets.samples_generator import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,f1_score
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

def plot_data(X,y,title):
    colors = np.random.rand(2,1)
    counter = 0
    for x1,x2 in X:
        plt.scatter(x1,x2,color="r" if y[counter]==0 else "b")
        counter+=1
    plt.title(title)
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.show()

def plot_data_wo_color(X):
    colors = np.random.rand(2,1)
    counter = 0
    for x1,x2 in X:
        plt.scatter(x1,x2,color="grey")
        counter+=1
    plt.title("Test data")
    plt.show()


def errors(y,persent):
    err_index = np.random.randint(0,len(y),int(persent*len(y)))
    y[err_index] = [0 if i==1 else 1  for i in y[err_index]]





X, y = make_classification(n_samples=500, n_informative=2, n_features=2,n_redundant=0,random_state=1)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,shuffle=True,random_state=2)

plot_data(X,y,"Sample")
plot_data_wo_color(X_test)

knn = kNearestNeighbor(X_train,y_train,k=10)
predicted = knn.prediction(X_test)
plot_data(X_test,predicted,"k Nearest Neighbors")
print("Accuracy: " + str(accuracy_score(y_test,predicted)))
print("F1: " + str(f1_score(y_test,predicted)))