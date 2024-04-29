import pandas as pd

def concat_dfs(dataframes):
    concat_frames=[dataframe.reset_index(drop=True) for dataframe in dataframes]
    df=pd.concat(concat_frames,ignore_index=True)
    df.reset_index(drop=True,inplace=True)
    return df


import pandas as pd

# Example DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})

# Reset indexes of both DataFrames
df1.reset_index(drop=True, inplace=True)
df2.reset_index(drop=True, inplace=True)

# Concatenate DataFrames
result = pd.concat([df1, df2], axis=0)

print(result)
