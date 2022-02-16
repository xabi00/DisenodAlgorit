#!/usr/bin/env python
# coding: utf-8

# In[1]:


def inss(v):
    for i in range(1,len(v)):
        j=i;
        while j>0 and v[j]<v[j-1]:
            v[j],v[j-1]=v[j-1],v[j];
            j=j-1;
    return(v)


# In[2]:


def bub(v):
    for i in range(len(v)):
        for j in range(0, len(v)-i-1):
            if v[j] > v[j+1] :
                v[j],v[j+1] = v[j+1],v[j]
    return(v)


# In[3]:


def merg(v):
    if len(v) > 1:
        mid = len(v)//2;
        L = v[:mid];
        R = v[mid:];
        merg(L);
        merg(R);
        i = j = k = 0;
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                v[k] = L[i];
                i += 1;
            else:
                v[k] = R[j];
                j += 1;
            k += 1
        while i < len(L):
            v[k] = L[i];
            i += 1;
            k += 1;
        while j < len(R):
            v[k] = R[j];
            j += 1;
            k += 1;
    return(v)


# In[4]:


def heapify(v,n,i):
    larg = i;
    l = 2 * i + 1; 
    r = 2 * i + 2;    
 
    if l < n and v[larg] < v[l]:
        larg = l;
 
    if r < n and v[larg] < v[r]:
        larg = r;
 
    if larg != i:
        v[i], v[larg] = v[larg], v[i] 
 
        heapify(v, n, larg)


# In[5]:


