import pandas as pd
ages=pd.Series([22,35,58], name="Age")
print(ages)
max = ages.max()
min = ages.min()
print(f"Maximum age: {max}")
print(f"Minimum age: {min}")