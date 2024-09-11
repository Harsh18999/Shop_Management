import streamlit as st
import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np 
from mlxtend.plotting import plot_decision_regions
from sklearn.preprocessing import LabelEncoder,PolynomialFeatures
import sklearn.datasets as dt

def Algorithm(X,y,clf):
    Model = LogisticRegression() if clf == 'Binary' else LogisticRegression(multi_class='multinomial')
    Model.fit(X,y)
    
    y_pred = Model.predict(X)
    fig = plt.figure(figsize=(10,6))
    acc = accuracy_score(y,y_pred)
    plt.title(f'Accuracy Score : {acc}')
    plot_decision_regions(X, y, Model, legend=len(np.unique(y)))
    st.pyplot(fig)

def plot_decision_boundary(X,y,degree=1):

    poly = PolynomialFeatures(degree=degree)
    X_trf = poly.fit_transform(X)

    Model = LogisticRegression()
    Model.fit(X_trf,y)
    y_pred = Model.predict(X_trf)
    accuracy = accuracy_score(y_pred,y)

    a=np.arange(start=X[:,0].min()-1, stop=X[:,0].max()+1, step=0.01)
    b=np.arange(start=X[:,1].min()-1, stop=X[:,1].max()+1, step=0.01)


    XX,YY=np.meshgrid(a,b)

    input_array=np.array([XX.ravel(),YY.ravel()]).T

    labels=Model.predict(poly.transform(input_array))

    fig = plt.figure(figsize=(12,6))
    plt.contourf(XX,YY,labels.reshape(XX.shape),alpha=0.5)
    plt.scatter(X[:,0],X[:,1], c=y)
    plt.title('Degree = {}, accuracy is {}'.format(degree,np.round(accuracy,4)))
    st.pyplot(fig)


st.sidebar.title('Logistic Regression Visualizer')
st.subheader('Logistic Regression Visualization Tool!')
dataset_type = st.sidebar.selectbox('Select dataset ',['Generated','Uploaded'])
dataset = None
data = None

if dataset_type == 'Uploaded':
    dataset = st.sidebar.file_uploader('Please Upload File')
    if dataset:
       data = pd.read_csv(dataset)
       columns = data.columns 
       x1 = st.sidebar.selectbox('Select X1',columns)
       x2 = st.sidebar.selectbox('Select X2',[x for x in columns if x != x1])
       target = st.sidebar.selectbox('Select Target Feature',[x for x in columns if x != x1 and x != x2 ])
       clf_type = st.sidebar.selectbox('Classification Type', ['Binary','Multinomial','Polynomial'] )
       if clf_type == 'Polynomial':
            degree = int(st.sidebar.number_input(label='Enter Polynomial degree',min_value=1,max_value=15,step=1))
       scatt = st.sidebar.button('Plot data')

       if scatt:
           if data.dtypes[target]!=int:
               le = LabelEncoder()
               le.fit(data[target])
               data[target] = le.transform(data[target])
           fig = plt.figure(figsize = (12,6)) 
           plt.scatter(data[x1],data[x2],c=data[target],cmap='winter',s=100)
           st.pyplot(fig)

       run_algorithm = st.sidebar.button('Run Algorithm') 

       if run_algorithm:
            if data.dtypes[target]!=int:
                le = LabelEncoder()
                le.fit(data[target])
                data[target] = le.transform(data[target])
            X = data[[x1,x2]].values
            y = data[target].values
            if clf_type == 'Polynomial':
                plot_decision_boundary(X,y,degree)
                
            else:
                Algorithm(X,y,clf_type)
                
       st.sidebar.write(data.head())

elif dataset_type == 'Generated':
    X,y = None,None

    n_samples = st.sidebar.number_input(label='Enter Number of sumples',min_value=10,value=100)
    n_classes = st.sidebar.number_input(label='Enter Number of classes in target variable',min_value=2)
    classs_diff = st.sidebar.number_input(label='Enter distance between each classes',value=0.3,min_value=0.1)
    clf_type = st.sidebar.selectbox('Classification Type', ['Binary','Multinomial','Polynomial'] )
    if clf_type == 'Polynomial':
           degree = int(st.sidebar.number_input(label='Enter Polynomial degree',min_value=1,max_value=15,step=1))

    if st.sidebar.button('Generate dataset'):
        X,y = dt.make_classification(n_samples=n_samples, n_features=2, n_informative=2, n_redundant=0, n_repeated=0, n_classes=n_classes, n_clusters_per_class=1, weights=None, flip_y=0.01, class_sep=classs_diff, hypercube=True, shift=0.0, scale=1.0, shuffle=True, random_state=41)
        if clf_type == 'Polynomial':
            plot_decision_boundary(X,y,degree)

        else:
            Algorithm(X,y,clf_type)
           

