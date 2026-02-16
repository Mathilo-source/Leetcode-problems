import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
        employees["time_spent"] = employees["out_time"] - employees["in_time"]
        
        # Step 2: Group by event_day and emp_id and sum
        result = (
            employees
            .groupby(["event_day", "emp_id"])["time_spent"]
            .sum()
            .reset_index()
        )
        
        # Step 3: Rename columns
        result.rename(columns={
            "event_day": "day",
            "time_spent": "total_time"
        }, inplace=True)
        
        return result
