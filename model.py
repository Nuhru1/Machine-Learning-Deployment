import pandas as pd
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pickle

dataset = pd.read_csv('Iris.csv')
dataset = dataset.drop(['Id'], axis = 1)

# want to use ony 2 classes here so let's cut rows cprresponding to the third class
data = dataset.iloc[ : , : ]


# here our target are species: iris_setosa (1) and iris_versicolor(-1). So the list Y will contain those values
target = data['Species']
Y = []

for x in target:
    if x == 'Iris-setosa':
        Y.append(1)
    elif x == 'Iris-versicolor':
        Y.append(0)
    else:
        Y.append(-1)
        

# As we will only use 2 features, let's drop others features
data = data.drop([ 'Species'], axis = 1)


# Y is a list , let's convert our features into a list then shuffle them together before splitting 
X = data.values.tolist()

# let's convert our train and test sets to a numpy arrays
X = np.array(X)

classifier = SVC(kernel='linear')
classifier.fit(X,Y)

pickle.dump(classifier, open('model.pkl','wb'))


model = pickle.load(open('model.pkl', 'rb'))
pred = model.predict(np.array([5.1, 3.5, 1.4, 0.2]).reshape(1, -1))
name = {
    1: "Iris_Setosa",
    0: "Iris_versiColor",
    -1: "Iris-virginica"
}


print(name[pred[0]])