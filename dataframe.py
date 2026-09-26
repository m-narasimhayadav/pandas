import pandas as pd
l=list(range(1,6))
s=pd.Series(l,name='numbers')
print(s)
d={'name':['narasimha','ravi','madhavi'],
    'branch':['cse','cec','ece']
  }
df=pd.DataFrame(d)
print(df)
