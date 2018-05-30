
# coding: utf-8

# In[ ]:


#http://adventofcode.com/2017/day/4


# In[19]:


arr = []
with open('text.txt','r') as src_file:
    for line in src_file:
        arr.append(line.split())
print(arr)


# In[20]:


ctr = 0
for i in arr:
    if len(i) == len(set(i)):
        ctr+=1
print(ctr)


# In[98]:


def wordcheck(tx1:str, tx2:str):
    #счётчик совпадений
    c = 0
    #берём буквы из первого слова
    for i in tx1:
        #и ищем их во втором. если нашли - совпадение +1
        if i in tx2:
            c+=1
        else:
            break
    #Если совпадений столько же, сколько и букв в строке, возвращаем похожесть
    if c == len(tx1):
        return 'same'
    else:
        return 'dif'


# In[184]:


x = 'abcde xyz ecdab'


# In[152]:


print(str_chk(x.split()))


# In[158]:


def str_chk(tx):  
    #вводим критерий валидности
    str_vdty = 'valid'
    #берём кол-во слов в тексте. последнее не с чем сравнивать, поэтому -1
    for st in range(len(tx)-1):
        # создаём две переменные - собственно слово (эталон), которое сравниваем и список оставшихся в листе
        a, *rest = tx[st:len(tx)]
        #для каждого из оставшихся сравниваем длину с эталоном
        for i in rest:
            if len(a)==len(i):
                #если совпадение есть, проверяем их между собой. если два совпадения - буквы одинаковы и можно перещёлкивать 
                #валидность
                if wordcheck(a,i) == 'same' and wordcheck(i,a)=='same':
                    str_vdty ='not valid'
                    break
    if str_vdty == 'not valid':
        #print('string not valid')
        return 0
    else:
        #print('string is valid')
        return 1


# In[159]:


nr = 0
for i in arr:
    nr += str_chk(i)


# In[160]:


print(nr)


# In[ ]:


## А теперь попробуем через словари


# In[161]:


d1 = {'a':1,'b':2,'c':3}


# In[162]:


d2 = {'a':1,'b':2,'c':3}


# In[165]:


print(d1==d2)


# In[166]:


str = 'abbcd'


# In[167]:


d1 = dict.fromkeys(set(str))


# In[169]:


for i in d1:
    d1[i]=str.count(i)


# In[170]:


print(d1)


# In[174]:


def worddict(txt1,txt2):
    d1 = dict.fromkeys(set(txt1))
    d2 = dict.fromkeys(set(txt2))
    for i in d1:
        d1[i]=txt1.count(i)
    for i in d2:
        d2[i]=txt2.count(i)
    if d1==d2:
        return 'strings are the same!'
    else:
        return 'strings are not the same!'


# In[175]:


print(worddict('abcde','edcba'))


# In[176]:


import timeit


# In[190]:


print(timeit.timeit("worddict(x1,x2)", setup="from __main__ import worddict, x1,x2"))


# In[187]:


x = 'abcde ecdab'.split()


# In[189]:


x1 = 'abcde'
x2 = 'ecdab'


# In[191]:


print (timeit.timeit("wordcheck(x1,x2)", setup="from __main__ import wordcheck, x1,x2")), '<= Old'
print (timeit.timeit("worddict(x1,x2)", setup="from __main__ import worddict, x1,x2")), '<- New'


# In[192]:


print(worddict('oiii','ooii'))


# In[193]:


print(wordcheck('oiii','ooii'))

