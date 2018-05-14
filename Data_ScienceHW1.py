
# coding: utf-8

# In[1]:


import pandas as pd
import csv
import os
import sys
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from pandas.core.frame import DataFrame
import math
import operator


# In[2]:


test = pd.read_csv("testing_data.csv")


# In[3]:


df = pd.read_csv("training_data.csv")


# In[4]:


df


# In[5]:


test


# In[5]:


houses = df.housing  #有無房子
ages = df.age    #年紀
jobs = df.job    #職業
maritals = df.marital #婚姻
edus = df.education    #教育
loans = df.loan       #貸款
balances = df.balance 
contacts = df.contact
campaigns = df.campaign
durations = df.duration
pdayss = df.pdays
previouss = df.previous
ys = df.y

test_houses = test.housing  #有無房子
test_ages = test.age    #年紀
test_jobs = test.job    #職業
test_maritals = test.marital #婚姻
test_edus = test.education    #教育
test_loans = test.loan       #貸款
test_balances = test.balance
test_contacts = test.contact
test_campaigns = test.campaign
test_durations = test.duration
test_pdayss = test.pdays
test_previouss = test.previous


# In[6]:


house=[]
age = []
job = []
marital =[]
edu = []
loan = []
balance = []
contact = []
campaign = []
duration = []
pdays = []
previous = []
y = []

test_house=[]
test_age = []
test_job = []
test_marital =[]
test_edu = []
test_loan = []
test_balance = []
test_contact = []
test_campaign = []
test_duration = []
test_pdays = []
test_previous = []


# In[7]:


for i in balances:
    balance+=[i]
for i in test_balances:
    test_balance+=[i]


# In[8]:


for i in ages:
    age+=[i]
for i in test_ages:
    test_age+=[i]


# In[9]:


for i in campaigns:
    campaign+=[i]
for i in test_campaigns:
    test_campaign+=[i]


# In[10]:


for i in pdayss:
    pdays+=[i]
for i in test_pdayss:
    test_pdays+=[i]


# In[11]:


for i in durations:
    duration+=[i]
for i in test_durations:
    test_duration+=[i]


# In[12]:


for i in previouss:
    previous+=[i]
for i in test_previouss:
    test_previous+=[i]


# In[13]:


for i in houses:
    if(i=="yes"):
        house+=[1]
    else:
        house+=[0]
for i in test_houses:
    if(i=="yes"):
        test_house+=[1]
    else:
        test_house+=[0]


# In[14]:


for i in ys:
    if(i=="yes"):
        y+=[1]
    else:
        y+=[0]


# In[15]:


for i in maritals:
    if(i=="married"):
        marital+=[0]#結婚= 0  未婚 =1 離婚 =2
    elif(i=="single"):
        marital+=[1]
    elif(i=="divorced"):
        marital+=[2]
for i in test_maritals:
    if(i=="married"):
        test_marital+=[0]#結婚= 0  未婚 =1 離婚 =2
    elif(i=="single"):
        test_marital+=[1]
    elif(i=="divorced"):
        test_marital+=[2]


# In[16]:


for i in edus:
    if(i=="primary"):
        edu+=[0]
    elif(i=="secondary"):
        edu+=[1]
    elif(i=="tertiary"):
        edu+=[2]
    elif(i=="unknown"):
        edu+=[3]
for i in test_edus:
    if(i=="primary"):
        test_edu+=[0]
    elif(i=="secondary"):
        test_edu+=[1]
    elif(i=="tertiary"):
        test_edu+=[2]
    elif(i=="unknown"):
        test_edu+=[3]


# In[17]:


for i in loans:
    if(i=="yes"):
        loan+=[1]
    else:
        loan+=[0]
for i in test_loans:
    if(i=="yes"):
        test_loan+=[1]
    else:
        test_loan+=[0]


# In[18]:


