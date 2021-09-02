from sklearn import neighbors
import streamlit as st
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.svm import SVC as svc
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.title('Iris classification')
st.write('A glance at the Table...')
iris = pd.read_csv('Iris.csv')
st.table(iris.head())
st.write("Rows, Columns: ", iris.shape)
clf_name = st.sidebar.radio(
    "Which ML Classifier to use?", ('KNN', 'SVM', 'Random Forest'))
st.write("You have Chosen: ", clf_name)


def get_param_ui(name):
    param = {}
    if name == 'KNN':
        k = st.sidebar.slider('What is the value of k?', 1, 15)
        param['k'] = k
        st.sidebar.write('You have chosen:', k)
    elif name == 'SVM':
        c = st.sidebar.slider('What is the value of c?', 0.01, 15.0)
        param['c'] = c
        st.sidebar.write('You have chosen:', c)
    else:
        maxdep = st.sidebar.slider(
            'What is the value of Maximum depth?', 2, 15)
        st.sidebar.write('You have chosen:', maxdep)
        n_est = st.sidebar.slider('What is the value of n_estimators?', 1, 100)
        st.sidebar.write('You have chosen:', n_est)
        param['maxdep'] = maxdep
        param['n_est'] = n_est
    return param


ui = get_param_ui(clf_name)


def get_clf(clf_name):
    if clf_name == 'KNN':
        clf = knn(n_neighbors=ui['k'])
    elif clf_name == 'SVM':
        clf = svc(C=ui['c'])
    else:
        clf = rfc(n_estimators=ui['n_est'], max_depth=ui['maxdep'])
    return clf


clf = get_clf(clf_name)
X = iris[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = iris['Species']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
st.write("Accuracy score: ", accuracy_score(y_test, y_pred))
