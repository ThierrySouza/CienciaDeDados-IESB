
# coding: utf-8

# In[2]:


#Importando a biblioteca
import pandas as pd

#criando o dataFrame através da leitura do arquivo
df = pd.read_excel('C:/Users/1831133126/Downloads/201710_EmissaoPassagens_SCDP.xlsx', skiprows=3, skip_footer=2)

#Filtrando as colunas
df.columns = df.columns.str.strip()


# In[ ]:


#Verificando os tipos das colunas
df.dtypes

#verificando o frame
df.info()

# verificar as 5 primeiras linhas do arquivo
df.head()

# verificar as 5 últimas linhas do arquivo
df.tail()


# In[ ]:


# Agrupando as passagens pelo orgão
df_group_orgao_superior = df.groupby('Nome do órgão superior')


# In[ ]:


#Somando as tarifas GERAIS
print(df_group_orgao_superior['Valor Tarifa Comercial'].sum())
print(df_group_orgao_superior['Valor Tarifa Governo'].sum())
print(df_group_orgao_superior['Valor Tarifa Embarque'].sum())
print(df_group_orgao_superior['Valor Bilhete'].sum())


# In[ ]:


#Maior soma das tarifas GERAIS
print(df_group_orgao_superior['Valor Tarifa Comercial'].sum().max())
print(df_group_orgao_superior['Valor Tarifa Governo'].sum().max())
print(df_group_orgao_superior['Valor Tarifa Embarque'].sum().max())
print(df_group_orgao_superior['Valor Bilhete'].sum().max())


# In[ ]:


# Agrupando as passagens por Companhia aerea
df_group_comp_air = df.groupby('Companhia Aérea')

#Valor médio das passagens por Companhia
df_group_comp_air['Valor Tarifa Comercial'].mean()


# In[ ]:


#Somando as tarifas GERAIS por Companhia
print(df_group_comp_air['Valor Tarifa Comercial'].sum())
print(df_group_comp_air['Valor Tarifa Governo'].sum())
print(df_group_comp_air['Valor Tarifa Embarque'].sum())
print(df_group_comp_air['Valor Bilhete'].sum())


# In[ ]:


#Maior soma das tarifas GERAIS por Companhia
print(df_group_comp_air['Valor Tarifa Comercial'].sum().max())
print(df_group_comp_air['Valor Tarifa Governo'].sum().max())
print(df_group_comp_air['Valor Tarifa Embarque'].sum().max())
print(df_group_comp_air['Valor Bilhete'].sum().max())


# In[ ]:


#Formatando a data de emissão do bilhete
df['Data Emissão Bilhete'] = pd.to_datetime(df['Data Emissão Bilhete'], format='%Y-%m-%d %H:%M:%S') 


# In[ ]:


# quantidade de bilhetes emitidos por companhia aerea
df_dt_emissao_bilhete['Companhia Aérea'].value_counts()


# In[ ]:


#Formatando a data de embarque
df['Data Embarque'] = pd.to_datetime(df['Data Embarque'], format='%Y-%m-%d %H:%M:%S') 


# In[ ]:


# quantidade de embarques diurnos emitidos por companhia aerea
df_dt_embarque = df[df['Data Embarque'].dt.hour > 18]
df_dt_embarque['Companhia Aérea'].value_counts()


# In[ ]:


# quantidade de embarques noturno emitidos por companhia aerea
df_dt_embarque = df[df['Data Embarque'].dt.hour > 18]
df_dt_embarque['Companhia Aérea'].value_counts()


# In[9]:


#Quantidade de bilhetes solicitados por situacao
df_group_situacao = df.groupby('Situação Final Bilhete')
df_group_situacao['Situação Final Bilhete'].value_counts()