for i in jobs:
    if(i=="services"):   #services=0
        job+=[0]
    elif(i=="management"): #management=1
        job+=[1]
    elif(i=="admin."): #admin=2
        job+=[2]
    elif(i=="technician"): #technician=3
        job+=[3]
    elif(i=="blue-collar"): #blue-collar=4
        job+=[4]
    elif(i=="housemaid"): #housemaid=5
        job+=[5]
    elif(i=="entrepreneur"): #entrepreneur=6
        job+=[6]
    elif(i=="unemployed"): #unemployed=7
        job+=[7]
    elif(i=="student"): #student=8
        job+=[8]
    elif(i=="retired"): #retired=9
        job+=[9]
    elif(i=="self-employed"): #self-employed=10
        job+=[10]
    elif(i=="unknown"): #unknown=11
        job+=[11]
        
for i in test_jobs:
    if(i=="services"):   #services=0
        test_job+=[0]
    elif(i=="management"): #management=1
        test_job+=[1]
    elif(i=="admin."): #admin=2
        test_job+=[2]
    elif(i=="technician"): #technician=3
        test_job+=[3]
    elif(i=="blue-collar"): #blue-collar=4
        test_job+=[4]
    elif(i=="housemaid"): #housemaid=5
        test_job+=[5]
    elif(i=="entrepreneur"): #entrepreneur=6
        test_job+=[6]
    elif(i=="unemployed"): #unemployed=7
        test_job+=[7]
    elif(i=="student"): #student=8
        test_job+=[8]
    elif(i=="retired"): #retired=9
        test_job+=[9]
    elif(i=="self-employed"): #self-employed=10
        test_job+=[10]
    elif(i=="unknown"): #unknown=11
        test_job+=[11]


# In[19]:


for i in contacts:
    if(i=="cellular"):
        contact+=[0]
    elif(i=="telephone"):
        contact+=[1]
    elif(i=="unknown"):
        contact+=[2]
for i in test_contacts:
    if(i=="cellular"):
        test_contact+=[0]
    elif(i=="telephone"):
        test_contact+=[1]
    elif(i=="unknown"):
        test_contact+=[2]


# In[20]:


c={"age" : age,
   "job" : job,
   "marital" : marital,
   "edu" : edu,
   "loan" : loan,
   "housing" : house,
   "contact" : contact,
   "campaign" : campaign,
   "previous" : previous,
   "y" : y}

d={"age" : test_age,
   "job" : test_job,
   "marital" : test_marital,
   "edu" : test_edu,
   "loan" : test_loan,
   "housing" : test_house,
   "contact" : test_contact,
   "campaign" : test_campaign,
   "previous" : test_previous}


# In[21]:


training_data=DataFrame(c)


# In[22]:


test_data=DataFrame(d)


# In[25]:


ans =[]
id_index = []
dist = 0
for x in range(len(test_data)):
    id_index+=[x]
    distance = []
    for j in range(len(training_data)):
        for index in range(len(test_data.columns)):
            dist+=pow((test_data.values[x][index]-training_data.values[j][index]),2)
        distance+=[math.sqrt(dist)]
        dist = 0
    yes = 0
    no = 0
    sortss = []
    for i in range(len(training_data)):
        sortss.append((y[i],distance[i]))
    sortss.sort(key =operator.itemgetter(1))
    for i in range(5):
        if(sortss[i][0]==0):
            no+=1
        elif(sortss[i][0]==1):
            yes+=1
    if(yes>no):
        ans +=[1]
    elif(yes<no):
        ans +=[0]


# In[30]:


output = []


# In[31]:


for i in range(4522):
    output.append((id_index[i],ans[i]))


# In[32]:


an = 0
bn = 0
for i in range(4522):
    if(ans[i]==1):
        an+=1
    elif(ans[i]==0):
        bn+=1
    else:
        print("error")


# In[33]:


bn


# In[34]:


an


# In[35]:


with open('output.csv', 'w', newline='') as csvfile:
  # 建立 CSV 檔寫入器
  writer = csv.writer(csvfile)

  # 寫入一列資料
  writer.writerow(['id', 'ans'])

  # 寫入另外幾列資料
  for i in range(4522):
        writer.writerow([id_index[i],ans[i]])

