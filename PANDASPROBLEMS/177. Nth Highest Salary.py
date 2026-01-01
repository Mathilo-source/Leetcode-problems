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




import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    colName = 'getNthHighestSalary('+str(N)+')'
    df = employee.drop_duplicates(['salary'])
    
    if 0 < N <= df.salary.count():
        df = df.sort_values('salary')
        salary = [df.iloc[-N, 1]]  
    else:
        salary = [None]     
        
    return pd.DataFrame({colName: salary})    
