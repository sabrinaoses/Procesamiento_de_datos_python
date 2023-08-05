#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Punto1, importar las librerias p/la realización por ej: pandas,numpy,  matplotlib, etc y el dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("C:/Users/sabri/OneDrive/Escritorio/python ticmas/ejercicios practicos mod 2/titanic.csv",sep=",")


# In[3]:


#Punto 2,imrimir las 1eras 5 filas
df.head()


# In[4]:


#punto 3 imprimir las ultimas 5 filas
df.tail()


# In[5]:


# punto 4 imprimir las dimensiones del dataset
print(df.shape)


# In[6]:


#punto 5, obt la totalidad de los registros p/columns
df.count()


# In[7]:


#punto 6, analizar el tipo de dato por columna
df.dtypes


# In[8]:


#punto7, obtener el tpo de estruct del dataset, si es o no un dataframe
type(df)


# In[9]:


#punto8, listar los nombres por columns
print(df.columns)


# In[10]:


#punto9, separar los  features en una var x y la var target en y
X=df.drop('Survived', axis=1)
y=df.Survived #defino el target


# In[15]:


#separo los datos en train(70%)y test(30%)con un random_state=42
from sklearn.model_selection import train_test_split


# In[12]:


#pto10, me quedo con el 30 y el 70 para elm train
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=30,random_state=42)


# In[17]:


#pto 11,12 y 13, crea un arbol de decision p un mod de clasif, con los stes param defin
from sklearn.tree import DecisionTreeClassifier 
tree=DecisionTreeClassifier(max_depth=2,random_state=42)#profundidad 2 y semilla 42


# In[ ]:




