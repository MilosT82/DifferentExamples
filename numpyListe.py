
#prvi nacin, ako mi zadajemo listu
import numpy as np
x = np.array([1,1])
print(x)
m=[x,x]
print(m)
m[0][0]=0
print(m)

#drugi nacin formiranja liste, koriscenjem np.ones. Ova funkcija se koristi samo kada imamo jedinice
import numpy as np
a=np.ones(2)
print(a)
b=[a,a]
b[0][0]=0
print(b)

#Drugi nacin spajanja lista
g=a+a 
#postoji jos nekoliko nacina, sto se vidi u prilozenom linku
# https://www.digitalocean.com/community/tutorials/concatenate-lists-python

# m pretvorimo u dataframe 
import pandas as pd
import numpy as np
x=np.ones(2)
print(x)
m=[x,x]
print(m)
df=pd.DataFrame(m)
df
df[0][0]=0
print(df)