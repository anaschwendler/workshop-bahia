
# coding: utf-8

# # Licitações - MPBA
# 
# Datasets utilizados disponíveis em: https://www.mpba.mp.br/area/portaltransparencia/biblioteca/1417
# 
# Para desenvolver podemos usar uma aproximação parecida com: https://github.com/rafapetter/suspeitando/blob/master/analise/licitacoes.ipynb

# In[1]:


import pandas as pd
import ezodf

def read_ods(filename, sheet_no=0, header=0):
    tab = ezodf.opendoc(filename=filename).sheets[sheet_no]
    return pd.DataFrame({col[header].value:[x.value for x in col[header+1:]]
                         for col in tab.columns()})


# In[2]:


import glob

licitations_filepaths = glob.glob('../data/*licitacoes_-_planilha_editavel.ods')
licitations_filepaths


# In[3]:


datasets = pd.DataFrame()
for licitation_filepath in licitations_filepaths:
    subset = read_ods(licitation_filepath)
    datasets = datasets.append(subset)
print(datasets.shape)
datasets.head()


# In[4]:


datasets.columns

