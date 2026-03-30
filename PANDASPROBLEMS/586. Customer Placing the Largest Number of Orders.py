import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    result=orders["customer_number"].mode().to_frame()
    return result
