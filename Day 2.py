
# coding: utf-8

# In[ ]:


# http://adventofcode.com/2017/day/2


# In[50]:


arr=[]
with open('text.txt','r') as src:
    for x in src:
        arr.append(x.split())


# In[51]:


n=[]
for i in arr:
    n.append(list(map(int,i)))


# In[55]:


chksum=0
tempsum=0
for i in n:
    tempsum=max(i)-min(i)
    chksum+=tempsum
    
print(chksum)


# In[56]:


test_arr= [5,9,2,8]


# In[69]:


t = divmod(5,3)


# In[99]:


def searcher(x:int, inp_arr:list):
    for i in inp_arr:
        divtup=divmod(x,i)
        if divtup[1]==0 and divtup[0] != 1:
            return divtup[0]
        


# In[101]:


res_sum = 0
for i in n:
    for j in i:
        x = searcher(j,i)
        if x is not None:
            res_sum +=x
print(res_sum)

