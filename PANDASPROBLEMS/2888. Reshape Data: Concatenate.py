import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    result = pd.concat([df1, df2], axis=0, ignore_index=True)
    return result
  #pd.concat([df1, df2], axis=0) stacks the rows of df2 below df1.
  #ignore_index=True resets the index so it runs from 0 to n–1.
