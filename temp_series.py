import pandas as pd
temp=pd.Series([32,39,40,42,38,37,38],
index=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"])
print(temp)
print("maximum temp",temp.max())
print("minimum temp",temp.min())
print("average temp",temp.mean())