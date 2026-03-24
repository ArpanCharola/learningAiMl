#4 (Given a Pandas DataFrame representing a dataset,
# write a snippet to check for missing values (NaN) and replace
# them with the mean of that column.)
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A' : [1, 2, np.nan, 4],
    'B' : [5, 6, np.nan, 7],
    'C' : [8, np.nan, 10, 11],
})

print("Original Dataframe:")
print(df)

#check missingValues
print("\nMissing values per column:")
print(df.isnull().sum())

df_filled = df.fillna(df.mean())
print("\nDataFrame after filling NANs with column means:")
print(df_filled)

