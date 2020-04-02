#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1

# I had originally anticipated that former candidate, Andrew Yang, was going to win the election
# After Yang Dropped out, I believed that Joe Biden would win the nomination due to the fact that he has
# a ton of experience in politics and he apeals to a large range of people (former obama supporters)

# I believe that Joe Biden and Donald Trump will be our two candidates for President later this year


# In[7]:


from rcp import get_polls, get_poll_data
from pprint import pprint
import pandas as pd
import pprint as pprint
import matplotlib.pyplot as plt


# In[12]:


# 2 (terminal)

# Troys-MacBook-Pro:~ troysiegler$ pip install realclearpolitics (done in terminal)

# Requirement already satisfied: realclearpolitics in ./anaconda3/lib/python3.6/site-packages (1.2.1)
# Requirement already satisfied: requests in ./anaconda3/lib/python3.6/site-packages (from realclearpolitics) (2.22.0)
# Requirement already satisfied: beautifulsoup4 in ./anaconda3/lib/python3.6/site-packages (from realclearpolitics) (4.7.1)
# Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in ./anaconda3/lib/python3.6/site-packages (from requests->realclearpolitics) (1.24.2)
# Requirement already satisfied: chardet<3.1.0,>=3.0.2 in ./anaconda3/lib/python3.6/site-packages (from requests->realclearpolitics) (3.0.4)
# Requirement already satisfied: certifi>=2017.4.17 in ./anaconda3/lib/python3.6/site-packages (from requests->realclearpolitics) (2019.6.16)
# Requirement already satisfied: idna<2.9,>=2.5 in ./anaconda3/lib/python3.6/site-packages (from requests->realclearpolitics) (2.8)
# Requirement already satisfied: soupsieve>=1.2 in ./anaconda3/lib/python3.6/site-packages (from beautifulsoup4->realclearpolitics) (1.8)
# Troys-MacBook-Pro:~ troysiegler$ 

#Troys-MacBook-Pro:COVID-19 troysiegler$ rcp https://www.realclearpolitics.com/epolls/2020/president/us/2020_democratic_presidential_nomination-6730.html
#Downloading: 2020_democratic_presidential_nomination-6730.csv
#CSV created.
#Troys-MacBook-Pro:COVID-19 troysiegler$


# In[22]:


# 3
# opening the file (deleted RCP average in excel)

democrat = pd.read_csv("2020_democratic_presidential_nomination-6730.csv")
democrat


# In[21]:


# 3 (continued)

# observations about the data

# 1: Sanders and Biden are currently the two front runners
# 2: Sanders has the highest spreads over all of the different types of poles
# 3: Gabbard is the lowest out of all the current candidates


# In[25]:


# 4 

def loadAndCleanData(file):
    lCFile = pd.read_csv(file)
    lCFile.fillna(value = 0, inplace = True)
    return lCFile

cleanFile = loadAndCleanData("2020_democratic_presidential_nomination-6730.csv")


# In[34]:


# 5

def normalizeData(file):
    undecided = []
    for i,v in file.iterrows():
        undecided.append((100 - (v[3] + v[4])))
        
    file["Undecided"] = undecided
    return file


# In[36]:


#6

normalizeData(democrat)


# In[37]:


# 7
# I know a lot of these codes are not outputting graphs because I recently updated my file and most of these 
# candidates have already dropped out
# But I kept the codes in here to prove that at one point they did work

def plotCandidate(candidate, file):
    plt.scatter(y=file[candidate], x=file["Poll"])


# In[43]:


plotCandidate("Warren", democrat)


# In[44]:


plotCandidate("Buttigieg", democrat)


# In[40]:


plotCandidate("Sanders", democrat)


# In[45]:


plotCandidate("Klobuchar", democrat)


# In[46]:


plotCandidate("Steyer", democrat)


# In[42]:


plotCandidate("Bloomberg", democrat)


# In[47]:


plotCandidate("Gabbard", democrat)


# In[39]:


plotCandidate("Biden", democrat)


# In[48]:


# 8 

def statsPerCandidate(candidate, file):
    averagePoll = file[candidate].mean()
    return averagePoll


# In[49]:


# 9
statsPerCandidate("Sanders", democrat)


# In[50]:


statsPerCandidate("Biden", democrat)


# In[ ]:


# the rest of the code for problem 9 will not run due to the fact that I just updated my file, however,
# I have decided to still include them


# In[51]:


