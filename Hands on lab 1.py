#!/usr/bin/env python
# coding: utf-8

# In[24]:


# importacion del archivo
import pandas as pd
df= pd.read_csv("C:/Users/sabri/OneDrive/Escritorio/python ticmas/ejercicios practicos mod 2/data_corona_group (2) (2).csv", sep=",")


# In[25]:


#imprimir las 1eras 5 filas
df.head()


# In[26]:


#ultimos 5 registros
df.tail()


# In[27]:


#dimensiones del dataset
print(df.shape)


# In[28]:


#obtener la totalidad de los registros  por columnas--->analizar los valores missings
df.count()


# In[29]:


df.info()


# In[30]:


#si solo quiero conocer el tipo de dato
df.dtypes


# In[31]:


#si queremos verificar la estructura del dataset
type(df)


# In[32]:


#listar los nombres por columnas
print(df.columns)


# In[38]:


#eliminar columnas
columns_to_drop=['Sno','Date','Province/State']


# In[ ]:




