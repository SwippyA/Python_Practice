import pandas as pd

df = pd.DataFrame([[1,2,2,3],[33,33,3,22],[4,5,10,22]],columns=["A","C","B","D"])
print(df['A'].nunique())