import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
 return students.dropna(subset=["name"])
  #.dropna drops all vrows with null values in the [name] column
