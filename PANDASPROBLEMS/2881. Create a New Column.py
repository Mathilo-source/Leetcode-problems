import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(bonus=employees["salary"]*2)
  #we use the .assign function to create a new column and assign to it [salary]*2 as the values it should hold