statsPerCandidate("Steyer", democrat)
statsPerCandidate("Warren", democrat)
statsPerCandidate("Buttigieg", democrat)
statsPerCandidate("Klobuchar", democrat)
statsPerCandidate("Bloomberg", democrat)
statsPerCandidate("Gabbard", democrat)


# In[58]:


#10

def cleanSample(data):
    LV = []
    RV = []
    for i in data["Sample"]:
        LV.append(i[-2:])
        RV.append(i[:-2])
    for i in range(len(RV)):
        if RV[i] == '':
            RV[i] = 0
        else:
            RV[i] = int(RV[i])
    data["Sample Type"] = LV
    data["Sample Size"] = RV
    data = data.replace('', None)
    return data


# In[62]:


#11

cleanSample(democrat)


# In[73]:


#12

def computePollWeight(data, pollName):
    return sum(data[data['Poll'] == pollName]["Sample Size"]) / sum(data["Sample Size"])


# In[75]:


computePollWeight(democrat, "Morning ConsultM. Consult")


# In[76]:


computePollWeight(democrat, "Politico/Morning ConsultPolitico")


# In[77]:


computePollWeight(democrat, "Reuters/IpsosReuters")


# In[83]:


#13

def weightedStatsPerCandidate(candidate, df):
    weight = []
    for poll in df["Poll"].unique():
        x = sum(df[df["Poll"] == poll][candidate])
        y = computePollWeight(df, poll)
        weight.append(x*y)
    return sum(weight)/len(weight)


# In[87]:


#14
weightedStatsPerCandidate("Biden", democrat)


# In[88]:


weightedStatsPerCandidate("Sanders", democrat)


# In[89]:


# Based on the calculations that I have made above, I believe that Joe Biden is slightly
# more likely to win the nomination over Bernie Sanders


# In[90]:


# 15

def computeCorrelation(candidate1, candidate2, file):
    return file[candidate1].corr(file[candidate2])


# In[92]:


#16 

myCandidate = []
repeat = []

for candidate1 in myCandidate:
    for candidate2 in myCandidate:
        if candidate1 != candidate2:
            if [candidate1, candidate2] not in repeat and [candidate1, candidate2] not in repeat:
                print(candidate1 + "vs" + candidate2 + ": " + computeCorrelation(candidate1, candidate2, file))
                repeat.append([candidate1, candidate2])


# In[93]:


print(computeCorrelation("Biden", "Sanders", democrat))


# In[94]:


# Unfortunatley, due to the fact that I just updated my data file, Biden and Sanders are the only two 
# candidates that are left in the race. However, I ran the Correlation function with both of them and 
# I came out with a score of 0.738, which indicates there may be some correlation between the two (not too much)


# In[113]:


#17

def superTuesday(file, candidates):
    BidenST = []
    SandersST = []
    
    for i, row in file.iterrows():
        Biden = row["Biden"]
        Sanders = row["Sanders"]
        for candidate in candidates:
            if candidate != "Biden" and candidate != "Sanders":
                BidenC = computeCorrelation("Biden", candidate, file)
                SandersC = computeCorrelation("Sanders", candidate, file)
                if abs(BidenC) > abs(SandersC):
                    Biden += row[candidate]
                else:
                    Sander += row[candidate]
            BidenST.append(BidenC)
            SandersST.append(SandersC)
    file["BidenST"] = BidenST
    file["SandersST"] = SandersST


# In[114]:


#18

superTuesday(democrat, myCandidate)
print("Sanders mean is", int(democrat["SandersST"].mean()))
print("Bidens mean is", int(democrat["BidenST"].mean()))
print("Sanders weighted mean is", int(weightedStatsPerCandidate("Sanders", democrat)))
print("Bidens weighted mean is", int(weightedStatsPerCandidate("Biden", democrat)))


# In[118]:


import numpy as np
import scipy.stats


# In[121]:


# 19
def getConfidenceInterval(datacolumn):
    npArray = 1.0 * np.array(datacolumn)
    stdErr = scipy.stats.sem(npArray)
    n = len(datacolumn)
    return stdErr * scipy.stats.t.ppf((1 + .95)/2.0, n-1)


# In[122]:


getConfidenceInterval(democrat["Biden"])


# In[123]:


getConfidenceInterval(democrat["Sanders"])


# In[124]:


# 20
def runTTest(data1, data2):
    return scipy.stats.ttest_ind(data1, data2)


# In[125]:


print(runTTest(democrat["Biden"], democrat["Sanders"]))
print(runTTest(democrat["BidenST"], democrat["SandersST"]))


# In[ ]:




