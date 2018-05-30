
# coding: utf-8

# In[ ]:


## http://adventofcode.com/2017/day/8


# In[59]:


def func(inp_comm):
    x=inp_comm.split()
    
    if x[1]=='inc':
        d[x[0]]=d.get(x[0])+int(x[2])
    else:
        d[x[0]]=d.get(x[0])-int(x[2])
    return d[x[0]]


# In[55]:


def condition(inp_cond):
    x = inp_cond.split()
    if x[5] == '<':
        return d[x[4]]<int(x[6])
    if x[5] == '<=':
        return d[x[4]]<=int(x[6])
    if x[5] == '==':
        return d[x[4]]==int(x[6])
    if x[5] == '>':
        return d[x[4]]>int(x[6])
    if x[5] == '>=':
        return d[x[4]]>=int(x[6])
    if x[5] == '!=':
        return d[x[4]]!=int(x[6])


# In[42]:


d_src=[]
with open('D8.txt','r') as file:
    for line in file:
        d_src.append(line.split()[0])
print(d_src)


# In[47]:


d= dict.fromkeys(d_src,0)


# In[60]:


max_r = 0
d= dict.fromkeys(d_src,0)
with open('D8.txt','r') as file:
    for line in file:
        if condition(line):
            tmp = func(line)
            if tmp > max_r:
                max_r=tmp
print(d, tmp)


# In[61]:


print(max_r)