def heaps(v):
    n=len(v);
    for i in range(n//2 - 1, -1, -1):
        heapify(v, n, i)
    for i in range(n-1, 0, -1):
        v[i], v[0] = v[0], v[i]
        heapify(v, i, 0)
    return(v)


# In[6]:


def partition(v, l, h):
    i = (l-1)  
    pivot = v[h]   
 
    for j in range(l, h):
        if v[j] <= pivot:
            i = i+1
            v[i], v[j] = v[j], v[i]
 
    v[i+1], v[h] = v[h], v[i+1]
    return (i+1)


# In[7]:


def quicks(v, l, h):
    if len(v) == 1:
        return v
    if l < h:
        pi = partition(v, l, h)

        quicks(v, l, pi-1)
        quicks(v, pi+1, h)
    return(v)


# In[8]:


import random
def rlis(n):
    v=[]
    for i in range(n):
        v.append(random.randint(-10000, 10000))
    return(v)


# In[9]:


import random
def inlis(n):
    v=[]
    k=int(-10000)
    for i in range(n):
        s=random.randint(k, k+10000)
        v.insert(0,s)
        k=s
    return(v)


# In[33]:


import random,timeit
for k in range(10):
    n=random.randint(1,41)
    print('Algoritmos para un vector aleatorio de tamaño',n)
    v=rlis(n)
    print(v)
    t1=timeit.default_timer()
    inss(v)
    t2=timeit.default_timer()
    print('InsertionSort tarda',t2-t1,'segundos en ordenar el vector.')
    t3=timeit.default_timer()
    bub(v)
    t4=timeit.default_timer()
    print('BubleSort tarda',t4-t3,'segundos en ordenar el vector.')
    t5=timeit.default_timer()
    merg(v)
    t6=timeit.default_timer()
    print('MergeSort tarda',t6-t5,'segundos en ordenar el vector.')
    t7=timeit.default_timer()
    heaps(v)
    t8=timeit.default_timer()
    print('HeapSort tarda',t8-t7,'segundos en ordenar el vector.')
    t9=timeit.default_timer()
    quicks(v,0,n-1)
    t10=timeit.default_timer()
    print('QuickSort tarda',t10-t9,'segundos en ordenar el vector.')
    print('El vector ordenado es',inss(v))
    print('Algoritmos para un vector inversamente ordenado de tamaño',n)
    v=inlis(n)
    print(v)
    t1=timeit.default_timer()
    inss(v)
    t2=timeit.default_timer()
    print('InsertionSort tarda',t2-t1,'segundos en ordenar el vector.')
    t3=timeit.default_timer()
    bub(v)
    t4=timeit.default_timer()
    print('BubleSort tarda',t4-t3,'segundos en ordenar el vector.')
    t5=timeit.default_timer()
    merg(v)
    t6=timeit.default_timer()
    print('MergeSort tarda',t6-t5,'segundos en ordenar el vector.')
    t7=timeit.default_timer()
    heaps(v)
    t8=timeit.default_timer()
    print('HeapSort tarda',t8-t7,'segundos en ordenar el vector.')
    t9=timeit.default_timer()
    quicks(v,0,n-1)
    t10=timeit.default_timer()
    print('QuickSort tarda',t10-t9,'segundos en ordenar el vector.')
    print('El vector ordenado es',inss(v))


# In[44]:


import random,timeit
import matplotlib.pyplot as plt
t_i=[]
t_b=[]
t_m=[]
t_h=[]
t_q=[]
for k in range(1,750):
    v=rlis(k)
    t1=timeit.default_timer()
    inss(v)
    t2=timeit.default_timer()
    t_i.append(t2-t1)
    t3=timeit.default_timer()
    bub(v)
    t4=timeit.default_timer()
    t_b.append(t4-t3)
    t5=timeit.default_timer()
    merg(v)
    t6=timeit.default_timer()
    t_m.append(t6-t5)
    t7=timeit.default_timer()
    heaps(v)
    t8=timeit.default_timer()
    t_h.append(t8-t7)
    t9=timeit.default_timer()
    quicks(v,0,k-1)
    t10=timeit.default_timer()
    t_q.append(t10-t9)
    v=inlis(k)
    t1=timeit.default_timer()
    inss(v)
    t2=timeit.default_timer()
    t3=timeit.default_timer()
    bub(v)
    t4=timeit.default_timer()
    t5=timeit.default_timer()
    merg(v)
    t6=timeit.default_timer()
    t7=timeit.default_timer()
    heaps(v)
    t8=timeit.default_timer()
    t9=timeit.default_timer()
    quicks(v,0,k-1)
    t10=timeit.default_timer()
plt.figure(figsize=(12, 6))
plt.bar(range(1,750), t_i)
plt.xlabel('Tamaño del Vector')
plt.ylabel('Tiempo de ejecución')
plt.title('InsertionSort')
plt.show()
plt.figure(figsize=(12, 6))
plt.bar(range(1,750), t_b)
plt.xlabel('Tamaño del Vector')
plt.ylabel('Tiempo de ejecución')
plt.title('BubleSort')
plt.show()
plt.figure(figsize=(12, 6))
plt.bar(range(1,750), t_m)
plt.xlabel('Tamaño del Vector')
plt.ylabel('Tiempo de ejecución')
plt.title('MergeSort')
plt.show()
plt.figure(figsize=(12, 6))
plt.bar(range(1,750), t_h)
plt.xlabel('Tamaño del Vector')
plt.ylabel('Tiempo de ejecución')
plt.title('HeapSort')
plt.show()
plt.figure(figsize=(12, 6))
plt.bar(range(1,750), t_q)
plt.xlabel('Tamaño del Vector')
plt.ylabel('Tiempo de ejecución')
plt.title('QuickSort')
plt.show()


# In[43]:


import random,timeit
import matplotlib.pyplot as plt
t_i=[]
t_b=[]
t_m=[]
t_h=[]
t_q=[]
for k in range(1,750):
    v=inlis(k)
    t1=timeit.default_timer()
    inss(v)
    t2=timeit.default_timer()
    t_i.append(t2-t1)
    t3=timeit.default_timer()
    bub(v)
    t4=timeit.default_timer()
    t_b.append(t4-t3)
    t5=timeit.default_timer()
    merg(v)
    t6=timeit.default_timer()
    t_m.append(t6-t5)
    t7=timeit.default_timer()
    heaps(v)
    t8=timeit.default_timer()
    t_h.append(t8-t7)
    t9=timeit.default_timer()
    quicks(v,0,k-1)
    t10=timeit.default_timer()
    t_q.append(t10-t9)
    v=inlis(k)
    t1=timeit.default_timer()
    inss(v)
    t2=timeit.default_timer()
    t3=timeit.default_timer()
    bub(v)
    t4=timeit.default_timer()
    t5=timeit.default_timer()
    merg(v)
    t6=timeit.default_timer()
    t7=timeit.default_timer()
    heaps(v)
    t8=timeit.default_timer()
    t9=timeit.default_timer()
    quicks(v,0,k-1)
    t10=timeit.default_timer()
plt.figure(figsize=(12, 6))
plt.bar(range(1,750), t_i)
plt.xlabel('Tamaño del Vector')
plt.ylabel('Tiempo de ejecución')
plt.title('InsertionSort')
plt.show()
plt.figure(figsize=(12, 6))
plt.bar(range(1,750), t_b)
plt.xlabel('Tamaño del Vector')
plt.ylabel('Tiempo de ejecución')
plt.title('BubleSort')
plt.show()
plt.figure(figsize=(12, 6))
plt.bar(range(1,750), t_m)
plt.xlabel('Tamaño del Vector')
plt.ylabel('Tiempo de ejecución')
plt.title('MergeSort')
plt.show()
plt.figure(figsize=(12, 6))
plt.bar(range(1,750), t_h)
plt.xlabel('Tamaño del Vector')
plt.ylabel('Tiempo de ejecución')
plt.title('HeapSort')
plt.show()
plt.figure(figsize=(12, 6))
plt.bar(range(1,750), t_q)
plt.xlabel('Tamaño del Vector')
plt.ylabel('Tiempo de ejecución')
plt.title('QuickSort')
plt.show()

