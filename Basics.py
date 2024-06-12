# I will be analyzing data from a Wiki article about a List of Helicopter Prison Escapes in the past.
# I aim to analyze the data to answer two questions;
# i) In which year did most helicopter escapes occur?
# ii) Which country had the most attempted prison breaks by helicopter?
# 

# # Analyzing Data

# ## Prison helicopter Escapes

# We begin by importing some helper functions.

# In[1]:


from helper import *


# ## Get the Data

# Now, let's get the data from the [List of helicopter prison escapes]
# (https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes) Wikipedia article.

# In[2]:


url = 'https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes'

data = data_from_url(url)


# Let's print the first three rows:

# In[3]:


for row in data[:3]:
    
    print(row)


# In[4]:


index = 0

for row in data:
    
    data[index] = row[:-1]
    
    index += 1

print(data)


# In[5]:


for row in data:
    
    row[0] = fetch_year(row[0])
    
print(data)
    
    


# In[6]:


print(len(data))
type(data[4][0])
# type(year)


# In[7]:


min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]



i = 0
years = []

for year in range(min_year, max_year):
    
    aa = data[i-1][0]
    
    i += 1
    
aa


# In[8]:


y = []
for row in data:
    
    y.append(row[0])
    
print(y)


# In[9]:


min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]


years = []

attempts_per_year = []

for year in range(min_year,max_year+1):

    years.append(year)
    
    attempts_per_year.append([year,0])
    
    


print(attempts_per_year)


# In[14]:


for row in data:
        
        for year_attempt in attempts_per_year:
        
            year = year_attempt[0] # Instruction 3 - assign the year value in year_attempt to year
            
            
#             print(year)
            if row[0] == year:
            
                year_attempt[1] += 1
                
             
#             print(year_attempt)
                
print(attempts_per_year)


# In[15]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_year)


# Thus, the years 1986, 2001, 2007 and 2009 have the highest numbre of attpemted prison escapes usung a helicopter.

# In[12]:


# Authour: MZwandile Masani (Prime Masani)

"""THIS IS ANOTHER WAY (NON-VISUAL) OF EXTRACTING THE YEAR WITH THE HIGHEST ATTEMPTS."""
cnt_att = []
max_year = []
for i in attempts_per_year:
    
#     if i[1]>

    cnt_att.append(i[1])
    
a = max(cnt_att)

for i in attempts_per_year:

    if i[1]>=a:

        max_year.append(i)


print(a)

print(max_year)
    
"""Note, you could use the same apprrouch to extract the years with 1 or more attempts only.
Thus essentially deleting the years that do not have any attempted escapes.
    Set a to 1 in the if statement."""


# In[13]:


countries_frequency = df["Country"].value_counts()

print_pretty_table(countries_frequency)


# In[ ]:




