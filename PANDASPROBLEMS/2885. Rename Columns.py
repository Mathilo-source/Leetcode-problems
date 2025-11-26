import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(columns={'id':'student_id','first':'first_name','last':'last_name','age':'age_in_years'},inplace=True)
    return students
  
  #.rename() renames the column names
  #Syntax:
# pandas DataFrame .rename() function syntax:
# DataFrame.rename(mapper=None, *, index=None, columns=None, axis=None, inplace=False, errors='ignore')
# - index: dictionary or function to rename rows
# - columns: dictionary or function to rename columns
# - inplace: True to modify the original DataFrame, False to return a new one
# - errors: 'ignore' to skip labels not found, 'raise' (default) to raise an error
  
