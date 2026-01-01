import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Get distinct salaries
    distinct_salaries = employee['salary'].drop_duplicates()
    
    # Sort salaries in descending order
    distinct_salaries = distinct_salaries.sort_values(ascending=False)
    
    # If there are fewer than N distinct salaries
    if len(distinct_salaries) < N:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    # Get the Nth highest salary
    nth_salary = distinct_salaries.iloc[N - 1]
    
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_salary]})
