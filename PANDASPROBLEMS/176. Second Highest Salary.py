import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Get unique salaries sorted descending
    distinct_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    # Get the second highest salary if it exists, else None
    second_highest_salary = distinct_salaries.iloc[1] if len(distinct_salaries) > 1 else None
    
    # Return result as a DataFrame
    result = pd.DataFrame({'SecondHighestSalary': [second_highest_salary]})
    return result
